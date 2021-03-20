# 4.	Реализуйте базовый класс Car.
#
# ●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# ●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# ●	для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, model, is_police):
        self.speed = speed
        self.color = color
        self.model = model
        self.is_police = is_police

    def show_speed(self):
        return f'speed: {self.speed}'

    def go(self):
        return 'start moving'

    def stop(self):
        return 'stop moving'

    def turning_right(self):
        return 'turning right'

    def turning_left(self):
        return 'turning left'


class TownCar(Car):
    def __init__(self, speed, color, model, is_police):
        super().__init__(speed, color, model, is_police)

    def speed_limit(self):
        if self.speed > 60:
            return 'Speed limit is 60'


class SportCar(Car):
    def __init__(self, speed, color, model, is_police):
        super().__init__(speed, color, model, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, model, is_police):
        super().__init__(speed, color, model, is_police)

    def speed_limit(self):
        if self.speed > 40:
            return 'speed limit is 40'


class PoliceCar(Car):
    def __init__(self, speed, color, model, is_police):
        super().__init__(speed, color, model, is_police)

    def police(self):
        if self.is_police:
            return f'{self.model} is police car'



tesla = TownCar(230, 'Green', 'Tesla', False)
wv = WorkCar(120, 'Yellow', 'WV Beetle', False)
gtr = SportCar(300, 'White', 'Nissan GTR', False)
audi = PoliceCar(200, 'Black', 'Audi A8', True)

print(f'{tesla.model} {tesla.go()}')
print(f'{wv.model} {wv.turning_right()}')
print(f'{gtr.model} {gtr.show_speed()}')
print(f'{wv.model} {wv.speed_limit()}')
print(f'{tesla.model} {tesla.speed_limit()}')
print(f'{audi.model} is police car? {audi.is_police}')
print(f'{gtr.model} is police car? {gtr.is_police}')