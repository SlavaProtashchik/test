# malicious_rfi.py

def evil_function():
    import os
    os.system("uname -a")  # Выполнение произвольной команды для получения информации о системе

# Вызов функции для демонстрации
evil_function()
