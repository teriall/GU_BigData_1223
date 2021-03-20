# 3.	Реализовать базовый класс Worker (работник).
#
# ●	определить атрибуты: name, surname, position (должность), income (доход);
# ●	последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus};
# ●	создать класс Position (должность) на базе класса Worker;
# ●	в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом
# премии (get_total_income);
# ●	проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, _wage, _bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'wage': _wage, 'bonus': _bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}, {self.position}'

    def get_full_income(self):
        return f'Full income is: {self.income.get("wage") + self.income.get("bonus")}'


a = Position('Vasili', 'Pupkin', 'Python programmer', 100000, 25000)
print(a.get_full_name())
print(a.get_full_income())
