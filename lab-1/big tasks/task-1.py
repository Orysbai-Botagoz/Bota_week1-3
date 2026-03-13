def block_1_filter_names(data): #1.	Фильтрация студентов по имени:
    clean_data = []
    for s in data:
        if all(not char.isdigit() for char in s["name"]): #удаляем всех студентов, у которых в имени есть цифры
            student = s.copy()
            student["name"] = s["name"].title()
            clean_data.append(student)
    return clean_data

def block_2_process_grades(students): #2.	Обработка оценок
    for s in students:
        new_grades = []
        for g in s["grades"]:
            if g <= 0:
                continue
            if g < 10 and g % 2 != 0:
                new_grades.append(sum(int(d) for d in str(g)))
            elif g >= 10 and g % 2 == 0:
                new_grades.append(g ** 2)
            else:
                new_grades.append(g)
        s["processed_grades"] = new_grades
    return students


import string

def block_3_analyze_comments(students): #3.	Анализ комментариев
    vowels_list = set("aeiou")
    all_vowels_found = set()
    for s in students:
        text = " ".join(s["comments"]).lower()
        text = text.translate(str.maketrans("", "", string.punctuation)) #("Что заменяем", "На что заменяем", Что нужно удалить), удаляем все знаки препинания
        words = text.split()
        valid_words = set()
        for w in words:
            if len(w) >= 4 and w != w[::-1]: #не являются палиндромами
                valid_words.add(w)
                for char in w:
                    if char in vowels_list: #множество гласных
                        all_vowels_found.add(char)
        s["temp_words"] = valid_words # сохраняем уникальные слова
    return students, all_vowels_found

def block_4_word_analysis(students): #4.	Глобальный анализ по всем студентам
    word_counts = {}
    for s in students:
        for word in s["temp_words"]:
            word_counts[word] = word_counts.get(word, 0) + 1 #если word нет то получается + 1
    filtered_words = {w: count for w, count in word_counts.items() if count >= 2}
    sorted_items = sorted(
        filtered_words.items(),
        key=lambda x: (-x[1], x[0]) # -x[1] для убывания, [0] По алфавиту
    )
    return dict(sorted_items)

def block_5_and_6_final(students, all_vowels_from_block3, word_counts): #5.	Сводные данные, 6.	Возвращаемое значение функции
    sorted_for_avg = sorted(
        students,
        key=lambda s: (
            -(sum(s["processed_grades"]) / len(s["processed_grades"])) if s["processed_grades"] else 0,
            s["name"]
        )
    )
    students_by_avg = [s["name"] for s in sorted_for_avg]
    names_by_len = {}
    for s in students:
        length = len(s["name"])
        if length not in names_by_len:
            names_by_len[length] = []
        if s["name"] not in names_by_len[length]:
            names_by_len[length].append(s["name"])
    return {
        "students": [{"name": s["name"], "processed_grades": s["processed_grades"]} for s in students],
        "all_vowels": all_vowels_from_block3,
        'students_by_avg': students_by_avg,
        "students_by_name_length": names_by_len,
    }
input_data = [
    {
        "name": "Alice",
        "grades": [2, 9, 15, -1, 0],
        "grades": [7, 9, 15],
        "grades": [4, 9, 15],
        "grades": [4, 9, 15],
        "comments": ["Good work!", "Excellent effort.", "Needs Improvement"]
    },
    {
        "name": "Bob",
        "grades": [5, 3],
        "comments": ["Very good.", "Not bad"]
    },
    {
        "name": "Charlie123",
        "grades": [10, 10, 10],
        "comments": ["I should not be here"]
    },
    {
        "name": "Eve",
        "grades": [10, 5],
        "comments": ["Good morning", "Python is great"]
    }
]
step1 = block_1_filter_names(input_data)
step2 = block_2_process_grades(step1)
step3, vowels = block_3_analyze_comments(step2)
word_counts = block_4_word_analysis(step3)
output_data = block_5_and_6_final(step3, vowels, word_counts)

import pprint
pprint.pprint(output_data, indent=4, sort_dicts=False)