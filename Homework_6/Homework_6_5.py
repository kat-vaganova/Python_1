# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}.")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}.")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title}.")


st = Stationery("")
st.draw()

pen = Pen("Ручкой")
pen.draw()

pencil = Pencil("Карандашом")
pencil.draw()

st_handle = Handle("Маркером")
st_handle.draw()
