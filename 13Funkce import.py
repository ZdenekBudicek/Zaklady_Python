import random
import math

# Generování náhodného celého čísla z rozshau
print(random.randint(10, 18))

# Generování náhodného desetiného čísla mezi 0 a 1
print(random.random())

# Generování náhodného čísla z rozmezí + krok(po kolika to má jít)
print(random.randrange(15, 25, 2))

# Zaokrouhluje nahorů a dolů
print(math.ceil(5.1))
print(math.floor(5.1))
