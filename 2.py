# Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_in_sec = int(input('Введите время в секундах: '))

print('%02d:%02d:%02d' % (time_in_sec // 3600, ((time_in_sec % 3600) // 60), ((time_in_sec % 3600) % 60)))
