# генерация случайных массивов
import random

def random_array(size, min_val=0, max_val=50):
    arr1 = [random.randint(min_val, max_val) for _ in range(size)]
    arr2 = [random.randint(min_val, max_val) for _ in range(size)]
    return arr1, arr2

