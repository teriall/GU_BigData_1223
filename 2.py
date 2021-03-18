# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.
line_counter = 0
words = 0
with open('2.txt', 'r') as doc:
    for line in doc:
        line_counter += 1
        for i in str.split(line):
            words += 1
print(f'File {doc.name} contain {line_counter} lines and {words} words')
