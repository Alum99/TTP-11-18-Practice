# ручной ввода массивов
def manual_input():
    size = int(input("Введите размер массивов: "))

    print("Введите элементы первого массива через пробел:")
    arr1 = list(map(int, input().split()))

    print("Введите элементы второго массива через пробел:")
    arr2 = list(map(int, input().split()))

    if len(arr1) != size or len(arr2) != size:          # Проверка размера
        raise ValueError(f"Ошибка: нужно ввести {size} чисел, а введено {len(arr1)} и {len(arr2)}")

    return arr1, arr2

