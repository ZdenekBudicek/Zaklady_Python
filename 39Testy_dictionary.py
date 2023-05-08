students_results = {
    "Harry": 85,
    "Ron": 71,
    "Hermione": 98,
    "Draco": 69
}
description_result = {}

for key in students_results:
    score = students_results[key]
    if 91 <= score <= 100:
        description_result[key] = "Excelentní"
    elif 81 <= score <= 90:
        description_result[key] = "Vynikající"
    elif 71 <= score <= 80:
        description_result[key] = "Splněno"
    else:
        description_result[key] = "Nesplněno"
print(description_result)
