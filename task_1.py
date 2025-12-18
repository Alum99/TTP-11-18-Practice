import random
from logger import logger
from messages import Messages
from exceptions import InputError, InvalidValueError, DataNotSetError, OperationError, AppError


# Генерирует массив случайных чисел
def generate_array(size: int, min_v: int = 0, max_v: int = 50) -> list[int]: # аннотация возвращаемого значения
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
    if size <= 0:
        raise InvalidValueError("Размер массива должен быть положительным") # некорректные значения
    return [random.randint(min_v, max_v) for _ in range(size)]


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
    raw = input("Введите числа через пробел: ")
    if not raw.strip():
        raise InputError("Пустой ввод")  # Ошибка ввода пользователем.
    try:
        return [int(x) for x in raw.split()]
    except ValueError:
        raise InputError("Введены нецелые числа") # Ошибка ввода пользователем.


# Возвращает число, записанное в обратном порядке цифр
def reverse_number(n: int) -> int:
    """
    Возвращает число, записанное в обратном порядке цифр.

    Параметры:
        :param n: исходное целое число.

    Возвращает:
        :return: число с перевернутым порядком цифр.
    """

    result = int(str(n)[::-1])
    logger.debug(f"reverse_number: {n} -> {result}")   # вспомогательная функция, не засоряет лог
    return result


# количество общих чисел в двух массивах
def count_common_and_reversed(arr1: list[int], arr2: list[int]) -> int:
    """
    Подсчитывает количество общих чисел между двумя массивами,
    учитывая также перевёрнутые значения.

    Каждая пара чисел учитывается только один раз,
    даже если такие значения встречаются несколько раз в массивах.

    :param arr1: первый массив целых чисел
    :param arr2: второй массив целых чисел
    :return: количество уникальных общих чисел между массивами

    :raises EmptyArrayError:
        если один или оба массива пустые
    :raises OperationError:
        если возникает ошибка при выполнении подсчёта
    """

    if not arr1 or not arr2:
        raise DataNotSetError("Массивы не заданы или пусты") # Ошибка при попытке работы с данными, которые ещё не заданы

    count = 0
    used_pairs = []

    try:
        for a in arr1:
            for b in arr2:
                if a == b or a == reverse_number(b) or reverse_number(a) == b:
                    pair = (min(a, b), max(a, b))
                    if pair not in used_pairs:
                        used_pairs.append(pair)
                        count += 1
    except Exception as e:
        raise OperationError(f"Ошибка выполнения подсчёта: {e}") from e  # Ошибка выполнения операции.

    return count


# меню для задания 1: общие числа в двух массивах
def task_1_menu() -> None:
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
    msgs = Messages.TASK1 # Сохраняет ссылку на класс из файла messages.py

    while True:
        print("\n" + msgs.title) # вывод заголовка меню
        for option in msgs.menu: # вывод всех пунктов меню, msgs.menu — список строк с пунктами меню
            print(option)

        choice = input(msgs.prompt)   # msgs.prompt — строка с приглашением "Выберите пункт: "
        logger.info(f"task1: выбран пункт {choice}")

        # ввод вручную
        if choice == "1":
            try:
                print("Первый массив:")
                arr1 = input_array_manual()
                print("Второй массив:")
                arr2 = input_array_manual()
                result = None
                logger.info("Массивы введены вручную")
            except AppError as e:
                logger.error(str(e))
                print(msgs.input_error)


        # генерация массивов
        elif choice == "2":
            try:
                size1 = int(input("Размер первого массива: "))
                size2 = int(input("Размер второго массива: "))
                arr1 = generate_array(size1)
                arr2 = generate_array(size2)
                print("Первый массив:", arr1)
                print("Второй массив:", arr2)
                result = None
                logger.info("Массивы сгенерированы случайно")
            except AppError as e:
                logger.error(str(e))
                print(msgs.input_error)


        # вычисление
        elif choice == "3":
            try:
                if arr1 is None or arr2 is None:
                    raise DataNotSetError("Массивы не заданы")

                result = count_common_and_reversed(arr1, arr2)
                msgs = Messages.TASK1
                logger.info("Подсчёт выполнен")
            except AppError as e:
                logger.error(str(e))
                print(msgs.no_data)


        # вывод результата
        elif choice == "4":
            if result is None:
                print(msgs.no_data)
            else:
                print(f"Результат: {result}")
                logger.info("Результат показан")

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
            print(msgs.invalid_choice)
            logger.info("Неверный пункт меню task1")


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