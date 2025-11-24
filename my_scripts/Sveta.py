#!/usr/bin/env python3
"""
sveta_match_ps.py
Применяет преобразование, вычисленное по паре (before, after),
ко всем изображениям в ~/Desktop/photo -> ~/Desktop/photo_end.

По умолчанию использует:
 - before:  /mnt/data/_MG_0239.JPG
 - after:   /mnt/data/_MG_0239_processed.JPG

Чтобы использовать свои файлы, отредактируй переменные `ref_before_path` и `ref_after_path`.
"""
import os
import glob
import cv2
import numpy as np
from PIL import Image, ImageEnhance
from skimage import exposure

# -----------------------
# ПУТИ (поменяй, если нужно)
# -----------------------
desktop = os.path.expanduser("~/Desktop")
INPUT_DIR = os.path.join(desktop, "photo")
OUTPUT_DIR = os.path.join(desktop, "photo_end")
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Референс "до" и "после" — используем те, что ты прислал.
ref_before_path = "/Users/qwertz/Desktop/_MG_0239.JPG"
ref_after_path  = "/Users/qwertz/Desktop/фото.jpg"

# Поддерживаемые форматы
EXTS = ("*.jpg","*.jpeg","*.png","*.webp","*.tiff","*.bmp" , "*JPG", "*JPEG", "*PNG", "*WEBP", "*TIFF", "*BMP")


# -----------------------
# УТИЛИТЫ
# -----------------------
def imread_rgb(path):
    bgr = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if bgr is None:
        return None
    if bgr.ndim == 2:
        rgb = cv2.cvtColor(bgr, cv2.COLOR_GRAY2RGB)
    else:
        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    return rgb

def imwrite_rgb(path, rgb):
    bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
    cv2.imwrite(path, bgr, [int(cv2.IMWRITE_JPEG_QUALITY), 95])


# -----------------------
# СТРОИМ ЛУК-ТАБЛИЦУ ПО PIXEL PAIRS
# -----------------------
def build_channel_lut(before_rgb, after_rgb, bins=256):
    """
    Строим 1D LUT для каждого канала методом усреднения
    выходной интенсивности для каждого входного бина и интерполяцией.
    """
    # ожидаем одинаковый размер; если нет — ресайзим референс "after" под "before"
    if before_rgb.shape != after_rgb.shape:
        after_rgb = cv2.resize(after_rgb, (before_rgb.shape[1], before_rgb.shape[0]), interpolation=cv2.INTER_LINEAR)

    luts = []
    for ch in range(3):
        src = before_rgb[..., ch].ravel().astype(np.int32)
        dst = after_rgb[..., ch].ravel().astype(np.int32)
        # для устойчивости возьмём случайную выборку (если картинка большая)
        if src.size > 500000:
            idx = np.random.choice(src.size, size=500000, replace=False)
            src_s = src[idx]
            dst_s = dst[idx]
        else:
            src_s = src; dst_s = dst
        # средний dst по src-бинам
        bins_edges = np.arange(257)  # 0..256
        sums = np.zeros(256, dtype=np.float64)
        counts = np.zeros(256, dtype=np.int64)
        inds = src_s  # 0..255
        for i in range(src_s.size):
            v = inds[i]
            sums[v] += dst_s[i]
            counts[v] += 1
        # избегаем деления на 0
        avg = np.zeros(256, dtype=np.float64)
        has = counts > 0
        avg[has] = sums[has] / counts[has]
        # заполнение пустых значений интерполяцией
        x = np.where(has)[0]
        if x.size == 0:
            # fallback identity
            lut = np.arange(256)
        else:
            y = avg[has]
            interp = np.interp(np.arange(256), x, y)
            lut = np.clip(interp, 0, 255).astype(np.uint8)
        luts.append(lut)
    return luts  # list of three arrays length 256


def apply_lut_to_img(img_rgb, luts):
    out = img_rgb.copy()
    for ch in range(3):
        out[..., ch] = luts[ch][out[..., ch]]
    return out


