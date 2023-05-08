# Funkce s více parametry
def greet(name, location):
    print(f"Ahoj, já jsem {name} a pocházím z města {location}")


# Positional Argument
greet("Honza", "Jihlava")

# keyword arguments
greet(location="Tábor", name="Martina")
