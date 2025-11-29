from manual_input import manual_input
from random_array import random_array
from sort_arrays import sort_arrays
from sum_arrays import sum_arrays

# ручной ввод массивов
arr1, arr2 = manual_input()                                # ввод массивов 1 2 4 5 6, 1 4 5 5 3
arr1_s, arr2_s = sort_arrays(arr1, arr2)                   # сортировка массивов по условиям
final_manual_unsorted = sum_arrays(arr1_s, arr2_s)         # финальный массив несортированный
final_manual_sorted = sorted(sum_arrays(arr1_s, arr2_s))   # финальный массив сортированный

# сложение
print("\n-- Результат для ручного ввода --")
print("\nРезультат неотсортированный:", final_manual_unsorted)      # [7, 8, 0, 7, 6]
print("\nРезультат отсортированный:", final_manual_sorted)          # [0, 6, 7, 7, 8]

# случайный ввод массивов
arr1_r, arr2_r = random_array(5)
print("\nСлучайные массивы:")
print(arr1_r)                                         # [44, 43, 37, 22, 41]
print(arr2_r)                                         # [47, 9, 11, 41, 35]

arr1_r_s, arr2_r_s = sort_arrays(arr1_r, arr2_r)
final_random = sum_arrays(arr1_r_s, arr2_r_s)
print("\n-- Результаты для рандомного ввода --")
print("\nРезультат отсортированный:", final_random)   # [53, 54, 76, 78, 69]

