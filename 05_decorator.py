"""
Ukázka vytvoření vlastního deokorátoru
"""

def world(function):
    def wrapper():
        return function() + "world!"
    return wrapper


def hi():
    return "Hi "

# Takhle by vypadalo použití dekorátoru v případě, že by neexistovala syntaxe s @ - viz. níže
decorated_hi = world(hi)
print(decorated_hi())

# Standardní použití námi vytvořeného dekorátoru
@world
def hello():
    return "Hello "


print(hello())
