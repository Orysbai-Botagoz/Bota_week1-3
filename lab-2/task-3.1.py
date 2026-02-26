import json


total_sum = 0
total_count = 0
user_count = {}
items_counts = {}
orders_num = 0
top_user_total = {}
with open("orders.json", "r") as f:
    reader = json.load(f)
    for order in reader:
        user = order["user"]
        items = order["items"]
        total = order["total"]
        total_sum += total
        if user not in user_count:
            user_count[user] = 1
            orders_num += 1
        else:
            user_count[user] += 1
        for item in items:
            if item not in items_counts:
                items_counts[item] = 1
            else:
                items_counts[item] += 1
        max_item = max(items_counts, key=items_counts.get)
        if user not in top_user_total:
            top_user_total[user] = total
        else:
            top_user_total[user] += total
        top_user = max(top_user_total, key=top_user_total.get)



data = {
    "total_revenue": total_sum,
    "most_popular_item": max_item,
    "total_orders": orders_num,
    "top_user": top_user,


}

with open("summary-1.json", "w") as f_out:
    json.dump(data, f_out, indent=4)




