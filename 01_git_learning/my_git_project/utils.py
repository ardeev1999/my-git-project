#!/usr/bin/env python3
"""
Вспомогательные функции
"""

def show_system_info():
    """Показать информацию о системе"""
    import platform
    import sys
    
    print("\n🖥️  ИНФОРМАЦИЯ О СИСТЕМЕ:")
    print(f"  ОС: {platform.system()} {platform.release()}")
    print(f"  Python: {sys.version.split()[0]}")
    print(f"  Архитектура: {platform.architecture()[0]}")

def calculate(a, b):
    """Простой калькулятор"""
    print(f"\n🧮 КАЛЬКУЛЯТОР:")
    print(f"  {a} + {b} = {a + b}")
    print(f"  {a} - {b} = {a - b}")
    print(f"  {a} * {b} = {a * b}")
    if b != 0:
        print(f"  {a} / {b} = {a / b:.2f}")
    else:
        print("  Деление на ноль!")

if __name__ == "__main__":
    show_system_info()
    calculate(10, 2)
