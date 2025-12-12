from input_manual import input_array_manual
from random_array import generate_array
from check_sum import check_sum
from power_operation import power_of_sum

def main():
    print("-- Тестирование функций --")

    # генерация массивов
    arr1 = generate_array(5)
    arr2 = generate_array(5)
    arr3 = generate_array(5)

    print("arr1:", arr1)         # [8, 19, 3, 47, 43]
    print("arr2:", arr2)         # [10, 11, 2, 3, 43]
    print("arr3:", arr3)         # [36, 50, 5, 40, 10]

    # ручной ввод
    arr_manual = input_array_manual(5)        # 4 5 6 7 8
    print("Введённый массив:", arr_manual)    # [4, 5, 6, 7, 8]

    # Проверка на сумму индексов
    indexes = check_sum(arr1, arr2, arr3)
    print("Индексы, где arr1[i] + arr2[i] == arr3[i]:", indexes)    # [3]

    # Проверка на лог операции
    if indexes:
        results = power_of_sum(arr1, arr2, arr3, indexes)
        print("Результаты (сумма трёх чисел в степени минимального):", results)  # [100]
    else:
        print("Совпадений нет — возведение в степень не выполняется.")

if __name__ == "__main__":
    main()

