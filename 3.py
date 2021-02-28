# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input('Пожалуйста, введите число: ')
two_numbers = (number + number)
three_numbers = (number + number + number)

print('Сумма чисел n + nn + nnn:', int(number) + int(two_numbers) + int(three_numbers))