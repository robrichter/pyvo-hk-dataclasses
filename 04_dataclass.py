"""
Doteď by nám příklady fungovaly i na starším Pythonu. Nyní je již třeba minimálně verze 3.7.

Příklad ukazuje sílu datových tříd, kdy nemusíme implementovat žádné dunder metody pro inicializaci,
reprezentaci ani porovnání, vše je za nás vytvořeno.
"""

from dataclasses import dataclass

"""
Datová třída se vytváří použitím dekorátoru @dataclass (v tomto konkrétním příkladu s parametrem
order=True). Dekorátor jsme si naimportovali z modulu dataclassses, který je součástí interpretu,
viz. výše.

name:str Toto je tzv. typová anotace, která Pythonu řekne, o jaký datový typ se jedná (v tomto 
konkrétním případě o řetězec). Tuto informaci potřebuje pro potřeby porovnávání.
"""
@dataclass(order=True)
class Person:
    name: str
    surname: str
    age: int
    height: int


john = Person("John", "Doe", 66, 180)
john_copy = Person("John", "Doe", 66, 180)
great_zohn = Person("Zohn", "Zow", 666, 1800)

print(f"{john}\n{john_copy}\njohn == john_copy: {john == john_copy}\n")
print(f"{john}\n{great_zohn}\njohn == great_zohn: {john == great_zohn}\n")
print(f"{john}\n{great_zohn}\njohn < gret_zohn: {john < great_zohn}\n")