"""
Tento příklad ukazuje, jak datové třídy podrobněji nastavovat. V předchozích příkladech
nám do porovnávání či reprezentace vstupovali veškeré atributy třídy. Tady si ukážeme, jak můžeme
některé vynechat, nebo jak nastavit implicitní hodnoty.
"""

from dataclasses import dataclass, field


@dataclass(order=True)
class Person:
    name: str = field(compare=False, default="John")
    surname: str = field(compare=False, default="Dow")
    age: int = field(repr=False, default=66)
    height: int = field(compare=False, repr=False, default=180)


john = Person()
john_bad_copy = Person(surname="Doh")
great_zohn = Person("Zohn", "Zow", 10, 1800)

print(f"{john}\n{john_bad_copy}\njohn == john_bad_copy: {john == john_bad_copy}\n")
print(f"{john}\n{great_zohn}\njohn == great_zohn: {john == great_zohn}\n")
print(f"{john}\n{great_zohn}\njohn < great_zohn: {john < great_zohn}\n")


