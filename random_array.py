# Генерирует массив случайных чисел

import random

def generate_array(size: int, min_v: int, max_v: int) -> list[int]:
    return [random.randint(min_v, max_v) for _ in range(size)] # случайное целое число min_v, max_v

