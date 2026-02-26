import csv
import json

user_counts = {}
suspicious_amount = []
total_fraud_sum = 0
suspicious_user = set()


with open("transactions.csv", 'r', encoding="utf-8") as f_in:
    reader = csv.DictReader(f_in)
    for row in reader:
        user = row["user_id"]
        amount = int(row["amount"])
        if user not in user_counts:
            user_counts[user] = 1
        else:
            user_counts[user] += 1
        if amount > 500000:
            suspicious_amount.append(amount)
            total_fraud_sum += amount

    for user, count in user_counts.items():
        if count > 3:
            suspicious_user.add(user)
    data = {
        "suspicious_user": list(suspicious_user)
    }
user_strings = ",".join(suspicious_user)
with open ("fraud_report.txt", "w", encoding="utf-8") as f_out:
    f_out.write(f"Подозрительных транзакций: {len(suspicious_amount)}\n")
    f_out.write(f"Подозрительных пользователей: {len(suspicious_user)}\n")
    f_out.write((f"Список пользователей: {user_strings}\n"))
    f_out.write(f"Общая сумма подозрительных операций: {total_fraud_sum}")


with open ("fraud_users.json", "w", encoding="utf-8") as f_out:
    json.dump(data, f_out, indent=4, ensure_ascii=False)


