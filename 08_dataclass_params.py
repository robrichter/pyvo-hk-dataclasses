"""
Ukázka všech parametrů, které můžeme při vytvoření datové třídy využít.
order - defaultně False, při zapnutí se implementuje metody __lt__, __gt__, __eg__, __el__
eq - defaultně True, při zapnutí implementuje metody __eq__, __ne__
init - defaultně True, implementuje __init__ metodu
repr - defaultně True, implementuje __repr__ metodu
frozen - defaultně False, při zapnutí nám nedovolí vytvořenou instanci měnit
unsafe_hash - Nebudeme vysvětlovat, protože se jedná o složitější koncept a není
pravděpodobné, že bychom jej opravdu potřebovali. Zjednodušeně řečeno, ovlivňuje zda bude
implementována dunder metoda __hash__.
Pozor, neovlivňuje to sám, ale vždy jde o kombinaci parametrů order, frozen, unsafe_hash.
"""

from dataclasses import dataclass, field


@dataclass(order=True, frozen=False, unsafe_hash=False, init=True, eq=True, repr=True)
class Person:
    name: str = field(compare=False, default="John")
    surname: str = field(compare=False, default="Doe")
    age: int = field(repr=False, default=66)
    height: int = field(compare=False, repr=False, default=180)


john = Person()
john_bad_copy = Person(surname="Doh")
great_zohn = Person("Zohn", "Zow", 10, 1800)

print(f"{john}\n{john_bad_copy}\njohn == john_bad_copy: {john == john_bad_copy}\n")
print(f"{john}\n{great_zohn}\njohn == great_zohn: {john == great_zohn}\n")
print(f"{john}\n{great_zohn}\njohn < great_zohn: {john < great_zohn}\n")
