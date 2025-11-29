# Возвращает список индексов, где arr1[i] + arr2[i] == arr3[i]

def check_sum(arr1, arr2, arr3):          # принимает три массива одинаковой длины

    result_indexes = []                   # для хранения индексов
    for i in range(len(arr1)):
        if arr1[i] + arr2[i] == arr3[i]:
            result_indexes.append(i)      # список результатов
    return result_indexes

