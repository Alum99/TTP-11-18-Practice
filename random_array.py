# генератор случайных массивов с параметрами по умолчанию
import random

def generate_array(size, min_val=0, max_val=50):
    return [random.randint(min_val, max_val) for _ in range(size)]
