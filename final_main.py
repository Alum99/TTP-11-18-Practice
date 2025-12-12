# импорты для задач 1,2,3
from manual_input_1 import input_array_manual
from random_array_1 import generate_array
from reverse_num_1 import reverse_number

from input_manual_2 import input_array_manual as input_array_manual_v2
from random_array_2 import generate_array as generate_array_v2
from check_sum_2 import check_sum
from power_operation_2 import power_of_sum

from manual_input_3 import manual_input as manual_input_v3
from random_array_3 import random_array
from sort_arrays_3 import sort_arrays
from sum_arrays_3 import sum_arrays

def task_1():  # решение задачи 1
    print("Выберите способ ввода массивов:")
    print("1 — ввод чисел вручную")
    print("2 — генерация случайных чисел")
    print("-----------------------")
    mode = int(input("Выберите способ ввода: "))

    # ввод массивов, они могут быть разных размеров
    if mode == 1: # вручную
        print("\nВведите первый массив:")
        arr1 = input_array_manual()
        print("Введите второй массив:")
        arr2 = input_array_manual()
    else: # генерация
        size1 = int(input("Размер первого массива: "))
        size2 = int(input("Размер второго массива: "))
        arr1 = generate_array(size1, 0, 100)
        arr2 = generate_array(size2, 0, 100)

    print("\nПервый массив: ", arr1)
    print("Второй массив: ", arr2)

    # считаем общие и перевёрнутые числа
    count = 0
    res = []
    for num1 in arr1:
        if num1 in arr2 or reverse_number(num1) in arr2:
            count += 1
            res.append(num1)

    print("\nОбщие и перевёрнутые числа:", res)
    print(f"Общее количество одинаковых чисел (включая перевёрнутые): {count}")


def task_2(): # решение задачи 2
    print("Выберите способ ввода массивов:")
    print("1 — ввод вручную")
    print("2 — генерация случайных")
    mode = int(input("Выберите способ: "))
    size = int(input("Выберите размер массивов (3 массива будут одинакового размера): "))

    if mode == 1: # ручной ввода
        arr1 = input_array_manual_v2(size)
        arr2 = input_array_manual_v2(size)
        arr3 = input_array_manual_v2(size)

    else: # случайная генерация
        arr1 = generate_array_v2(size)
        arr2 = generate_array_v2(size)
        arr3 = generate_array_v2(size)

    print("\nПервый массив: ", arr1)
    print("Второй массив: ", arr2)
    print("Третий массив: ", arr3)

    # Находим индексы, где a[i] + b[i] == c[i]
    indexes = check_sum(arr1, arr2, arr3)

    if not indexes:
        print("\nНет индексов, где два числа под одним и тем же номером будут в сумме давать третье число.\n")
        return

    # Возведение в степень
    results = power_of_sum(arr1, arr2, arr3, indexes)

    print("\nИндексы:", indexes)
    print("Результаты возведения суммы в степень:", results, "\n")


def task_3(): # решение задачи 3
    print("Выберите способ ввода массивов:")
    print("1 — ввод вручную")
    print("2 — генерация случайных")
    mode = int(input("Выберите способ: "))
    size = int(input("Выберите размер массивов (2 массива будут одинакового размера): "))

    if mode == 1:    # ручной ввода
        arr1, arr2 = manual_input_v3()
    else:            # случайная генерация
        arr1, arr2 = random_array(size)

    print("\nПервый массив: ", arr1)
    print("Второй массив: ", arr2)

    # Сортируем
    arr1_sorted, arr2_sorted = sort_arrays(arr1, arr2)

    print("\nПервый массив отсортированный: ", arr1_sorted)
    print("Второй массив отсортированный: ", arr2_sorted )

    # Складываем
    result = sum_arrays(arr1_sorted, arr2_sorted)

    print("\nРезультат сложения:", sorted(result))
    print()

def main():
    while True:
        print("\nВыберите задачу:")
        print("===========================")
        print("1 — Входные данные: 2 массива с числами. Сколько у массивов общих чисел.")
        print("2 — Входные данные: 3 массива с числами одинакового размера. Могут ли два числа в сумме давать третье число.")
        print("3 — Входные данные: 2 массива с числами одинакового размера. Нужно произвести сумму чисел из массивов.")
        print("0 — Выход")
        print("===========================")

        choice = input("Введите номер выбранного пункта: ")

        if choice == "1":
            print("\nПолное условие задачи:\n"
                  "Входные данные: 2 массива с числами. Требуется проверить, сколько у массивов общих чисел.\n"
                  "Число считается общим, если оно есть в одном массиве,\n"
                  "а в другом массиве находится его перевернутая версия.\n"
                  "\nРешение:")
            task_1()

        elif choice == "2":
            print("\nПолное условие задачи:\n"
                  "Входные данные: 3 массива с числами одинакового размера. Нужно проверить, \n"
                  "могут ли два числа под одним и тем же номером в сумме давать третье число.\n"
                  "Если могут, то сумма трех чисел возводится в степень наименьшего числа.\n"
                  "\nРешение:")
            task_2()

        elif choice == "3":
            print("\nПолное условие задачи:\n"
                  "Входные данные: 2 массива с числами одинакового размера. Нужно произвести сумму чисел из массивов,\n"
                  "первый массив должен быть отсортирован в порядке убывания, второй в порядке возрастания.\n"
                  "Если числа в массивах совпадают, их сумма будет равна нулю.\n"
                  "Конечный массив нужно отсортировать в порядке возрастания.\n"
                  "\nРешение:")
            task_3()

        elif choice == "0":
            print("Выход")
            break
        else:
            print("Ошибка: неправильный выбор!")

if __name__ == "__main__":
    main()
