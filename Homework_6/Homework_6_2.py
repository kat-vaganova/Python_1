# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
#
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    _length: int = 5000
    _width: int = 20

    def __int__(self, width, length):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width


cl_road = Road()


class Raschet:
    weight: int = 25
    thickness: int = 5

    def mass(self, weight, thickness):
        self.weight = weight
        self.thickness = thickness

    def result(self):
        return self.thickness * self.weight * cl_road.area() / 1000


cl_raschet = Raschet()
print(f"Масса необходимого асфальта: {cl_raschet.result()} тонн")
