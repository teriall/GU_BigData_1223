# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    mylist = [a, b, c]
    mylist.remove(min(a, b, c))
    return sum(mylist)


print(my_func(1, 2, 3))
