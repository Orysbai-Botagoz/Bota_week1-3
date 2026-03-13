def block_1_clean_customers(orders): #1.	Фильтрация заказов и клиентов
    clean_orders = []
    for o in orders:
        if all(not char.isdigit() for char in o["customer"]):
            order_copy = o.copy()
            order_copy["customer"] = o["customer"].title()
            clean_orders.append(order_copy)
    return clean_orders

def block_2_process_items(orders): #2.	Обработка товаров в заказах
    for o in orders:
        processed_items = []
        for item in o["items"]:
            if item["price"] <= 0: #удаляем товары с отрицательной или нулевой ценой
                continue
            new_item = item.copy()
            p = new_item["price"]
            q = new_item["quantity"]
            if p > 100 and q > 1:
                p = p * q
            if q % 2 != 0:
                price_digits_sum = sum(int(d) for d in str(int(p)) if d.isdigit())
                p += price_digits_sum

            new_item["price"] = p
            processed_items.append(new_item)
        o["processed_items"] = processed_items
    return orders

import string
def block_3_analyze_notes(orders): #3.	Анализ заметок к заказу
    vowels_set = set("aeiou")
    all_global_vowels = set()
    for o in orders:
        full_text = " ".join(o["notes"]).lower() #объединяем все заметки в одну строку, удаляя знаки препинания
        clean_text = full_text.translate(str.maketrans("", "", string.punctuation))
        words = clean_text.split()
        valid_words = set()
        for w in words:
            if len(w) >= 4 and w != w[::-1]: #создаём список уникальных слов длиной ≥4, без палиндромов
                valid_words.add(w)
                for char in w:
                    if char in vowels_set:
                        all_global_vowels.add(char)
        o["temp_words"] = valid_words
    return orders, all_global_vowels

def block_4_word_counts(orders): #4.	Глобальный анализ по всем заказам
    word_map = {}
    for o in orders:
        for word in o["temp_words"]:
            word_map[word] = word_map.get(word, 0) + 1 #создаём словарь слов {слово: количество заказов, в которых оно встречается}
    filtered = {w: c for w, c in word_map.items() if c >= 2} #оставляем только слова, встречающиеся хотя бы в 2 заказах
    sorted_words = dict(sorted(filtered.items(), key=lambda item: (-item[1], item[0]))) #сортируем словарь по убыванию числа заказов, при равенстве — по алфавиту
    return sorted_words

def block_5_summarize_products(orders): #5.	Сводные данные по товарам
    unique_products = set()
    order_totals = [] #(количество товаров, список order_id)
    item_count_map = {}
    for o in orders:
        current_total = 0
        current_items_names = set()
        for item in o["processed_items"]:
            unique_products.add(item["name"])
            current_items_names.add(item["name"])
            current_total += item["price"]
        order_totals.append({"id": o["order_id"], "total": current_total})
        qty = len(o["processed_items"])
        if qty not in item_count_map:
            item_count_map[qty] = []
        if o["order_id"] not in item_count_map[qty]:
            item_count_map[qty].append(o["order_id"])
    sorted_orders_by_total = sorted(
        order_totals,
        key=lambda x: (-x["total"], x["id"]) #создаём список студентов, отсортированный по средней обработанной оценке по убыванию, при равенстве — по имени
    )
    orders_by_total_ids = [x["id"] for x in sorted_orders_by_total]

    return unique_products, orders_by_total_ids, item_count_map

def analyze_orders(orders): #6.	Возвращаемое значение функции
    data = block_1_clean_customers(orders)
    data = block_2_process_items(data)
    data, all_vowels = block_3_analyze_notes(data)
    word_counts = block_4_word_counts(data)
    unique_products, orders_by_total, orders_by_item_count = block_5_summarize_products(data)
    final_orders = []
    for o in data:
        final_orders.append({
            "order_id": o["order_id"],
            "customer": o["customer"],
            "processed_items": o["processed_items"]
        })

    return {
        "orders": final_orders,
        "word_counts": word_counts,
        "all_vowels": all_vowels,
        "unique_products": unique_products,
        "orders_by_total": orders_by_total,
        "orders_by_item_count": orders_by_item_count
    }

input_orders = [
    {
        "order_id": "A123",
        "customer": "john_doe",
        "items": [
            {"name": "Laptop", "price": 1000.0, "quantity": 2},  # Цена > 100 и кол-во > 1: станет 2000
            {"name": "Mouse", "price": 25.5, "quantity": 1}     # Кол-во 1 (нечет): 25.5 + сумма цифр (2+5=7) = 32.5
        ],
        "notes": ["Deliver ASAP", "fragile package"] # Слова: deliver, asap, fragile, package
    },
    {
        "customer": "anna_smith",
        "order_id": "B456",
        "items": [
            {"name": "Monitor", "price": 150.0, "quantity": 1}, # Кол-во 1 (нечет): 150 + (1+5+0=6) = 156
            {"name": "Cable", "price": -5.0, "quantity": 1}      # Цена <= 0: удалится
        ],
        "notes": ["Handle with care", "ASAP please"] # Слова: handle, care, asap, please
    },
    {
        "customer": "mark_pro99", # Содержит цифры: ВЕСЬ заказ будет удален
        "order_id": "C789",
        "items": [{"name": "Phone", "price": 500.0, "quantity": 1}],
        "notes": ["Call me"]
    },
    {
        "customer": "elena",
        "order_id": "D001",
        "items": [
            {"name": "Laptop", "price": 1000.0, "quantity": 2}  # Станет 2000
        ],
        "notes": ["fragile", "Deliver tomorrow"] # Слова: fragile, deliver, tomorrow
    }
]

import pprint
pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)
result = analyze_orders(input_orders)
pp.pprint(result)





