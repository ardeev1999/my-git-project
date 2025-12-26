#!/usr/bin/env python3
"""
Git Learning - Финальная версия без ошибок кодировки
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

def run_command_safe(command, description, wait=True):
    """
    Безопасный запуск команд с обработкой кодировки Windows
    """
    print(f"\n💻 {description}")
    print(f"   Команда: {command}")
    
    if wait:
        input("\n   Нажмите Enter для выполнения...")
    
    try:
        # Для Windows используем правильную кодировку (cp866 для русской Windows)
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=False  # Не конвертируем в текст сразу!
        )
        
        # Пытаемся декодировать с разными кодировками
        encodings = ['utf-8', 'cp866', 'cp1251', 'iso-8859-1']
        
        stdout_decoded = ""
        stderr_decoded = ""
        
        for encoding in encodings:
            try:
                stdout_decoded = result.stdout.decode(encoding)
                stderr_decoded = result.stderr.decode(encoding)
                break
            except UnicodeDecodeError:
                continue
        
        # Если не удалось декодировать, используем байты
        if not stdout_decoded and not stderr_decoded:
            stdout_decoded = str(result.stdout)[:200]
            stderr_decoded = str(result.stderr)[:200]
        
        if stdout_decoded.strip():
            print(f"\n✅ Результат:\n{stdout_decoded[:300]}")
        
        if stderr_decoded.strip() and "warning" not in stderr_decoded.lower():
            print(f"\n⚠️  Ошибки:\n{stderr_decoded[:300]}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Ошибка выполнения: {str(e)[:100]}")
        return False

def create_project():
    """Создание проекта"""
    project_name = "my_git_project"
    
    if os.path.exists(project_name):
        print(f"📁 Папка '{project_name}' уже существует.")
        choice = input("   Удалить и создать заново? (y/n): ").lower()
        if choice == 'y':
            import shutil
            shutil.rmtree(project_name, ignore_errors=True)
            print(f"✅ Папка удалена")
        else:
            project_name = input("   Введите новое имя проекта: ")
    
    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)
    
    print(f"📂 Рабочая папка: {os.getcwd()}")
    return project_name

def create_files():
    """Создание файлов проекта"""
    print("\n📄 СОЗДАЕМ ФАЙЛЫ ПРОЕКТА:")
    
    # README.md
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(f"""# Мой Git проект

Проект создан для изучения Git.

## Автор
Вячеслав Ардеев

## Контакты
Email: ardeev1999@gmail.com

## Технологии
- Python 3.x
- Git
- VS Code

## Дата создания
{datetime.now().strftime('%Y-%m-%d %H:%M')}
""")
    print("✅ README.md создан")
    
    # main.py
    with open("main.py", "w", encoding="utf-8") as f:
        f.write('''#!/usr/bin/env python3
"""
Главный файл проекта
"""

def main():
    print("="*50)
    print("ПРИВЕТСТВИЕ ОТ GIT ПРОЕКТА!")
    print("="*50)
    
    print("\\n👤 Автор: Вячеслав Ардеев")
    print("📧 Email: ardeev1999@gmail.com")
    
    print("\\n🐙 Этот проект создан для изучения Git.")
    print("\\n🚀 Начните с команд:")
    print("   git init")
    print("   git add .")
    print("   git commit -m 'Сообщение'")
    print("\\n" + "="*50)

if __name__ == "__main__":
    main()
''')
    print("✅ main.py создан")
    
    # utils.py
    with open("utils.py", "w", encoding="utf-8") as f:
        f.write('''#!/usr/bin/env python3
"""
Вспомогательные функции
"""

def show_system_info():
    """Показать информацию о системе"""
    import platform
    import sys
    
    print("\\n🖥️  ИНФОРМАЦИЯ О СИСТЕМЕ:")
    print(f"  ОС: {platform.system()} {platform.release()}")
    print(f"  Python: {sys.version.split()[0]}")
    print(f"  Архитектура: {platform.architecture()[0]}")

def calculate(a, b):
    """Простой калькулятор"""
    print(f"\\n🧮 КАЛЬКУЛЯТОР:")
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
''')
    print("✅ utils.py создан")
    
    # Показываем файлы
    print("\n📁 Файлы в проекте:")
    files = os.listdir('.')
    for file in files:
        if os.path.isfile(file):
            size = os.path.getsize(file)
            print(f"  📄 {file} ({size} байт)")

def git_tutorial():
    """Git туториал"""
    print_header("GIT ТУТОРИАЛ - ВЫПОЛНИТЕ ЭТИ КОМАНДЫ")
    
    print("""
