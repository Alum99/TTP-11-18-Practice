# импорты для задач 1,2,3
from sorting_1 import sort_array
from merge_1 import merge_arrays
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

def task_1():
    print("Тут будет решение задачи 1.")

def task_2():
    print("Тут будет решение задачи 2.")

def task_3():
    print("Тут будет решение задачи 3.")

def main():
    while True:
        print("\nВыберите задачу:")
        print("===========================")
        print("1 — Входные данные: 2 массива с числами. Сколько у массивов общих чисел.")
        print("2 — Входные данные: 3 массива с числами одинакового размера. Могут ли два числа в сумме давать третье число.")
        print("3 — Входные данные: 2 массива с числами одинакового размера. Нужно произвести сумму чисел из массивов.")
        print("0 — Выход")
        print("===========================")

        choice = input("Ваш выбор: ")

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
