"""
Ukázka implementace reprezentace vyplnění dunder metody __repr__()

Ve chvíli, kdy se instance třídy Person dá "vypsat" funkcí print, zavolá se dunder metoda
__repr__(), která printu předá to, co jsme si nadefinovali.
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


person = Person("John", "Doe", 66, 180)
print(person)

