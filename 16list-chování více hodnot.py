# List - chování více hodnot
employees = ["David", "Harry", "Ron"]
print(employees[0])
print(employees[1])
print(employees[2])

# Mění položku
employees[1] = "Hermiona"
print(employees)

# Přidáváme obsah
employees.append("Harry")
print(employees)

# Přidáváme více položek
employees.extend(["Crabbe, Goyle"])
print(employees)

# Odstraňujeme položku
employees.remove("Ron")
print(employees)
