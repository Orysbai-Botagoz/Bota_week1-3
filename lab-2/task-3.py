import json

total_revenue = 0
total_items_count = 0
user_orders_count = {}
all_items_list = []
item_counts = {}
max_order_sum = 0
top_user = ''
with open ("orders.json", 'r', encoding="utf-8") as f:
    orders = json.load(f) #сразу бөліп береді лист инт и тд без этого просто текст было бы
    for order in orders:
        user = order["user"]
        total = order["total"]
        items = order["items"]
        total_revenue += total # 1. Считаем общую выручку
        if total > max_order_sum: # 2. Ищем самого щедрого покупателя
            max_order_sum = total
            top_user = user


        if user not in user_orders_count:
            user_orders_count[user] = 1

        else:
            user_orders_count[user] += 1

        all_items_list.extend(items) #бәрі бір листта тұру үшін, листтің ішінде лист болмау үшін

        for item in items:
            if item not in item_counts:
                item_counts[item] = 1
            else:
                item_counts[item] += 1
        max_item = max(item_counts, key=item_counts.get)

        summary_data = {
            "total_revenue": total_revenue,
            "top_user": top_user,
            "most_popular_item": max_item,
            "total_orders" : len(orders),
        }

with open ("summary.json", 'w', encoding="utf-8") as f_out:
    json.dump(summary_data, f_out, indent=4, ensure_ascii=False) # indent=4 сделает файл красивым и читаемым, Если поставить False, Python запишет кириллицу как она есть
