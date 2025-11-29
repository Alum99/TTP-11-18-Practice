from sorting import sort_array
from merge import merge_arrays
from manual_input import input_array_manual
from random_array import generate_array
from reverse_num import reverse_number


def test_sort():
    print("\n-- Тест сортировки --")
    arr = [5, 1, 3, 2]
    print("Исходный:", arr)                        # [5, 1, 3, 2]
    print("Отсортированный:", sort_array(arr))     # [1, 2, 3, 5]


def test_merge():
    print("\n-- Тест объединения --")
    a = [1, 2]
    b = [3, 4]
    print("Результат:", merge_arrays(a, b))         # [1, 2, 3, 4]


def test_manual_input():
    print("\n-- Тест ручного ввода --")
    arr = input_array_manual()                      # 2 3 6 8 1
    print("Вы ввели:", arr)                         # [2, 3, 6, 8, 1]


def test_random_generation():
    print("\n-- Тест генерации массива --")
    arr = generate_array(5, 1, 10)
    print("Случайный массив:", arr)                  # [4, 6, 1, 7, 5]


def test_reverse():
    print("\n-- Тест переворота числа --")
    print("123 →", reverse_number(123))              # 321
    print("4005 →", reverse_number(4005))            # 5004


def main():
    print("== Тестирование всех функций ==")

    test_sort()
    test_merge()
    test_reverse()
    test_random_generation()

    print("\n== Тест ручного ввода: ==")
    test_manual_input()


if __name__ == "__main__":
    main()