# -----------------------
# ДОПОЛНИТЕЛЬНЫЕ ЛОКАЛЬНЫЕ ПОДТЯГИВАНИЯ
# -----------------------
def local_adjustments(img_rgb):
    """
    - конвертируем в Lab, применим CLAHE к L-каналу (деликатно),
    - вернём, немного усилим vibrance, saturation и легкую резкость с маской краёв.
    """
    # CLAHE на L
    lab = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2LAB).astype(np.float32)
    L, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    L2 = clahe.apply(L.astype(np.uint8)).astype(np.float32)
    lab2 = cv2.merge((L2, a, b))
    rgb2 = cv2.cvtColor(lab2.astype(np.uint8), cv2.COLOR_LAB2RGB)

    # Vibrance: усиление насыщенности, но меньше для уже насыщенных пикселей
    hsv = cv2.cvtColor(rgb2, cv2.COLOR_RGB2HSV).astype(np.float32)
    h,s,v = cv2.split(hsv)
    # усиливаем s в тех местах, где s < 150
    mask_low = (s < 150).astype(np.float32)
    s = np.clip(s + mask_low * 15.0, 0, 255)
    hsv2 = cv2.merge((h,s,v)).astype(np.uint8)
    rgb3 = cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB)

    # Лёгкая резкость на краях, без затрагивания гладких областей:
    gray = cv2.cvtColor(rgb3, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    edges = cv2.dilate(edges, np.ones((3,3), np.uint8), iterations=1)
    edges = cv2.GaussianBlur(edges.astype(np.float32), (0,0), sigmaX=2)/255.0
    edges = edges[..., None]

    # unsharp mask
    blur = cv2.GaussianBlur(rgb3, (0,0), sigmaX=1.2)
    sharp = np.clip(rgb3.astype(np.float32)*(1.15) - blur.astype(np.float32)*0.15, 0, 255).astype(np.uint8)

    # смешивание sharp только на границах
    out = (rgb3.astype(np.float32)*(1-edges) + sharp.astype(np.float32)*edges).astype(np.uint8)
    return out


# -----------------------
# ОСНОВНОЙ ПАЙПЛАЙН
# -----------------------
def compute_and_apply(ref_before, ref_after, image_paths):
    print("Чтение референса...")
    before = imread_rgb(ref_before)
    after  = imread_rgb(ref_after)
    if before is None or after is None:
        raise RuntimeError("Не удалось загрузить референсы. Проверьте пути.")

    print("Построение LUT по референсам (это займёт ~10-30с)...")
    luts = build_channel_lut(before, after)

    print("Обработка файлов...")
    for p in image_paths:
        print("->", os.path.basename(p))
        img = imread_rgb(p)
        if img is None:
            print("   ! не удалось прочитать, пропускаю")
            continue

        # 1) применим LUT
        out = apply_lut_to_img(img, luts)

        # 2) локальная доработка (CLAHE, vibrance, мягкая резкость)
        out = local_adjustments(out)

        # 3) УБРАНА ЗАЩИТА ЛИЦ - теперь все изображение обрабатывается одинаково

        # 4) финальная легкая тональная корректировка - match_histogram немного по каналам
        # используем skimage exposure.match_histograms для финального приближения к референсу
        try:
            out = exposure.match_histograms(out, after, multichannel=True)
            out = np.clip(out, 0, 255).astype(np.uint8)
        except Exception:
            # если match_histograms не работает (очень большие размеры) — пропускаем
            pass

        # 5) сохранить (с суффиксом)
        name = os.path.splitext(os.path.basename(p))[0]
        ext  = os.path.splitext(p)[1]
        out_path = os.path.join(OUTPUT_DIR, f"{name}_psmatch{ext}")
        imwrite_rgb(out_path, out)
        print("   сохранено:", out_path)

    print("Готово.")


# -----------------------
# Запуск
# -----------------------
if __name__ == "__main__":
    # список файлов в папке INPUT_DIR
    files = []
    for ex in EXTS:
        files.extend(glob.glob(os.path.join(INPUT_DIR, ex)))
    files = sorted(files)
    print("Найдено:", len(files), "файлов для обработки в", INPUT_DIR)
    if len(files) == 0:
        print("Положи, пожалуйста, исходники в", INPUT_DIR, "и запусти снова.")
    else:
        compute_and_apply(ref_before_path, ref_after_path, files)

    print("Готово.")