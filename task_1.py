import random
from logger import logger

# Генерирует массив случайных чисел
def generate_array(size: int, min_v: int, max_v: int) -> list[int]:
    """
    Генерирует массив случайных целых чисел.

    Параметры:
        :param size: количество элементов массива (длина).
        :param min_v: минимальное возможное значение числа (включительно), по умолчанию 0.
        :param max_v: максимальное возможное значение числа (включительно), по умолчанию 50.

    Возвращает:
        :return: список случайных целых чисел длиной size.
    """

    # случайное целое число из промежутка min_v, max_v
    logger.info("Генерация случайного массива")
    try:
        if size <= 0:
            raise ValueError("Размер массива должен быть положительным числом")    # искусственно вызванная ошибка
        return [random.randint(min_v, max_v) for _ in range(size)]
    except Exception as e:                                  # сохраняет объект ошибки в переменной e
        logger.error(f"Ошибка генерации массива: {e}")      # лог с уровнем ERROR
        print("Ошибка генерации массива:", e)               # сообщение, не прерывая выполнение программы.
        return []                                           # пустой список


# Ввод массива вручную через пробел
def input_array_manual() -> list[int]:
    """
    Выполняет ручной ввод массива чисел через пробел.

    Пользователь вводит строку чисел, разделённых пробелом.
    Преобразует введённые данные в список целых чисел.

    Возвращает:
        :return: список введённых пользователем чисел.
    """

    logger.info("Ввод массива вручную")
    try:
        raw = input("Введите числа через пробел: ")
        arr = [int(x) for x in raw.split()]
        if not arr:
            raise ValueError("Массив не может быть пустым")
        return arr
    except ValueError as ve:  # исключения типа ValueError(данные нельзя преобразовать в целые, кол-во не соотв ожидаемым)
        logger.error(f"Ошибка ввода: {ve}")   # лог с уровнем ERROR
        print("Ошибка ввода:", ve)
        return []
    except Exception as e:    # любые другие исключения
        logger.error(f"Неизвестная ошибка ввода: {e}")
        print("Произошла ошибка:", e)
        return []


# Возвращает число, записанное в обратном порядке цифр
def reverse_number(n: int) -> int:
    """
    Возвращает число, записанное в обратном порядке цифр.

    Параметры:
        :param n: исходное целое число.

    Возвращает:
        :return: число с перевернутым порядком цифр.
    """

    # logger.info("Переворот числа")
    try:
        s = str(n)
        return int(s[::-1])
    except Exception as e:
        logger.error(f"Ошибка переворота числа {n}: {e}") # лог с уровнем ERROR
        print("Ошибка переворота числа:", e)
        return n


# меню для задания 1
def task_1_menu():
    """
    Задача 1.

    Подсчёт количества общих чисел в двух массивах.
    Число считается общим, если оно присутствует в обоих массивах
    или если в одном массиве есть число, а в другом — его перевёрнутая версия
    (например, 12 и 21).

    Функциональность меню:
        1. Ввод массивов вручную
        2. Генерация случайных массивов
        3. Выполнение алгоритма
        4. Вывод результата
        5. Возврат в главное меню

    Алгоритм работы
    1. Считать или сгенерировать два массива целых чисел.
    2. Для каждого элемента первого массива проверить:
       - содержится ли он во втором массиве;
       - содержится ли во втором массиве его перевёрнутая версия.
    3. Подсчитать количество таких элементов.
    4. Вывести список найденных чисел и их общее количество.

    Возвращает:
        None
    Функция выводит результат на экран и не возвращает значение.
    """

    arr1 = None
    arr2 = None
    result = None

    while True:
        print("\n=====ЗАДАНИЕ 1======")
        print("1. Ввести массивы вручную")
        print("2. Сгенерировать массивы случайно")
        print("3. Посчитать общие и перевёрнутые числа")
        print("4. Показать результат")
        print("5. Назад в главное меню")
        print("6. Отключить логирование (CRITICAL)")

        choice = input("Выберите пункт: ")
        logger.info(f"Пользователь выбрал пункт меню task_1: {choice}")

        # ввод вручную
        if choice == "1":
            try:
                print("Первый массив:")
                arr1 = input_array_manual()
                print("Второй массив:")
                arr2 = input_array_manual()
                if not arr1 or not arr2:
                    raise RuntimeError("Ввод массивов не удался")
                result = None
                logger.info("Массивы введены вручную")
            except Exception as e:
                logger.error(f"Ошибка ручного ввода: {e}")
                print("Ошибка ручного ввода:", e)


        # генерация массивов
        elif choice == "2":
            try:
                size1 = int(input("Размер первого массива: "))
                size2 = int(input("Размер второго массива: "))
                arr1 = generate_array(size1, 0, 100)
                arr2 = generate_array(size2, 0, 100)
                if not arr1 or not arr2:
                    raise RuntimeError("Генерация массивов не удалась")
                print("Первый массив:", arr1)
                print("Второй массив:", arr2)
                result = None
                logger.info("Массивы сгенерированы автоматически")
            except Exception as e:
                logger.error(f"Ошибка генерации массивов: {e}")
                print("Ошибка генерации массивов:", e)


        # вычисление
        elif choice == "3":
            try:
                if arr1 is None or arr2 is None:
                    raise RuntimeError("Сначала введите или сгенерируйте массивы")
                count = 0
                used_pairs = []
                for a in arr1:
                    for b in arr2:
                        if (a == b) or (a == reverse_number(b)) or (reverse_number(a) == b):
                            pair = (min(a, b), max(a, b))
                            if pair not in used_pairs:
                                used_pairs.append(pair)
                                count += 1
                result = count
                print("Подсчёт выполнен")
                logger.info("Подсчёт выполнен")
            except Exception as e:
                logger.error(f"Ошибка подсчёта: {e}")
                print("Ошибка подсчёта:", e)


        # вывод результата
        elif choice == "4":
            try:
                if result is None:
                    raise RuntimeError("Нет результата для вывода")
                print(f"Общее количество одинаковых чисел: {result}")
                logger.info("Результат выведен")
            except Exception as e:
                logger.error(f"Ошибка вывода результата: {e}")
                print("Ошибка вывода результата:", e)

        # выход в главное меню
        elif choice == "5":
            logger.info("Возврат в главное меню")
            return

        # отключение логирования
        elif choice == "6":
            logger.setLevel("CRITICAL")
            print("Логирование отключено")
            logger.critical("Установлен уровень CRITICAL")

        else:
            print("Неверный пункт.")
            logger.info("Неверный пункт меню")


# ГЛАВНОЕ МЕНЮ

def main():
    while True:
        print("\nГЛАВНОЕ МЕНЮ")
        print("1. Задание 1")
        print("0. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            task_1_menu()
        elif choice == "0":
            print("Выход")
            break
        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    main()