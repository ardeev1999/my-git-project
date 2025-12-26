#!/usr/bin/env python3
"""
Git Learning - Исправленная версия для Windows PowerShell
Простой и понятный туториал
"""
import os
import subprocess
import sys
from datetime import datetime

def print_header(text):
    """Красивый заголовок"""
    print("\n" + "="*60)
    print(f"🎯 {text}")
    print("="*60)

def print_step(step, total, text):
    """Отображение шага"""
    print(f"\n📝 ШАГ {step}/{total}: {text}")
    print("-"*50)

def find_git_exe():
    """Найти git.exe на Windows"""
    possible_paths = [
        r"C:\Program Files\Git\bin\git.exe",
        r"C:\Program Files (x86)\Git\bin\git.exe",
        r"C:\Program Files\Git\cmd\git.exe",
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            print(f"✅ Найден Git: {path}")
            return path
    
    print("❌ Git не найден!")
    print("Проверьте установку Git или запустите команды вручную.")
    return None

def run_command(command, description, wait=True, use_git=False):
    """Запуск команды"""
    print(f"\n💻 {description}")
    print(f"   Команда: {command}")
    
    if wait:
        input("\n   Нажмите Enter для выполнения...")
    
    try:
        # Если это Git команда и мы нашли git.exe
        if use_git and command.startswith("git "):
            git_exe = find_git_exe()
            if not git_exe:
                return False
            
            # Заменяем git на полный путь
            command = command.replace("git ", f'"{git_exe}" ', 1)
        
        # Запускаем команду
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            encoding='utf-8',
            capture_output=True
        )
        
        if result.stdout:
            print(f"\n✅ Результат:\n{result.stdout[:500]}...")  # Ограничиваем вывод
        
        if result.stderr and "warning" not in result.stderr.lower():
            print(f"\n⚠️  Ошибки:\n{result.stderr[:500]}...")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Ошибка выполнения: {e}")
        return False

def manual_git_commands():
    """Ручные команды для выполнения в отдельном терминале"""
    print_header("КОМАНДЫ ДЛЯ РУЧНОГО ВЫПОЛНЕНИЯ")
    
    commands = [
        "git --version",
        "git config --list",
        "git init",
        "git status",
        "git add .",
        'git commit -m "Сообщение"',
        "git log --oneline",
        "git branch",
        "git checkout -b feature/new-feature",
    ]
    
    print("\n📋 Откройте НОВЫЙ терминал VS Code (Ctrl+Shift+`)")
    print("   и выполните эти команды по порядку:\n")
    
    for i, cmd in enumerate(commands, 1):
        print(f"{i:2}. {cmd}")
    
    print("\n💡 Совет: Копируйте команды и вставляйте в терминал (Ctrl+V)")

