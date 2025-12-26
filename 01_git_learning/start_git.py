#!/usr/bin/env python3
"""
ОБУЧАЮЩИЙ СКРИПТ ДЛЯ GIT - Практическое руководство (PowerShell версия)
Автор: Вячеслав Ардеев
"""
import os
import subprocess
import sys
import time
from datetime import datetime

class GitLearning:
    """Класс для интерактивного обучения Git (PowerShell версия)"""
    
    def __init__(self):
        self.project_name = "my_learning_project"
        self.steps_completed = 0
        self.total_steps = 10
        
    def print_header(self, title):
        """Печать заголовка"""
        print("\n" + "="*70)
        print(f"🎯 {title}")
        print("="*70)
    
    def print_step(self, step_num, description):
        """Печать шага"""
        print(f"\n📝 ШАГ {step_num}/{self.total_steps}: {description}")
        print("-"*50)
    
    def run_command(self, command, description, wait_for_user=True, shell_type="powershell"):
        """Запуск команды с описанием"""
        print(f"\n💻 {description}")
        print(f"   Команда: {command}")
        
        if wait_for_user:
            input("\n   Нажмите Enter для выполнения...")
        
        try:
            # Для Git команд используем cmd, для остальных - PowerShell
            if command.startswith("git "):
                # Git команды запускаем через cmd
                result = subprocess.run(
                    command, 
                    shell=True, 
                    text=True, 
                    encoding='utf-8',
                    capture_output=True,
                    executable="cmd.exe"  # Явно указываем cmd для Git команд
                )
            else:
                # Остальные команды через PowerShell
                result = subprocess.run(
                    command, 
                    shell=True, 
                    text=True, 
                    encoding='utf-8',
                    capture_output=True
                )
            
            if result.stdout:
                print(f"\n✅ Результат:\n{result.stdout}")
            
            if result.stderr and "warning" not in result.stderr.lower():
                print(f"\n⚠️  Предупреждения:\n{result.stderr}")
            
            self.steps_completed += 1
            return True
            
        except Exception as e:
            print(f"\n❌ Ошибка: {e}")
            return False
    
    def create_file(self, filename, content):
        """Создание файла с содержимым"""
        print(f"\n📄 Создаю файл: {filename}")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Файл {filename} создан")
        return True
    
    def check_git_installation(self):
        """Проверка установки Git"""
        self.print_header("ПРОВЕРКА УСТАНОВКИ GIT")
        
        print("🔍 Проверяю вашу настройку Git...")
        
        # Проверяем версию Git
        self.run_command("git --version", "Проверка версии Git", wait_for_user=False)
        
        # Проверяем настройки пользователя
        print("\n👤 Проверяю настройки пользователя...")
        self.run_command("git config user.name", "Ваше имя в Git", wait_for_user=False)
        self.run_command("git config user.email", "Ваш email в Git", wait_for_user=False)
        
        print("\n✅ Git настроен корректно!")
        return True
    
    def step_1_create_repository(self):
        """Шаг 1: Создание репозитория"""
        self.print_step(1, "СОЗДАНИЕ ПЕРВОГО GIT РЕПОЗИТОРИЯ")
        
        # Создаем папку проекта
        if os.path.exists(self.project_name):
            print(f"📁 Папка '{self.project_name}' уже существует.")
            choice = input("   Использовать существующую? (y/n): ")
            if choice.lower() != 'y':
                self.project_name = input("   Введите новое имя проекта: ")
        
        os.makedirs(self.project_name, exist_ok=True)
        os.chdir(self.project_name)
        
        print(f"📁 Рабочая директория: {os.getcwd()}")
        
        # Инициализируем Git
        self.run_command("git init", "Инициализация Git репозитория")
        
        # Показываем скрытую папку .git
        print("\n📂 Создана скрытая папка .git/")
        if os.path.exists(".git"):
            print("   Содержимое папки .git/:")
            # Используем PowerShell команду для показа скрытых файлов
            self.run_command("dir -Force", "Показать все файлы (включая скрытые)", wait_for_user=False)
        
        return True
    
    def step_2_create_first_files(self):
        """Шаг 2: Создание первых файлов"""
        self.print_step(2, "СОЗДАНИЕ ПЕРВЫХ ФАЙЛОВ ПРОЕКТА")
        
        # Создаем README.md
        readme_content = """# Мой первый Git проект

Этот проект создан в процессе обучения Git.

## Описание проекта:
Проект предназначен для изучения системы контроля версий Git.

## Цели обучения:
1. Освоить основные команды Git
2. Научиться работать с ветками
3. Понять процесс слияния изменений
4. Научиться отменять изменения

## Технологии:
- Python 3.9+
- Git 2.52.0+
- VS Code

## Автор:
Вячеслав Ардеев
ardeev1999@gmail.com

---

*Создано: {date}*
""".format(date=datetime.now().strftime("%Y-%m-%d %H:%M"))
        
        self.create_file("README.md", readme_content)
        
        # Создаем первый Python скрипт
        python_content = '''#!/usr/bin/env python3
"""
Главный файл проекта - приветствие
"""

import datetime

def show_greeting():
    """Показать приветствие"""
    print("="*50)
    print("ПРИВЕТСТВИЕ ОТ ПЕРВОГО GIT ПРОЕКТА!")
    print("="*50)
    
    name = "Вячеслав Ардеев"
    email = "ardeev1999@gmail.com"
    
    print(f"\\n👤 Автор: {name}")
    print(f"📧 Email: {email}")
    print(f"📅 Дата: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\\n🎯 Цель проекта: Изучение Git на практике")
    print("\\n" + "="*50)

def show_menu():
    """Показать меню"""
    print("\\n📋 МЕНЮ ПРОЕКТА:")
    print("1. Показать информацию о проекте")
    print("2. Запустить калькулятор")
    print("3. Проверить систему")
    print("4. Выход")
    
    try:
        choice = input("\\nВыберите опцию (1-4): ")
        return int(choice)
    except ValueError:
        return 0

def run_calculator():
    """Запустить простой калькулятор"""
    print("\\n🧮 КАЛЬКУЛЯТОР")
    print("-"*30)
    
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        
        print(f"\\nРезультаты:")
        print(f"  {a} + {b} = {a + b}")
        print(f"  {a} - {b} = {a - b}")
        print(f"  {a} * {b} = {a * b}")
        if b != 0:
            print(f"  {a} / {b} = {a / b:.2f}")
        else:
            print("  Деление на ноль невозможно!")
            
    except ValueError:
        print("Ошибка: введите числа корректно!")

def check_system():
    """Проверка системы"""
    import platform
    import sys
    
    print("\\n🖥️  ИНФОРМАЦИЯ О СИСТЕМЕ:")
    print(f"  ОС: {platform.system()} {platform.release()}")
    print(f"  Python: {platform.python_version()}")
    print(f"  Процессор: {platform.processor()}")
    print(f"  Архитектура: {platform.architecture()[0]}")

if __name__ == "__main__":
    show_greeting()
    
    while True:
        choice = show_menu()
        
        if choice == 1:
            print("\\n📊 ИНФОРМАЦИЯ О ПРОЕКТЕ:")
            print("Название: Мой первый Git проект")
            print("Автор: Вячеслав Ардеев")
            print("Версия: 1.0.0")
            print("Дата создания: 2024")
            
        elif choice == 2:
            run_calculator()
            
        elif choice == 3:
            check_system()
            
        elif choice == 4:
            print("\\n👋 До свидания!")
            break
            
        else:
            print("\\n❌ Неверный выбор. Попробуйте снова.")
        
        input("\\nНажмите Enter для продолжения...")
'''
        
        self.create_file("main.py", python_content)
        
        print("\n📁 Созданные файлы:")
        # Используем PowerShell команду вместо ls -la
        self.run_command("dir", "Список файлов в проекте", wait_for_user=False)
        
        return True
    
    def step_3_first_commit(self):
        """Шаг 3: Первый коммит"""
        self.print_step(3, "ПЕРВЫЙ КОММИТ - ФИКСАЦИЯ ИЗМЕНЕНИЙ")
        
        print("\n📊 Текущий статус репозитория:")
        self.run_command("git status", "Проверка состояния файлов", wait_for_user=False)
        
        print("\n➕ Добавляем файлы в индекс Git (staging area):")
        self.run_command("git add README.md main.py", "Добавление файлов README.md и main.py")
        
        print("\n📊 Статус после добавления:")
        self.run_command("git status", "Проверка состояния", wait_for_user=False)
        
        print("\n💾 Создаем первый коммит:")
        self.run_command(
            'git commit -m "Initial commit: добавлены README.md и основной скрипт"',
            "Создание первого коммита с описанием"
        )
        
        print("\n📜 История коммитов:")
        self.run_command("git log --oneline", "Краткая история коммитов", wait_for_user=False)
        
        return True
    
    def step_4_modify_files(self):
        """Шаг 4: Модификация файлов"""
        self.print_step(4, "МОДИФИКАЦИЯ ФАЙЛОВ И ВТОРОЙ КОММИТ")
        
        print("\n✏️  Добавляем новую функцию в main.py...")
        
        # Читаем текущий файл
        with open("main.py", "r", encoding="utf-8") as f:
            content = f.read()
        
        # Добавляем новую функцию перед if __name__ == "__main__":
        new_function = '''
def show_git_info():
    """Показать информацию о Git"""
    import subprocess
    
    print("\\n🐙 ИНФОРМАЦИЯ О GIT:")
    try:
        # Получаем версию Git
        result = subprocess.run(["git", "--version"], capture_output=True, text=True)
        print(f"  Версия Git: {result.stdout.strip()}")
        
        # Получаем текущую ветку
        result = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True)
        print(f"  Текущая ветка: {result.stdout.strip()}")
        
        # Получаем количество коммитов
        result = subprocess.run(["git", "rev-list", "--count", "HEAD"], capture_output=True, text=True)
        print(f"  Количество коммитов: {result.stdout.strip()}")
        
    except Exception as e:
        print(f"  Ошибка получения информации: {e}")
'''
        
        # Вставляем новую функцию
        insert_point = content.find("if __name__ == \"__main__\":")
        new_content = content[:insert_point] + new_function + content[insert_point:]
        
        # Добавляем вызов функции в меню
        new_content = new_content.replace(
            'print("3. Проверить систему")',
            'print("3. Проверить систему")\n    print("5. Информация о Git")'
        ).replace(
            'elif choice == 4:',
            'elif choice == 4:\n            print("\\n👋 До свидания!")\n            break\n        \n        elif choice == 5:\n            show_git_info()'
        )
        
        # Записываем обратно
        with open("main.py", "w", encoding="utf-8") as f:
            f.write(new_content)
        
        print("✅ Добавлена функция show_git_info()")
        
        # Проверяем изменения
        print("\n🔍 Проверяем изменения:")
        self.run_command("git diff", "Показ изменений в файлах", wait_for_user=False)
        
        # Добавляем и коммитим
        self.run_command("git add main.py", "Добавление измененного файла в индекс")
        self.run_command("git status", "Проверка статуса", wait_for_user=False)
        self.run_command(
            'git commit -m "Добавлена функция show_git_info для отображения информации о Git"',
            "Второй коммит"
        )
        
        print("\n📜 Обновленная история:")
        self.run_command("git log --oneline", "История коммитов", wait_for_user=False)
        
        return True
    
    def step_5_working_with_branches(self):
        """Шаг 5: Работа с ветками"""
        self.print_step(5, "РАБОТА С ВЕТКАМИ В GIT")
        
        print("\n🌿 Создаем новую ветку для разработки функции:")
        self.run_command("git branch feature/calculator-enhancement", "Создание ветки feature/calculator-enhancement")
        
        print("\n🔄 Переключаемся на новую ветку:")
        self.run_command("git checkout feature/calculator-enhancement", "Переключение на ветку feature")
        
        print("\n📊 Текущие ветки:")
        self.run_command("git branch", "Список всех веток", wait_for_user=False)
        
        # Создаем новый файл с улучшенным калькулятором
        calculator_content = '''#!/usr/bin/env python3
"""
Улучшенный калькулятор - новая функция
"""

class AdvancedCalculator:
    """Класс расширенного калькулятора"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Сложение"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Вычитание"""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Умножение"""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Деление"""
        if b == 0:
            raise ValueError("Деление на ноль!")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, a, b):
        """Возведение в степень"""
        result = a ** b
        self.history.append(f"{a} ^ {b} = {result}")
        return result
    
    def show_history(self):
        """Показать историю вычислений"""
        print("\\n📊 ИСТОРИЯ ВЫЧИСЛЕНИЙ:")
        if not self.history:
            print("  История пуста")
        else:
            for i, operation in enumerate(self.history, 1):
                print(f"  {i}. {operation}")

def run_advanced_calculator():
    """Запуск улучшенного калькулятора"""
    print("\\n🧮 УЛУЧШЕННЫЙ КАЛЬКУЛЯТОР")
    print("="*40)
    
    calc = AdvancedCalculator()
    
    operations = {
        '1': ('Сложение', calc.add),
        '2': ('Вычитание', calc.subtract),
        '3': ('Умножение', calc.multiply),
        '4': ('Деление', calc.divide),
        '5': ('Степень', calc.power)
    }
    
    while True:
        print("\\nДоступные операции:")
        for key, (name, _) in operations.items():
            print(f"  {key}. {name}")
        print("  6. Показать историю")
        print("  7. Выход")
        
        choice = input("\\nВыберите операцию (1-7): ")
        
        if choice == '7':
            print("\\n👋 Выход из калькулятора")
            break
            
        elif choice == '6':
            calc.show_history()
            
        elif choice in operations:
            try:
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                
                operation_name, operation_func = operations[choice]
                result = operation_func(a, b)
                
                print(f"\\n✅ Результат {operation_name.lower()}: {result}")
                
            except ValueError as e:
                print(f"\\n❌ Ошибка: {e}")
            except Exception as e:
                print(f"\\n❌ Неожиданная ошибка: {e}")
        else:
            print("\\n❌ Неверный выбор. Попробуйте снова.")
        
        input("\\nНажмите Enter для продолжения...")

if __name__ == "__main__":
    run_advanced_calculator()
'''
        
        self.create_file("advanced_calculator.py", calculator_content)
        
        print("\n💾 Коммитим новую функцию в ветке:")
        self.run_command("git add advanced_calculator.py", "Добавление нового файла")
        self.run_command(
            'git commit -m "Добавлен улучшенный калькулятор в ветке feature"',
            "Коммит в ветке feature"
        )
        
        return True
    
    def step_6_merge_branch(self):
        """Шаг 6: Слияние веток"""
        self.print_step(6, "СЛИЯНИЕ ВЕТОК (MERGE)")
        
        print("\n⬅️  Возвращаемся в основную ветку:")
        self.run_command("git checkout main", "Переключение на ветку main")
        
        print("\n🔄 Сливаем изменения из ветки feature:")
        self.run_command("git merge feature/calculator-enhancement", "Слияние ветки feature в main")
        
        print("\n📊 История после слияния:")
        self.run_command("git log --oneline --graph --all", "Графическое представление истории", wait_for_user=False)
        
        print("\n📁 Проверяем файлы после слияния:")
        self.run_command("dir", "Список файлов", wait_for_user=False)
        
        return True
    
    def step_7_gitignore(self):
        """Шаг 7: Создание .gitignore"""
        self.print_step(7, "СОЗДАНИЕ .gitignore ФАЙЛА")
        
        gitignore_content = """# Файлы Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Файлы окружения
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Файлы IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Системные файлы
.DS_Store
Thumbs.db

# Логи и временные файлы
*.log
*.tmp
*.temp

# Файлы проекта
instance/
.webassets-cache

# Файлы тестов
.coverage
htmlcov/
.pytest_cache/
.tox/

# Конфигурационные файлы
settings.ini
config.ini

# Файлы базы данных
*.db
*.sqlite3
"""
        
        self.create_file(".gitignore", gitignore_content)
        
        print("\n➕ Добавляем .gitignore в репозиторий:")
        self.run_command("git add .gitignore", "Добавление .gitignore")
        self.run_command('git commit -m "Добавлен .gitignore файл"', "Коммит .gitignore")
        
        # Создаем временный файл для демонстрации игнорирования
        with open("temp_file.tmp", "w") as f:
            f.write("Это временный файл, который должен игнорироваться")
        
        print("\n🔍 Проверяем игнорирование файлов:")
        self.run_command("git status", "Статус - temp_file.tmp должен быть неотслеживаемым", wait_for_user=False)
        
        return True
    
    def step_8_undo_changes(self):
        """Шаг 8: Отмена изменений"""
        self.print_step(8, "ОТМЕНА ИЗМЕНЕНИЙ В GIT")
        
        print("\n⚠️  Симулируем ошибку - случайно изменяем README.md")
        
        # Делаем "случайное" изменение
        with open("README.md", "a", encoding="utf-8") as f:
            f.write("\n\n---\nСЛУЧАЙНЫЙ ТЕКСТ, КОТОРЫЙ НУЖНО ОТМЕНИТЬ\n")
        
        print("\n🔍 Проверяем изменения:")
        self.run_command("git diff README.md", "Показ изменений в README.md", wait_for_user=False)
        
        print("\n↩️  Отменяем изменения в файле:")
        self.run_command("git checkout -- README.md", "Отмена изменений в README.md")
        
        print("\n✅ Проверяем, что изменения отменены:")
        self.run_command("git diff README.md", "Проверка - изменений быть не должно", wait_for_user=False)
        
        return True
    
    def step_9_github_preparation(self):
        """Шаг 9: Подготовка к GitHub"""
        self.print_step(9, "ПОДГОТОВКА К РАБОТЕ С GITHUB")
        
        print("\n🌐 Следующие шаги для работы с GitHub:")
        
        github_steps = """
1. СОЗДАЙТЕ АККАУНТ НА GITHUB:
   • Перейдите на https://github.com
   • Нажмите "Sign up"
   • Используйте email: ardeev1999@gmail.com
   • Выберите имя пользователя (например: vyacheslav-ardeev)

2. СОЗДАЙТЕ НОВЫЙ РЕПОЗИТОРИЙ:
   • Нажмите "+" в правом верхнем углу → "New repository"
   • Имя: my-first-git-project
   • Описание: "Мой первый проект для изучения Git"
   • Public (публичный)
   • НЕ добавляйте README, .gitignore или license

3. ПРИВЯЖИТЕ ЛОКАЛЬНЫЙ РЕПОЗИТОРИЙ К GITHUB:
   Выполните команды в этом терминале:
   
   git remote add origin https://github.com/ВАШ-ЛОГИН/my-first-git-project.git
   git branch -M main
   git push -u origin main

4. ПРОВЕРЬТЕ НА GITHUB:
   • Обновите страницу репозитория
   • Убедитесь, что файлы загружены
"""
        
        print(github_steps)
        
        # Создаем инструкцию в файле
        with open("GITHUB_INSTRUCTIONS.md", "w", encoding="utf-8") as f:
            f.write(github_steps)
        
        print("\n📄 Инструкция сохранена в GITHUB_INSTRUCTIONS.md")
        
        return True
    
    def step_10_summary(self):
        """Шаг 10: Итоги обучения"""
        self.print_step(10, "ИТОГИ ОБУЧЕНИЯ И СЛЕДУЮЩИЕ ШАГИ")
        
        print("\n🎉 ПОЗДРАВЛЯЮ! ВЫ УСПЕШНО ИЗУЧИЛИ ОСНОВЫ GIT!")
        
        # Получаем количество коммитов
        result = subprocess.run(['git', 'rev-list', '--count', 'HEAD'], capture_output=True, text=True)
        commit_count = result.stdout.strip()
        
        # Получаем количество веток
        result = subprocess.run(['git', 'branch'], capture_output=True, text=True)
        branch_count = len(result.stdout.strip().split('\n'))
        
        # Получаем количество файлов
        file_count = len([f for f in os.listdir('.') if os.path.isfile(f)])
        
        summary = f"""
📊 РЕЗУЛЬТАТЫ ОБУЧЕНИЯ:

✅ Создан проект: {self.project_name}
✅ Выполнено шагов: {self.steps_completed}/{self.total_steps}
✅ Создано коммитов: {commit_count}
✅ Создано веток: {branch_count}
✅ Создано файлов: {file_count}

📚 ИЗУЧЕННЫЕ КОМАНДЫ GIT:
1. git init - создание репозитория
2. git add - добавление файлов в индекс
3. git commit - фиксация изменений
4. git status - проверка состояния
5. git log - просмотр истории
6. git branch - работа с ветками
7. git checkout - переключение веток
8. git merge - слияние веток
9. git diff - просмотр изменений
10. git checkout -- <file> - отмена изменений

🚀 СЛЕДУЮЩИЕ ШАГИ В ОБУЧЕНИИ:

1. СОЗДАЙТЕ АККАУНТ НА GITHUB (15 минут)
2. ЗАГРУЗИТЕ ПРОЕКТ НА GITHUB (5 минут)
3. ПЕРЕЙДИТЕ К DJANGO:
   cd ../02_django_project
   python start_django.py

4. НАЧНИТЕ РЕАЛЬНЫЙ ПРОЕКТ:
   Используйте Git для всех своих будущих проектов!

💡 СОВЕТЫ:
• Делайте частые коммиты с понятными сообщениями
• Используйте ветки для новых функций
• Всегда проверяйте git status перед коммитом
• Изучите Git в VS Code (встроенная поддержка)

📞 ПОМОЩЬ:
• Официальная документация: https://git-scm.com/doc
• GitHub Learning Lab: https://lab.github.com/
• Git Book на русском: https://git-scm.com/book/ru/v2
"""
        
        print(summary)
        
        # Сохраняем итоги в файл
        with open("LEARNING_SUMMARY.md", "w", encoding="utf-8") as f:
            f.write(summary)
        
        print("\n📄 Итоги сохранены в LEARNING_SUMMARY.md")
        
        return True
    
    def run(self):
        """Запуск всего процесса обучения"""
        self.print_header("ОБУЧАЮЩИЙ КУРС ПО GIT ДЛЯ НАЧИНАЮЩИХ")
        
        print("👋 Привет, Вячеслав!")
        print("🐙 Этот курс поможет вам освоить Git на практике.")
        print(f"⏱️  Время выполнения: ~30 минут\\n")
        
        input("Нажмите Enter чтобы начать обучение...")
        
        try:
            # Сохраняем исходную директорию
            original_dir = os.getcwd()
            
            # Запускаем все шаги
            steps = [
                self.check_git_installation,
                self.step_1_create_repository,
                self.step_2_create_first_files,
                self.step_3_first_commit,
                self.step_4_modify_files,
                self.step_5_working_with_branches,
                self.step_6_merge_branch,
                self.step_7_gitignore,
                self.step_8_undo_changes,
                self.step_9_github_preparation,
                self.step_10_summary
            ]
            
            for step in steps:
                if not step():
                    print(f"\\n⚠️  Шаг прерван. Продолжаем...")
            
            # Возвращаемся в исходную директорию
            os.chdir(original_dir)
            
            print(f"\\n{'='*70}")
            print("✅ ОБУЧЕНИЕ ЗАВЕРШЕНО УСПЕШНО!")
            print("="*70)
            
            print(f"\\n📁 Ваш проект находится в: {os.path.join(original_dir, self.project_name)}")
            print("🚀 Теперь вы готовы к работе с Git в реальных проектах!")
            
            # Запускаем тестовый скрипт проекта
            print(f"\\n🧪 Запускаю тестовый скрипт проекта...")
            project_path = os.path.join(original_dir, self.project_name, "main.py")
            if os.path.exists(project_path):
                print(f"\\n{'='*50}")
                print("🚀 ЗАПУСК ВАШЕГО ПРОЕКТА:")
                print("="*50)
                os.chdir(os.path.join(original_dir, self.project_name))
                os.system("python main.py")
            
        except KeyboardInterrupt:
            print(f"\\n\\n⚠️  Обучение прервано пользователем.")
        except Exception as e:
            print(f"\\n❌ Произошла ошибка: {e}")
        finally:
            input(f"\\nНажмите Enter для завершения...")

def main():
    """Точка входа"""
    # Создаем экземпляр класса обучения
    git_learning = GitLearning()
    
    # Запускаем обучение
    git_learning.run()

if __name__ == "__main__":
    main()