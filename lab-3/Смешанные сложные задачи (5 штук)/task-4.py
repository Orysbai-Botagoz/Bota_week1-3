students = [("Иван", 85), ("Анна", 72), ("Пётр", 90), ("Мария", 60)]
names = {name: (lambda score: "Отлично" if point >= 90 else "Хорошо" if 70 <= point < 90 else "Удовлетворительно")(point) for name, point in students}
print(names)