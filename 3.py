# 3.	Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

min_salary = 13000
min_salary_list = []
salary_list = []
with open('3.txt', 'r', encoding='UTF8') as doc:
    my_list = doc.read().split('\n')
    for el in my_list:
        if int(el.split()[1]) < min_salary:
            min_salary_list.append(el.split()[0])
        salary_list.append(el.split()[1])
print(f'Average salary is: {sum(map(int, salary_list)) / len(salary_list):.0f} \nPoor workers list: {min_salary_list}')
