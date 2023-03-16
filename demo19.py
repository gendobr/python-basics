class Bird:
    wingsLeft: wing  # атрибут
    wingsRight: wing  # атрибут
    head: Head  # атрибут
    beak: Beak  # атрибут
    legsLeft: legs  # атрибут
    legsRight: legs  # атрибут
    size: float  # атрибут
    name: str

    # конструктор
    def __init__(self) -> None:
        self.size = 10
        self.wings = [Wing(left, 30, 100), Wing(right, 30, 100)]
        self.head = Head()
        self.beak = Beak()

    # метод
    def sing(self):
        """"""

    # метод
    def eat(self, food):
        """"""

    # метод
    def drink(self, food):
        """"""


class SwimmingBird(Bird):
    # метод
    def swim(self):
        """"""


class FlyingBird(Bird):
    # метод
    def fly(self):
        """"""


class Duck(SwimmingBird, FlyingBird):
    def sing(self):
        print("Кряк")


bird1 = Duck()
bird1.sing()

birds = [Duck(), Duck(), SwimmingBird(), FlyingBird()]
for bird in birds:
    bird.sing()
