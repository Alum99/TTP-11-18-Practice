import random
from logger import logger
from messages import Messages
from exceptions import InvalidValueError, InputError, OperationError, AppError

# генерация случайных массивов с обработкой ошибок
def random_array(size: int, min_val: int = 0, max_val: int = 50) -> tuple[list[int], list[int]]: # аннотация возвращаемого значения
    """
    Генерирует два массива случайных целых чисел одинакового размера.

    Параметры:
        :param size: количество элементов в каждом массиве
        :param min_val: минимальное возможное значение элемента (включительно)
        :param max_val: максимальное возможное значение элемента (включительно)

    Возвращает:
        :return:  кортеж из двух массивов (arr1, arr2)

    :raises InvalidValueError: если size <= 0
    """

    logger.info("Генерация случайных массивов")
    if size <= 0:
        raise InvalidValueError("Размер массива должен быть положительным")

    arr1 = [random.randint(min_val, max_val) for _ in range(size)]
    arr2 = [random.randint(min_val, max_val) for _ in range(size)]
    return arr1, arr2


# ручной ввода массивов с обработкой ошибок
def manual_input() -> tuple[list[int], list[int]]:
    """
    Выполняет ручной ввод двух массивов одинакового размера.

    Пользователь вводит размер массивов, затем элементы
    каждого массива через пробел. Если количество введённых
    элементов не совпадает с заданным размером, возникает ошибка.

    Возвращает:
        :return:  кортеж из двух массивов (arr1, arr2)

    Ошибки:
        :raises InputError: если ввод некорректен
    """

    logger.info("Ручной ввод массивов")
    try:
        size = int(input("Введите размер массивов: "))
        if size <= 0:
            raise InvalidValueError("Размер массива должен быть положительным")

        arr1 = [int(x) for x in input("Введите первый массив: ").split()]
        arr2 = [int(x) for x in input("Введите второй массив: ").split()]

        if len(arr1) != size or len(arr2) != size:
            raise InputError(
                f"Ожидалось {size} элементов, получено {len(arr1)} и {len(arr2)}"
            )
        return arr1, arr2

    except ValueError:
        raise InputError("Введены нецелые числа")


# сортировка массивов по условиям
def sort_arrays(arr1: list[int], arr2: list[int]) -> tuple[list[int], list[int]]:
    """
    Сортирует два массива по заданным условиям.

    Первый массив сортируется по убыванию,
    второй массив — по возрастанию.

    Параметры:
        :param arr1: первый массив чисел
        :param arr2: второй массив чисел

    Возвращает:
        :return: кортеж из отсортированных массивов (arr1_sorted, arr2_sorted)
    """

    logger.info("Сортировка массивов")
    return sorted(arr1, reverse=True), sorted(arr2)


# правило сложения массивов
def sum_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Выполняет поэлементное сложение двух массивов.

    Если элементы с одинаковыми индексами равны,
    в результирующий массив добавляется 0.
    В противном случае добавляется сумма элементов.

    Параметры:
        :param arr1: первый массив чисел
        :param arr2: второй массив чисел

    Возвращает:
        :return: массив результатов сложения

    :raises OperationError: если размеры массивов различаются
    """

    logger.info("Сложение массивов")
    if len(arr1) != len(arr2):
        raise OperationError("Массивы должны быть одинаковой длины")
    return [0 if a == b else a + b for a, b in zip(arr1, arr2)]


# меню для 3 задания с обработкой ошибо
def task_3_menu() -> None:
    """
    Меню задачи 3:

    Работа с двумя массивами чисел одинакового размера.
    Сортировка массивов по заданным условиям и выполнение поэлементного сложения.

    Пользователь может:
        1. Ввести два массива вручную.
        2. Сгенерировать два массива случайных чисел.
        3. Показать исходные массивы, отсортированные массивы
           и результат сложения.
        4. Выйти в главное меню.

    Алгоритм работы:
        - первый массив сортируется по убыванию;
        - второй массив сортируется по возрастанию;
        - если элементы с одинаковыми индексами равны,
          в результат записывается 0, иначе — их сумма.

    Взаимодействие с пользователем:
        Функция запрашивает ввод через input() и выводит информацию через print().

    Возвращаемое значение:
    :return: функция завершает работу при выборе выхода в главное меню.
    """

    arr1: list[int] | None = None
    arr2: list[int] | None = None
    arr1_sorted: list[int] | None = None
    arr2_sorted: list[int] | None = None
    result: list[int] | None = None
    msgs = Messages.TASK3

    while True:
        print("\n" + msgs.title)
        for option in msgs.menu:
            print(option)

        choice = input(msgs.prompt)
        logger.info(f"task3: выбран пункт {choice}")

        # ручной ввод и преобразования
        if choice == "1":
            try:
                arr1, arr2 = manual_input()
                arr1_sorted, arr2_sorted = sort_arrays(arr1, arr2)
                result = sum_arrays(arr1_sorted, arr2_sorted)
                logger.info("Массивы введены вручную и обработаны")
            except AppError as e:
                logger.error(str(e))
                print(msgs.input_error)

        # генерация случайных массивов
        elif choice == "2":
            try:
                size = int(input("Введите размер массивов: "))
                arr1, arr2 = random_array(size)
                arr1_sorted, arr2_sorted = sort_arrays(arr1, arr2)
                result = sum_arrays(arr1_sorted, arr2_sorted)
                logger.info("Массивы сгенерированы и обработаны")
            except (ValueError, AppError) as e:
                logger.error(str(e))
                print(msgs.input_error)

        # результат и вывод
        elif choice == "3":
            if arr1 is None or result is None:
                print(msgs.no_data)
            else:
                print("Первый массив:", arr1)
                print("Второй массив:", arr2)
                print("Первый (убывание):", arr1_sorted)
                print("Второй (возрастание):", arr2_sorted)
                print("Результат:", sorted(result))
                logger.info("Результаты выведены")

        # выход в главное меню
        elif choice == "4":
            logger.info("Возврат в главное меню")
            return

        # Отключение логирования
        elif choice == "5":
            logger.setLevel("CRITICAL")
            print("Логирование отключено")
            logger.critical("Установлен уровень CRITICAL")

        else:
            print(msgs.invalid_choice)
            logger.info("Неверный пункт меню task3")

# ГЛАВНОЕ МЕНЮ 

def main():
    while True:
        print("\nГЛАВНОЕ МЕНЮ")
        print("1. Задание 3")
        print("0. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            task_3_menu()
        elif choice == "0":
            print("Выход")
            break
        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    main()