def interactive_tutorial():
    """Интерактивный туториал"""
    print_header("ИНТЕРАКТИВНОЕ ОБУЧЕНИЕ GIT")
    
    project_name = "my_first_git_project"
    
    # Шаг 1: Создание проекта
    print_step(1, 5, "СОЗДАНИЕ ПРОЕКТА")
    
    if os.path.exists(project_name):
        print(f"📁 Папка '{project_name}' уже существует.")
        choice = input("   Удалить и создать заново? (y/n): ")
        if choice.lower() == 'y':
            import shutil
            shutil.rmtree(project_name)
        else:
            project_name = input("   Введите новое имя проекта: ")
    
    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)
    
    print(f"📂 Рабочая папка: {os.getcwd()}")
    
    # Шаг 2: Создание файлов
    print_step(2, 5, "СОЗДАНИЕ ФАЙЛОВ")
    
    # README
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(f"""# {project_name}

Мой первый Git проект.

## Описание
Проект создан для изучения Git.

## Автор
Вячеслав Ардеев
ardeev1999@gmail.com

## Дата создания
{datetime.now().strftime('%Y-%m-%d %H:%M')}
""")
    print("✅ Создан README.md")
    
    # Python файл
    with open("main.py", "w", encoding="utf-8") as f:
        f.write('''#!/usr/bin/env python3
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
''')
    print("✅ Создан main.py")
    
    # Показываем файлы
    print("\n📄 Файлы в проекте:")
    run_command("dir", "Список файлов", wait=False)
    
    # Шаг 3: Инициализация Git
    print_step(3, 5, "ИНИЦИАЛИЗАЦИЯ GIT")
    
    print("\n🐙 Теперь инициализируем Git репозиторий:")
    print("   Откройте новый терминал (Ctrl+Shift+`) и выполните:")
    print("\n   1. git init")
    print("   2. git status")
    print("   3. git add .")
    print('   4. git commit -m "Initial commit"')
    
    input("\n   Нажмите Enter когда выполните эти команды...")
    
    # Шаг 4: Работа с Git
    print_step(4, 5, "РАБОТА С GIT")
    
    print("\n📊 Проверим что получилось:")
    run_command("git log --oneline", "История коммитов", wait=False, use_git=True)
    
    # Создаем еще файл
    with open("utils.py", "w", encoding="utf-8") as f:
        f.write('''#!/usr/bin/env python3
"""Вспомогательные функции"""

def greet(name):
    """Приветствие"""
    return f"Привет, {name}!"

def print_info():
    """Информация о проекте"""
    print("Проект: Мой первый Git проект")
    print("Автор: Вячеслав Ардеев")

if __name__ == "__main__":
    print_info()
''')
    
    print("\n✅ Добавлен новый файл utils.py")
    
    print("\n📝 Выполните в терминале:")
    print("   1. git status (увидите новый файл)")
    print("   2. git add utils.py")
    print('   3. git commit -m "Добавлен модуль утилит"')
    print("   4. git log --oneline (увидите 2 коммита)")
    
    input("\n   Нажмите Enter когда выполните...")
    
    # Шаг 5: Итоги
    print_step(5, 5, "ИТОГИ ОБУЧЕНИЯ")
    
    print("\n🎉 ОТЛИЧНО! ВЫ ИЗУЧИЛИ ОСНОВЫ GIT!")
    
    print(f"""
📊 РЕЗУЛЬТАТЫ:
• Создан проект: {project_name}
• Созданы файлы: 3
• Выполнены коммиты: 2
• Рабочая папка: {os.getcwd()}

📚 ИЗУЧЕННЫЕ КОМАНДЫ:
1. git init - создание репозитория
2. git status - проверка состояния
3. git add - добавление файлов
4. git commit - фиксация изменений
5. git log - история коммитов

🚀 СЛЕДУЮЩИЕ ШАГИ:
1. Создайте аккаунт на GitHub
2. Выполните: git remote add origin <ваш-репозиторий>
3. Выполните: git push -u origin main
4. Переходите к изучению Django!

💡 СОВЕТ:
• Всегда делайте git status перед коммитом
• Пишите понятные сообщения коммитов
• Используйте ветки для новых функций
""")
    
    # Запускаем наш проект
    print("\n🧪 ЗАПУСК ПРОЕКТА:")
    run_command("python main.py", "Запуск Python скрипта", wait=False)

def main():
    """Главная функция"""
    print("\n" + "="*70)
    print("🐙 GIT LEARNING - ПРАКТИЧЕСКИЙ КУРС ДЛЯ НАЧИНАЮЩИХ")
    print("="*70)
    
    print("\n👋 Привет, Вячеслав!")
    print("Выберите вариант обучения:\n")
    print("1. 🎯 Автоматический туториал (попробуем исправленный скрипт)")
    print("2. 🖐️  Ручной режим (вы выполняете команды сами)")
    print("3. 📚 Интерактивный туториал (рекомендуется)")
    
    choice = input("\nВаш выбор (1/2/3): ").strip()
    
    if choice == "1":
        # Проверяем Git
        print_header("ПРОВЕРКА GIT")
        if not find_git_exe():
            print("❌ Переключаемся на ручной режим...")
            manual_git_commands()
            return
        
        # Запускаем автоматические команды
        run_command("git --version", "Версия Git", wait=False, use_git=True)
        run_command("git config user.name", "Имя пользователя", wait=False, use_git=True)
        run_command("git config user.email", "Email", wait=False, use_git=True)
        
        print("\n✅ Git настроен корректно!")
        print("\n🎯 Теперь можете создать проект вручную или продолжить обучение.")
        
    elif choice == "2":
        manual_git_commands()
        
    elif choice == "3":
        interactive_tutorial()
        
    else:
        print("❌ Неверный выбор. Запускаю интерактивный режим...")
        interactive_tutorial()
    
    print("\n" + "="*70)
    print("✅ ОБУЧЕНИЕ ЗАВЕРШЕНО!")
    print("="*70)
    
    input("\nНажмите Enter для выхода...")

if __name__ == "__main__":
    main()