#week 4-6
data = []
user_id = set()
summa = 0
num_purchases = 0
with open ("shop_logs.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        parts = line.split(";")

        date = parts[0]
        user = parts[1]
        action = parts[2]

        amount = None
        if len(parts) == 4:
            amount = int(parts[3])
            summa += amount
            num_purchases += 1


        data.append({
            "date": date,
            "user": user,
            "action": action,
            "amount": amount
        })
        user_id.add(user)

with open ("data", "w") as w:
    w.write ("User id:" + ", ".join(user_id) + "\n")
    w.write ("Total purchases:" + str(summa) + "\n")
    w.write ("num_purchases: " + str(num_purchases) + "\n")
    w.write ("\n")
