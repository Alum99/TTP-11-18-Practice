def input_array_manual(size):
    print(f"Введите {size} чисел через пробел:")     # f-строка для динамической подстановки значения size
    arr = list(map(int, input().split()))            # преобразование ввода
    if len(arr) != size:                             # проверка размера массива
        raise ValueError("Количество чисел не совпадает с заданным размером!")
    return arr                                       # возвращает введенный массив чисел

