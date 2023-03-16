class Duck:
    size: float  # атрибут
    wings: List[wing]  # атрибут
    legs: List[legs]  # атрибут
    head: Head  # атрибут
    beak: Beak  # атрибут

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


BasilDuck = Duck()

BasilDuck.sing()
BasilDuck.eat("Bucket of beans")

print(BasilDuck.size)
