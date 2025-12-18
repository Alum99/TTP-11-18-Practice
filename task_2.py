import random
from logger import logger
from messages import Messages
from exceptions import InputError, InvalidValueError, DataNotSetError, OperationError, AppError

# генератор случайных массивов с параметрами по умолчанию
def generate_array(size: int, min_val: int = 0, max_val: int = 50) -> list[int]: # аннотация возвращаемого значения
    """
    Генерирует массив случайных целых чисел заданного размера.

    Параметры:
        :param size: количество элементов в массиве.
        :param min_val: минимальное возможное значение элемента (включительно), по умолчанию 0.
        :param max_val: максимальное возможное значение элемента (включительно), по умолчанию 50.

    Возвращает:
        :return: список случайных целых чисел длиной size.

    raises InvalidValueError: если size <= 0
    """

    logger.info("Генерация случайного массива")
    if size <= 0:
        raise InvalidValueError("Размер массива должен быть положительным")
    return [random.randint(min_val, max_val) for _ in range(size)]


# ввод массива вручную
def input_array_manual(size: int) -> list[int]:
    """
    Выполняет ручной ввод массива чисел с клавиатуры.

    Пользователь должен ввести ровно size целых чисел,
    разделённых пробелами. Если количество введённых
    чисел не совпадает с size, вызывается исключение.

    Параметры:
        :param size: требуемое количество элементов массива.

    Возвращает:
        :return: список целых чисел, введённых пользователем.

    Ошибки:
        :raises InputError: если ввод некорректный.
    """

    logger.info("Ввод массива вручную")
    raw = input(f"Введите {size} чисел через пробел: ").strip()
    if not raw:
        raise InputError("Пустой ввод")
    try:
        arr = [int(x) for x in raw.split()]
        if len(arr) != size:
            raise InputError(f"Количество введённых чисел ({len(arr)}) не совпадает с заданным ({size})")
        return arr
    except ValueError:
        raise InputError("Введены нецелые числа")


# Возвращает список индексов, где arr1[i] + arr2[i] == arr3[i]
# принимает три массива одинаковой длины
def check_sum(arr1: list[int], arr2: list[int], arr3: list[int]) -> list[int]:
    """
    Находит индексы элементов массивов, для которых
    arr1[i] + arr2[i] == arr3[i]

    Все три массива должны быть одинаковой длины.

    Параметры:
        :param arr1: первый массив чисел
        :param arr2: второй массив чисел
        :param arr3: третий массив чисел

    Возвращает:
        :return: список индексов, удовлетворяющих условию

    :raises DataNotSetError: если массивы имеют разную длину
    """

    logger.info("Вызов check_sum()")
    if len(arr1) != len(arr2) or len(arr2) != len(arr3):
        raise DataNotSetError("Все массивы должны быть одинаковой длины")

    return [i for i in range(len(arr1)) if arr1[i] + arr2[i] == arr3[i]]


# Вычисление (a + b + c) ** min(a, b, c)
def power_of_sum(arr1: list[int], arr2: list[int], arr3: list[int], indexes: list[int]) -> list[int]:
    """
    Возводит сумму элементов по индексам в степень минимального из них.

    (Вычисляет значения (a + b + c) ** min(a, b, c)
    для элементов массивов по заданным индексам)

    Для каждого индекса i из списка indexes:
        - берутся элементы arr1[i], arr2[i], arr3[i];
        - находится их сумма;
        - сумма возводится в степень минимального из трёх чисел.

    Параметры:
        :param arr1: первый массив чисел
        :param arr2: второй массив чисел
        :param arr3: третий массив чисел
        :param indexes: список индексов, для которых выполняется вычисление

    Возвращает:
        :return: список результатов возведения суммы в степень

    :raises OperationError: если ошибка вычисления
    """

    logger.info("Вызов power_of_sum()")
    results = []
    try:
        for i in indexes:
            a, b, c = arr1[i], arr2[i], arr3[i]
            results.append((a + b + c) ** min(a, b, c))
        return results
    except Exception as e:
        raise OperationError(f"Ошибка вычисления степени: {e}") from e


