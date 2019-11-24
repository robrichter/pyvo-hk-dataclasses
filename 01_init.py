"""
Ukázka vytvoření objektu z běžné třídy
Pro inicializaci se využívá dunder (double underscore) metoda __init__()
Dunder metody nemá smysl ve většině případů volat přímo, ale jsou volány Python interpretem
při nějaké události. V případě metody __init__() je události vytvoření instance třídy Person
"""

# Třída Person
class Person:
    def __init__(self, name, surname, age, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height


# Vytvoření instance třídy Person
person = Person("John", "Doe", 66, 180)
print(person)
