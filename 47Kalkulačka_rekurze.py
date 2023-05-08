# Calculator
import os


def sum(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": sum,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("Jaké je první číslo?\n"))

    lets_continue = "ano"
    while lets_continue == "ano":
        for symbol in operations:
            print(symbol)

        user_symbol = input("Zvolte jednu z operací výše: ")
        num2 = float(input("Jaké je další číslo?\n"))

        calc_function = operations[user_symbol]
        result = calc_function(num1, num2)

        print(f"{num1} {user_symbol} {num2} = {result}")
        lets_continue = input(
            "Napište 'ANO' pokud chcete pokračovat s výsledkem, pokud chcete spustit kalkulátor znovu napište 'ZNOVU', pokud chcete kalkulátor vypnout napište 'VYP'.\n").lower()
        if lets_continue == "ano":
            num1 = result
        elif lets_continue == "znovu":
            os.system("cls")
            calculator()
        else:
            lets_continue == "VYP"
            os.system("cls")
            break


calculator()
