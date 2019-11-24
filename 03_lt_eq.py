"""
Ukázka implementace reprezentace vyplnění dunder metody __repr__()

Funguje to obdobně jako u __repr__()

Dunder metody jsou volány při porovnávání instancí příslušnými operátory
__eq__() ==
__ne__() !=
__gt__() >
__lt__() <
__ge__() >=
__le__() <=

V příkladu jsou některé zakomentované. Je to z důvodu, že ve skutečnosti všechny nejsou třeba.
Python si dokáže odvodit opačnou funkci. Např. z __eq__ si odvodí __ne__
"""

class Person:
    def __init__(self, name, surname, age, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height

    def __repr__(self):
        return f"class: {self.__class__.__name__}," \
               f" name: {self.name}, surname: {self.surname}, age: {self.age}, height: {self.height}"

    def __eq__(self, other):
        return (self.name, self.surname, self.age, self.height) == \
                (other.name, other.surname, other.age, other.height)

    def __lt__(self, other):
        return ((self.name, self.surname, self.age, self.height) <
                (other.name, other.surname, other.age, other.height))

    def __ge__(self, other):
        return ((self.name, self.surname, self.age, self.height) >=
                (other.name, other.surname, other.age, other.height))

    # def __ne__(self, other):
    #     return (self.name, self.surname, self.age, self.height) != \
    #             (other.name, other.surname, other.age, other.height)

    # def __le__(self, other):
    #     return ((self.name, self.surname, self.age, self.height) <=
    #             (other.name, other.surname, other.age, other.height))

    # def __gt__(self, other):
    #     return ((self.name, self.surname, self.age, self.height) >
    #             (other.name, other.surname, other.age, other.height))


john = Person("John", "Doe", 66, 180)
john_copy = Person("John", "Doe", 66, 180)
great_zohn = Person("Zohn", "Zow", 666, 1800)

print(f"{john}\n{john_copy}\njohn == john_copy: {john == john_copy}\n")
print(f"{john}\n{great_zohn}\njohn == great_zohn: {john == great_zohn}\n")
print(f"{john}\n{great_zohn}\njohn < great_zohn: {john < great_zohn}\n")





