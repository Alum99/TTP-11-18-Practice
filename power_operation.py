# Для найденных индексов (из check_sum.py)

def power_of_sum(arr1, arr2, arr3, indexes):

    results = []
    for i in indexes:
        a, b, c = arr1[i], arr2[i], arr3[i]
        total = a + b + c                       # суммируем 3 числа
        power = min(a, b, c)                    # находим наименьшее
        results.append(total ** power)          # возводим в степень
    return results                              # возвращает список значений
