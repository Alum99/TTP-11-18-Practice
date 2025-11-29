# Возвращает число, записанное в обратном порядке цифр

def reverse_number(n: int) -> int:
    s = str(n)
    return int(s[::-1])

