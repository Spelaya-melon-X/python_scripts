import cv2
import numpy as np
import datetime

output_file = '27.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

zoom = 1.0
out = cv2.VideoWriter(output_file, fourcc, 10.0, (1280, 720))

print("Управление:")
print("  q — выход")
print("  w — увеличить масштаб")
print("  s — уменьшить масштаб")
print("  p — сохранить скриншот")

while cap.isOpened(): # начинаем з
    ret, frame = cap.read()
    if not ret:
        print("Не удалось прочитать кадр.")
        break

    # --- Масштабирование ---
    h, w = frame.shape[:2]
    center_x, center_y = w // 2, h // 2
    new_w, new_h = int(w / zoom), int(h / zoom)
    x1, y1 = center_x - new_w // 2, center_y - new_h // 2
    x2, y2 = center_x + new_w // 2, center_y + new_h // 2
    zoomed_frame = frame[y1:y2, x1:x2]
    zoomed_frame = cv2.resize(zoomed_frame, (w, h))

    out.write(zoomed_frame)
    cv2.imshow('Video', zoomed_frame)

    key = cv2.waitKey(10) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('w'):  # увеличить
        zoom = min(zoom + 0.1, 3.0)
        print(f"Масштаб: {zoom:.1f}x")
    elif key == ord('s'):  # уменьшить
        zoom = max(zoom - 0.1, 1.0)
        print(f"Масштаб: {zoom:.1f}x")
    elif key == ord('p'):  # скриншот
        filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        cv2.imwrite(filename, zoomed_frame)
        print(f"Скриншот сохранён: {filename}")

cap.release()
out.release()
cv2.destroyAllWindows()
