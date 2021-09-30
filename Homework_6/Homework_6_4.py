# 4.Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    speed: int
    color: str
    name: str
    is_police: bool
    side: str = ['left', 'right', 'return']

    def __init__(self, name, color, speed, is_police, side):
        self.speed = speed
        self.color = color
        self.name = name
        self.side = side
        self.is_police = is_police

    def go(self):  # поехала
        if self.speed > 0:
            print(f'Автомобиль {self.name} в движении')

    def stop(self):  # остановилась
        if self.speed == 0:
            print(f'Автомобиль {self.name} в остановлен')

    def turn(self):  # повернула
        if self.side == "right":
            print(f'Автомобиль {self.name} повернул направо')
        elif self.side == "left":
            print(f'Автомобиль {self.name} повернул налево')
        elif self.side == "return":
            print(f'Автомобиль {self.name} повернул развернулся')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} ({self.color}) составляет {self.speed} км/ч.')


class TownCar(Car):
    long: float  # длинна
    fuel_rate: float  # норма расхода топлива

    def __init__(self, name, color, speed, is_police, side, long, fuel_rate):
        super().__init__(name, color, speed, is_police, side)
        self.long = long
        self.fuel_rate = fuel_rate

    def max_speed(self):
        if self.speed > 60:
            print(f'Автомобиль {self.name} ({self.color}) превысил допустимую скорость! '
                  f'Скорость его движения {self.speed} км/ч.')


# town_car = TownCar(70, "blue", "audi", "left", False, 2.3, 10)
# town_car.max_speed()


class SportCar(Car):
    maxim_speed: int

    def __init__(self, name, color, speed, is_police, side, maxim_speed):
        super().__init__(name, color, speed, is_police, side)
        self.maxim_speed = maxim_speed

    def max_speed(self):
        print(f'Максимально возможная скорость спортивного автомобиля {self.name} - {self.maxim_speed} км/ч!')


# town_car = SportCar(70, "blue", "audi", "left", False, 100)
# town_car.max_speed()


class WorkCar(Car):
    carrying: int   # грузородъемность

    def __init__(self, name, color, speed, is_police, side, carrying):
        super().__init__(name, color, speed, is_police, side,)
        self.carrying = carrying

    def max_speed(self):
        if self.speed > 40:
            print(f'Автомобиль {self.name} (грузоподъемность: {self.carrying} т.) превысил допустимую скорость! '
                  f'Скорость его движения {self.speed} км/ч.')


class PoliceCar(Car):
    siren: bool

    def __init__(self, name, color, speed, is_police, side, siren):
        super().__init__(name, color, speed, is_police, side)
        self.siren = siren

    def info(self, class_object):
        if isinstance(class_object, PoliceCar):
            print(f"Автомобиль {self.name} принадлежит полиции")
        else:
            print(f"Автомобиль {self.name} НЕ принадлежит полиции")


# # printer = InfoPrinter()
# camry = PoliceCar(40, "blue", "camry", "left", True, True)
# camry.info(camry)
# camry.info(town_car)


car_obj = Car("Renault", "Black", 80, False, "left")
car_town = TownCar("Toyota", "White", 110, False, "right", 2.3, 12)
car_work = WorkCar("Volvo", "Brown", 55, False, "return", 8)
car_sport = SportCar("Ferrari", "Red", 220, False, "left", 360)
car_police = PoliceCar("Volkswagen", "Green", 0, True, "right", True)

car_obj.show_speed()
car_obj .go()
car_obj.turn()
car_obj.stop()

car_town.max_speed()
car_sport.max_speed()
car_work.max_speed()
car_police.info(car_police)
