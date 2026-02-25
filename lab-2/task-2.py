import csv
employees = []
dept_salaries = {}
with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        salary = int(row["salary"])
        row['salary'] = salary
        employees.append(row)
        dept = row['department']
        if dept not in dept_salaries:
            dept_salaries[dept] = []
        dept_salaries[dept].append(salary)
    all_salaries = [emp["salary"] for emp in employees]
    avg_salary = sum(all_salaries) / len(all_salaries)
    dept_averages = {}
    for dept, salaries in dept_salaries.items():
        avg = sum(salaries) / len(salaries)
        dept_averages[dept] = avg
    richest_employee = max(employees, key=lambda emp: emp["salary"])
    high_earners = [emp for emp in employees if emp["salary"] > avg_salary]

fieldnames = ['name', 'department', 'salary']
with open ("high_salary.csv", 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames) #fieldnames (справа) — это название вашей переменной
    writer.writeheader() #Без этого в файле сразу пошли бы данные без названий колонок.
    writer.writerows(high_earners)