📋 ОТКРОЙТЕ НОВЫЙ ТЕРМИНАЛ VS CODE:
1. Нажмите Ctrl+Shift+`
2. ИЛИ Terminal → New Terminal

🐙 ВЫПОЛНИТЕ КОМАНДЫ ПО ПОРЯДКУ:
""")
    
    commands = [
        ("git init", "Инициализация Git репозитория"),
        ("git status", "Проверка состояния файлов"),
        ("git add .", "Добавление всех файлов в индекс"),
        ('git commit -m "Initial commit: созданы базовые файлы"', "Первый коммит"),
        ("git log --oneline", "Просмотр истории коммитов"),
    ]
    
    for i, (cmd, desc) in enumerate(commands, 1):
        print(f"{i:2}. {cmd}")
        print(f"    # {desc}")
    
    print("""
💡 СОВЕТЫ:
• Копируйте команды (Ctrl+C) и вставляйте в терминал (Ctrl+V)
• Смотрите результат после каждой команды
• Не пропускайте шаги
""")
    
    input("\n🎯 Нажмите Enter когда выполните все команды...")
    
    # Проверяем результат
    print("\n📊 ПРОВЕРКА РЕЗУЛЬТАТОВ:")
    
    # Проверяем наличие .git папки
    if os.path.exists(".git"):
        print("✅ Git репозиторий создан (.git/ существует)")
    else:
        print("❌ Git репозиторий не создан")
        print("   Выполните команду: git init")
    
    # Проверяем коммиты
    try:
        result = subprocess.run(
            "git log --oneline",
            shell=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        if result.stdout:
            print(f"\n✅ История коммитов:\n{result.stdout}")
        else:
            print("\n⚠️  Нет коммитов в истории")
            print("   Выполните: git add . и git commit")
    except:
        print("\n⚠️  Не удалось проверить историю")

def create_github_instructions():
    """Инструкции для GitHub"""
    print_header("СЛЕДУЮЩИЕ ШАГИ: GITHUB")
    
    instructions = """
🌐 СОЗДАНИЕ АККАУНТА НА GITHUB:

1. Перейдите на: https://github.com
2. Нажмите "Sign up"
3. Введите:
   • Email: ardeev1999@gmail.com
   • Имя пользователя: vyacheslav-ardeev (или свой вариант)
   • Пароль
4. Подтвердите email

📦 СОЗДАНИЕ РЕПОЗИТОРИЯ:

1. Нажмите "+" → "New repository"
2. Заполните:
   • Repository name: my-git-project
   • Description: Мой первый Git проект
   • Public (публичный)
   • НЕ добавляйте README, .gitignore, license
3. Нажмите "Create repository"

🔗 ПРИВЯЗКА ЛОКАЛЬНОГО РЕПОЗИТОРИЯ:

Выполните команды в терминале:

git remote add origin https://github.com/ВАШ-ЛОГИН/my-git-project.git
git branch -M main
git push -u origin main

📤 ЗАГРУЗКА КОДА:

После выполнения команд выше:
1. Обновите страницу GitHub
2. Увидите свои файлы на GitHub
3. Поздравляю! Ваш код теперь в облаке!
"""
    
    print(instructions)
    
    # Сохраняем инструкции в файл
    with open("GITHUB_INSTRUCTIONS.md", "w", encoding="utf-8") as f:
        f.write(instructions)
    
    print("\n📄 Инструкции сохранены в GITHUB_INSTRUCTIONS.md")

def run_project():
    """Запуск проекта"""
    print_header("ЗАПУСК ПРОЕКТА")
    
    print("🧪 ЗАПУСКАЕМ ВАШ ПРОЕКТ:\n")
    
    if os.path.exists("main.py"):
        print("🚀 Запуск main.py:")
        print("="*50)
        os.system("python main.py")
        print("="*50)
    
    if os.path.exists("utils.py"):
        print("\n🚀 Запуск utils.py:")
        print("="*50)
        os.system("python utils.py")
        print("="*50)

def main():
    """Главная функция"""
    print("\n" + "="*70)
    print("🐙 GIT LEARNING - ПРАКТИЧЕСКИЙ КУРС")
    print("="*70)
    
    print("\n👋 Привет, Вячеслав!")
    print("✅ Этот скрипт без ошибок кодировки")
    print("⏱️  Время выполнения: 15-20 минут\n")
    
    input("Нажмите Enter чтобы начать...")
    
    try:
        # Запоминаем начальную папку
        start_dir = os.getcwd()
        
        # Создаем проект
        print_header("СОЗДАНИЕ ПРОЕКТА")
        project_name = create_project()
        
        # Создаем файлы
        print_header("СОЗДАНИЕ ФАЙЛОВ")
        create_files()
        
        # Git туториал
        print_header("ОБУЧЕНИЕ GIT")
        git_tutorial()
        
        # GitHub инструкции
        print_header("РАБОТА С GITHUB")
        create_github_instructions()
        
        # Запуск проекта
        print_header("ТЕСТИРОВАНИЕ")
        run_project()
        
        # Возвращаемся в исходную папку
        os.chdir(start_dir)
        
        # Итоги
        print_header("🎉 ОБУЧЕНИЕ ЗАВЕРШЕНО!")
        
        print(f"""
📊 РЕЗУЛЬТАТЫ:

✅ Создан проект: {project_name}
✅ Созданы файлы: 3
✅ Изучены команды Git: 5
✅ Готовность к GitHub: 100%

📁 Ваш проект здесь:
{os.path.join(start_dir, project_name)}

🚀 ЧТО ДЕЛАТЬ ДАЛЬШЕ:

1. Создайте аккаунт на GitHub (15 минут)
2. Загрузите проект на GitHub (5 минут)
3. Переходите к Django:
   cd ../02_django_project

💪 ВЫ МОЛОДЕЦ!
Вы успешно прошли базовое обучение Git.
Теперь используйте Git во всех своих проектах!
""")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Обучение прервано")
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
    finally:
        input("\nНажмите Enter для выхода...")

if __name__ == "__main__":
    # Устанавливаем кодировку для Windows
    if os.name == 'nt':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    main()