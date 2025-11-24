import os 
import shutil 
from PIL import Image, ImageEnhance
import glob

def make_dir(dir): 
    if not os.path.exists(dir):
        os.makedirs(dir)


def apply_sepia(img):
    width, height = img.size
    pixels = img.load()
    
    for py in range(height):
        for px in range(width):
            r, g, b = img.getpixel((px, py))
            
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)
            
            pixels[px, py] = (min(255, tr), min(255, tg), min(255, tb))
    
    return img

def process_image(input_path, output_path):
    """
    Обрабатывает изображение: применяет ЧБ фильтр, настраивает контрастность,
    резкость и яркость
    """
    try:
        # Открываем изображение
        with Image.open(input_path) as img:
            # Конвертируем в RGB если нужно (для PNG с прозрачностью)
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            
            # Применяем черно-белый фильтр
            img_bw = img.convert('L')
            # Конвертируем обратно в RGB для дальнейшей обработки
            img_processed = img_bw.convert('RGB')
            
            # Увеличиваем контрастность (1.5 - умеренное увеличение)
            enhancer = ImageEnhance.Contrast(img_processed)
            img_processed = enhancer.enhance(1.5)
            
            # Увеличиваем резкость (1.2 - легкое увеличение)
            sharpness_enhancer = ImageEnhance.Sharpness(img_processed)
            img_processed = sharpness_enhancer.enhance(1.2)
            
            # Настраиваем яркость (1.1 - легкое увеличение)
            brightness_enhancer = ImageEnhance.Brightness(img_processed)
            img_processed = brightness_enhancer.enhance(1.1)
            
            # Сохраняем обработанное изображение
            img_processed.save(output_path, quality=95)
            print(f"Обработано: {os.path.basename(input_path)}")
            
    except Exception as e:
        print(f"Ошибка при обработке {input_path}: {str(e)}")
        
        
def sveta_filter(input_path, output_path):
    try:
        with Image.open(input_path) as img:
            # Конвертируем в RGB если нужно
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            
            # ========== ОСНОВНЫЕ ЦВЕТОВЫЕ ХАРАКТЕРИСТИКИ ==========
            
            # 1. ЯРКОСТЬ (Brightness)
            brightness_enhancer = ImageEnhance.Brightness(img)
            img = brightness_enhancer.enhance(1.2)  # >1 - ярче, <1 - темнее
            
            # 2. КОНТРАСТНОСТЬ (Contrast)
            contrast_enhancer = ImageEnhance.Contrast(img)
            img = contrast_enhancer.enhance(1.3)  # >1 - контрастнее, <1 - мягче
            
            # 3. НАСЫЩЕННОСТЬ (Color)
            color_enhancer = ImageEnhance.Color(img)
            img = color_enhancer.enhance(0.8)  # >1 - насыщеннее, <1 - бледнее
            
            # 4. РЕЗКОСТЬ (Sharpness)
            sharpness_enhancer = ImageEnhance.Sharpness(img)
            img = sharpness_enhancer.enhance(1.5)  # >1 - резче, <1 - размытее
            
            # ========== СПЕЦИАЛЬНЫЕ ФИЛЬТРЫ ==========
            
            # 5. ЧЕРНО-БЕЛЫЙ (Grayscale)
            # img = img.convert('L').convert('RGB')  # раскомментировать для ЧБ
            
            # 6. СЕПИЯ (Sepia tone)
            # img = apply_sepia(img)  # см. функцию ниже
            
            # 7. ИНВЕРСИЯ ЦВЕТОВ (Negative)
            # img = ImageOps.invert(img)
            
            # 8. ПОСТЕРИЗАЦИЯ (уменьшение цветов)
            # img = ImageOps.posterize(img, bits=4)  # 4 бита = 16 цветов
            
            # 9. СОЛНЕЧНЫЙ СВЕТ (Solarize) - инвертирует светлые тона
            # img = ImageOps.solarize(img, threshold=128)
            
            # 10. АВТОКОНТРАСТ
            # img = ImageOps.autocontrast(img, cutoff=2)
            
            # 11. ВЫРАВНИВАНИЕ ЦВЕТОВ (Equalize)
            # img = ImageOps.equalize(img)
            
            # ========== ЦВЕТОВЫЕ КОРРЕКЦИИ ==========
            
            # 12. ТЕПЛЫЕ/ХОЛОДНЫЕ ТОНА
            # img = apply_color_balance(img, temperature=0.1)  # >0 - теплее, <0 - холоднее
            
            # 13. ВИНТАЖНЫЙ ЭФФЕКТ
            # img = apply_vintage_effect(img)
            
            # 14. ПОВЫШЕНИЕ ЧЕТКОСТИ
            # img = img.filter(ImageFilter.DETAIL)
            
            # 15. ЛЕГКОЕ РАЗМЫТИЕ
            # img = img.filter(ImageFilter.SMOOTH)
            
            # 16. УСИЛЕНИЕ КРАСНЫХ ТОНОВ
            # img = enhance_reds(img, factor=1.2)
            
            # ========== ДОПОЛНИТЕЛЬНЫЕ ЭФФЕКТЫ ==========
            
            # 17. ВИНЬЕТКА (затемнение краев)
            # img = apply_vignette(img, strength=0.8)
            
            # 18. ШУМ (Grain)
            # img = add_film_grain(img, intensity=0.1)
            
            # Сохраняем результат
            img.save(output_path, quality=95, optimize=True)
            print(f"✅ Обработано: {os.path.basename(input_path)}")
            
    except Exception as e:
        print(f"❌ Ошибка при обработке {input_path}: {str(e)}")

