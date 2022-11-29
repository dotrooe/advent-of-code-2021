class Person:
    name: str
    surname: str = "UNKNOWN"
    age: int

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f'{self.name} {self.surname}, age: {self.age}'

    def print(self):
        print(self)

    def getOlder(self, years: int):
        self.age += years


def main():
    maciek = Person("Maciek", "Jakis", 23)
    antek = Person("Antek", "Drugi", 19)

    print(maciek)
    print(antek)

    maciek.getOlder(10)
    antek.getOlder(20)

    maciek.print()
    antek.print()


if __name__ == '__main__':
    main()
