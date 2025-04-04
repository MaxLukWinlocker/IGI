from geometric_lib.circle import area as circle_area, perimeter as circle_perimeter
from geometric_lib.square import area as square_area, perimeter as square_perimeter  # ← Изменили здесь

radius = 5
side = 4  # Для квадрата нужна только одна сторона

print("=== Результаты ===")
print(f"Площадь круга: {circle_area(radius)}")
print(f"Длина окружности: {circle_perimeter(radius)}")
print(f"Площадь квадрата: {square_area(side)}")          # ← Изменили здесь
print(f"Периметр квадрата: {square_perimeter(side)}")    # ← Изменили здесь