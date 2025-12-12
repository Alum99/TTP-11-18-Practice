# правило сложения
def sum_arrays(arr1, arr2):
    result = []

    for a, b in zip(arr1, arr2):
        if a == b:
            result.append(0)
        else:
            result.append(a + b)

    return result   # итог НЕ по возрастанию

