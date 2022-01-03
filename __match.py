from dataclasses import dataclass


def Age(age):
    match age:
        case 18:
            print("Your are acceptable")
        case _:
            print("Not acceptable")


Age(18)


@dataclass
class Animal():
    name: str
    age: int


def Type(animal):
    match animal:
        case Animal(age=age) if age >= 5:
            print("Acceptable")
        case Animal():
            print("Too young")
        case _:
            raise ValueError("No acceptable")


# Type(Animal("Dog", 3))
Type(Dog())


def Which(first_number, second_number):

    match(fist_number, second_number):
        case(2, 0):
            print("second,zero")
        case _:
            print("none")


Which(2, 0)