# ========== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ДЛЯ ФИЛЬТРОВ ==========

def apply_sepia(img):
    """Применяет сепию эффект"""
    width, height = img.size
    pixels = img.load()
    
    for py in range(height):
        for px in range(width):
            r, g, b = img.getpixel((px, py))
            
            # Формула для сепии
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)
            
            pixels[px, py] = (min(255, tr), min(255, tg), min(255, tb))
    
    return img

def apply_color_balance(img, temperature=0.0):
    """Корректирует цветовую температуру"""
    # temperature > 0 - теплее (желтее)
    # temperature < 0 - холоднее (синее)
    r_enhancer = ImageEnhance.Color(img)
    g_enhancer = ImageEnhance.Color(img)
    b_enhancer = ImageEnhance.Color(img)
    
    # Разделяем каналы
    r, g, b = img.split()
    
    # Усиливаем/ослабляем каналы в зависимости от температуры
    r = r_enhancer.enhance(1.0 + temperature)
    g = g_enhancer.enhance(1.0 + temperature * 0.5)
    b = b_enhancer.enhance(1.0 - temperature)
    
    # Объединяем обратно
    return Image.merge('RGB', (r, g, b))

def enhance_reds(img, factor=1.2):
    """Усиливает красные тона"""
    # Разделяем каналы
    r, g, b = img.split()
    
    # Усиливаем красный канал
    r_enhancer = ImageEnhance.Brightness(r)
    r = r_enhancer.enhance(factor)
    
    # Объединяем обратно
    return Image.merge('RGB', (r, g, b))

def apply_vintage_effect(img):
    """Винтажный эффект с теплыми тонами и легкой сепией"""
    # Сначала теплые тона
    img = apply_color_balance(img, temperature=0.15)
    
    # Затем сепия
    img = apply_sepia(img)
    
    # Немного уменьшаем насыщенность
    color_enhancer = ImageEnhance.Color(img)
    img = color_enhancer.enhance(0.7)
    
    # Добавляем контраст
    contrast_enhancer = ImageEnhance.Contrast(img)
    return contrast_enhancer.enhance(1.2)
# Основной код
desktop_path = os.path.expanduser("~/Desktop")
photo_dir_begin = os.path.join(desktop_path, "photo")
photo_dir_end = os.path.join(desktop_path, "photo_end")

# Создаем папки если их нет
make_dir(photo_dir_begin)
make_dir(photo_dir_end)

# Поддерживаемые форматы изображений
supported_formats = ('*.jpg', '*.jpeg', '*.png', '*.bmp', '*.tiff', '*.webp')

# Получаем список всех изображений
file_list = []
for format in supported_formats:
    file_list.extend(glob.glob(os.path.join(photo_dir_begin, format)))

print(f"Найдено {len(file_list)} изображений для обработки")

# Обрабатываем каждое изображение
for file_path in file_list:
    if os.path.isfile(file_path):
        # Создаем имя для выходного файла
        filename = os.path.basename(file_path)
        name, ext = os.path.splitext(filename)
        output_filename = f"{name}_processed{ext}"
        output_path = os.path.join(photo_dir_end, output_filename)
        
        # Обрабатываем изображение
        # process_image(file_path, output_path)
        sveta_filter(file_path, output_path)

print("Обработка завершена!")