# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open('doc.txt', 'w') as doc:
    while True:
        line = input('Enter text: ')
        doc.writelines(line + '\n')
        if not line:
            break
