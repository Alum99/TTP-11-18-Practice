# Ввод массива вручную через пробел

def input_array_manual() -> list[int]:
    raw = input("Введите числа через пробел: ")
    return [int(x) for x in raw.split()]