# меню для 2 задания
def task_2_menu() -> None:
    """
    Меню задачи 2:
    Работа с тремя массивами одинаковой длины.
    Поиск индексов, для которых сумма элементов первых двух массивов
    равна элементу третьего массива, и возведение суммы в степень.

    Пользователь может:
        1. Ввести три массива вручную.
        2. Сгенерировать три массива случайно.
        3. Найти индексы, где arr1[i] + arr2[i] == arr3[i],
           и возвести сумму элементов в степень минимального из них.
        4. Показать массивы и результаты вычислений.
        5. Выйти в главное меню.

    Взаимодействие с пользователем:
        Функция запрашивает ввод через input() и выводит информацию через print().

    Возвращаемое значение:
        :return: функция завершает работу при выборе выхода в главное меню.
    """

    arr1: list[int] | None = None
    arr2: list[int] | None = None
    arr3: list[int] | None = None
    results: list[int] | None = None
    msgs = Messages.TASK2

    while True:
        print("\n" + msgs.title)
        for option in msgs.menu:
            print(option)
        choice = input(msgs.prompt)
        logger.info(f"task2: выбран пункт {choice}")

        # ввод вручную 
        if choice == "1":
            try:
                size = int(input("Введите размер массивов: "))
                arr1 = input_array_manual(size)
                arr2 = input_array_manual(size)
                arr3 = input_array_manual(size)
                results = None
                logger.info("Массивы введены вручную")
            except AppError as e:
                logger.error(str(e))
                print(msgs.input_error)
            except ValueError as e:
                logger.error(str(e))
                print("Ошибка ввода числа:", e)


        # генерация массивов
        elif choice == "2":
            try:
                size = int(input("Введите размер массивов: "))
                arr1 = generate_array(size)
                arr2 = generate_array(size)
                arr3 = generate_array(size)
                results = None
                print("Первый массив:", arr1)
                print("Второй массив:", arr2)
                print("Третий массив:", arr3)
                logger.info("Массивы сгенерированы случайно")
            except AppError as e:
                logger.error(str(e))
                print(msgs.input_error)
            except ValueError as e:
                logger.error(str(e))
                print("Ошибка ввода числа:", e)


        # вычисление
        elif choice == "3":
            try:
                if arr1 is None or arr2 is None or arr3 is None:
                    raise DataNotSetError("Массивы не заданы")
                indexes = check_sum(arr1, arr2, arr3)
                if not indexes:
                    print("Нет индексов, где сумма первых двух чисел равна третьему.")
                    results = []
                else:
                    results = power_of_sum(arr1, arr2, arr3, indexes)
                    print("Вычисление выполнено.")
                    logger.info("Вычисление выполнено")
            except AppError as e:
                logger.error(str(e))
                print(msgs.no_data)


        # вывод
        elif choice == "4":
            if arr1 is None or arr2 is None or arr3 is None:
                print(msgs.no_data)
            else:
                print("Первый массив:", arr1)
                print("Второй массив:", arr2)
                print("Третий массив:", arr3)
                if results is not None:
                    print("Индексы:", check_sum(arr1, arr2, arr3))
                    print("Результаты:", results)
                    logger.info("Результаты показаны")

        # выход в главное меню
        elif choice == "5":
            logger.info("Возврат в главное меню")
            return

        # Отключение логирования
        elif choice == "6":
            logger.setLevel("CRITICAL")
            print("Логирование отключено")
            logger.critical("Установлен уровень CRITICAL")

        else:
            print(msgs.invalid_choice)
            logger.info("Неверный пункт меню task2")

# ГЛАВНОЕ МЕНЮ 
def main():
    while True:
        print("\nГЛАВНОЕ МЕНЮ")
        print("1. Задание 2")
        print("0. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            task_2_menu()
        elif choice == "0":
            print("Выход")
            break
        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    main()