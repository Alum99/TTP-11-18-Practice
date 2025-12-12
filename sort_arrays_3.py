# сортировка массивов по условиям
def sort_arrays(arr1, arr2):
    arr1_sorted = sorted(arr1, reverse=True)   # убывание
    arr2_sorted = sorted(arr2)                 # возрастание
    return arr1_sorted, arr2_sorted

