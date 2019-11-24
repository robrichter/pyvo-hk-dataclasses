"""
Ukázka parametru frozen - zajistí nám, že vytvořené instance již nepůjdou dále měnit.
"""

from dataclasses import dataclass



@dataclass
class HotJohn:
    name: str = "John"
    surname: str = "Doe"
    age: int = 66
    height: int = 180


@dataclass(frozen=True)
class FrozenJohn:
    name: str = "John"
    surname: str = "Doe"
    age: int = 66
    height: int = 180


hot_john = HotJohn()
frozen_john = FrozenJohn()

print(hot_john)
hot_john.height = 170
hot_john.surname = "Doh"
hot_john.weight = 80
print(hot_john)
print(hot_john.weight)

frozen_john.height = 80
frozen_john.weight = 80
