import traceback

data = ["a", "b", "C"]

# 1. Пример обработки (не допуска) исключения проверкой
num = 6
if len(data) >= num:
    print(data[num])
else:
    print(f"В списке нет элемента под номером {num}")

# 2. Обработка всех исключений
try:
    print(data[num])
except:     # Отлавливаем все исключения
    print(f"В списке нет элемента под номером {num}")

# 3. Обработка определенного типа исключения
try:
    print(data[num])
except IndexError as e:     # Отлавливаем исключения IndexError
    print(f"Тип ошибки: {e}")
    print(f"В списке нет элемента под номером {num}")
# Можно отлавливать несколько типов исключений
except ArithmeticError as e:
    print(f"Тип ошибки: {e}")
