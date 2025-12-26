#!/usr/bin/env python3
print("Привет, Git!")
print("Это мой первый проект под контролем версий")

def calculator(a, b):
    """Простой калькулятор"""
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    if b != 0:
        print(f"{a} / {b} = {a / b}")

if __name__ == "__main__":
    calculator(10, 2)
