unique_users = set ()
total_purchases = 0
total_sum = 0
user_spending = {}

with open("shop_logs.txt", "r") as file:
    for line in file:
        line = line.strip() # Убираем лишние пробелы и символы переноса строки
        if not line:
            continue
        parts = line.split(";") # Разрезаем строку по разделителю
        if len(parts) < 3:
            continue
        unique_users.add(parts[1])
        if parts[2] == "BUY":
            amount = int(parts[3])
            total_sum += amount
            total_purchases += 1
            if parts[1] not in user_spending:
                user_spending[parts[1]] = amount
            else:
                user_spending[parts[1]] += amount
    active_user = max(user_spending, key=user_spending.get)
    if total_purchases > 0:
        average_check = total_sum / total_purchases
    else:
        average_check = 0
with open("report.txt", "w") as file:
    file.write(f"Уникальных пользователей: {len(unique_users)}\n" )
    file.write(f"Всего покупок: {total_purchases}\n" )
    file.write(f"Общая сумма: {total_sum}\n")
    file.write(f"Самый активный покупатель: {active_user}\n")
    file.write(f"Средний чек: {average_check}\n")