# 5.	Реализовать класс Stationery (канцелярская принадлежность).
#
# ●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# ●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ●	в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное
# сообщение;
# ●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'start drawing'


class Pen(Stationery):
    def __init__(self, title):
        super(Pen, self).__init__(title)

    def draw(self):
        return 'Pen is drawing now'


class Pencil(Stationery):
    def __init__(self, title):
        super(Pencil, self).__init__(title)

    def draw(self):
        return 'Pencil is drawing now'


class Marker(Stationery):
    def __init__(self, title):
        super(Marker, self).__init__(title)

    def draw(self):
        return 'Marker is drawing now'


pen = Pen('Blue')
pencil = Pencil('Hard')
marker = Marker('Black')

print(f'{pen.title} {pen.draw()}')
print(f'{pencil.title} {pencil.draw()}')
print(f'{marker.title} {marker.draw()}')