import random
from logger import logger

# генератор случайных массивов с параметрами по умолчанию
def generate_array(size, min_val=0, max_val=50):
    """
    Генерирует массив случайных целых чисел заданного размера.

    Параметры:
        :param size: количество элементов в массиве.
        :param min_val: минимальное возможное значение элемента (включительно), по умолчанию 0.
        :param max_val: максимальное возможное значение элемента (включительно), по умолчанию 50.

    Возвращает:
        :return: список случайных целых чисел длиной size.
    """
    
    logger.info("Генерация случайного массива")
    try:
        if size <= 0:
            raise ValueError("Размер массива должен быть положительным")
        return [random.randint(min_val, max_val) for _ in range(size)]
    except Exception as e:
        logger.error(f"Ошибка генерации массива: {e}")
        print("Ошибка генерации массива:", e)
        return []


# ручной ввод
def input_array_manual(size):
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
        :raises ValueError: если количество введённых чисел не совпадает с size.
    """

    logger.info("Ввод массива вручную")
    try:
        if size <= 0:
            raise ValueError("Размер массива должен быть положительным")
        arr = list(map(int, input(f"Введите {size} чисел через пробел: ").split()))   # f-строка для динамической подстановки значения size
        if len(arr) != size:                                                          # проверка размера массива
            raise ValueError(f"Количество введённых чисел ({len(arr)}) не совпадает с заданным размером ({size})")
        return arr                                                                    # возвращает введенный массив чисел
    except ValueError as ve:
        logger.error(f"Ошибка ввода: {ve}")
        print("Ошибка ввода:", ve)
        return []


# Для найденных индексов (из check_sum.py)
def power_of_sum(arr1, arr2, arr3, indexes):
    """
    Вычисляет значения (a + b + c) ** min(a, b, c)
    для элементов массивов по заданным индексам.

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
    """
    
    logger.info("Вызов power_of_sum()")
    results = []
    try:
        for i in indexes:
            a, b, c = arr1[i], arr2[i], arr3[i]
            total = a + b + c                       # суммируем 3 числа
            power = min(a, b, c)                    # находим наименьшее
            results.append(total ** power)          # возводим в степень
        return results                              # возвращает список значений
    except Exception as e:
        logger.error(f"Ошибка в power_of_sum: {e}")
        print("Ошибка вычисления степени:", e)
        return []


# Возвращает список индексов, где arr1[i] + arr2[i] == arr3[i]
def check_sum(arr1, arr2, arr3):                     # принимает три массива одинаковой длины
    """
    Находит индексы элементов массивов, для которых
    выполняется условие arr1[i] + arr2[i] == arr3[i].

    Все три массива должны быть одинаковой длины.

    Параметры:
        :param arr1: первый массив чисел
        :param arr2: второй массив чисел
        :param arr3: третий массив чисел

    Возвращает:
        :return: список индексов, удовлетворяющих условию
    """
    
    logger.info("Вызов check_sum()")
    try:
        if not (len(arr1) == len(arr2) == len(arr3)):
            raise ValueError("Все массивы должны быть одинаковой длины")
        result_indexes = []                              # для хранения индексов
        for i in range(len(arr1)):
            if arr1[i] + arr2[i] == arr3[i]:
                result_indexes.append(i)                 # список результатов
        return result_indexes
    except Exception as e:
        logger.error(f"Ошибка в check_sum: {e}")
        print("Ошибка поиска индексов:", e)
        return []


# меню для 2 задания с обработкой ошибок
def task_2_menu():
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
    
    arr1 = arr2 = arr3 = None
    results = None

    while True:
        print("\n===== ЗАДАНИЕ 2 =====")
        print("1. Ввести массивы вручную")
        print("2. Сгенерировать массивы случайно")
        print("3. Найти индексы и возвести суммы в степень")
        print("4. Показать массивы и результаты")
        print("5. Назад в главное меню")
        print("6. Отключить логирование (CRITICAL)")

        choice = input("Выберите пункт: ")
        logger.info(f"Пользователь выбрал пункт меню task_2: {choice}")

        # ввод вручную 
        if choice == "1":
            try:
                size = int(input("Введите размер массивов: "))
                arr1 = input_array_manual(size)
                arr2 = input_array_manual(size)
                arr3 = input_array_manual(size)
                if not arr1 or not arr2 or not arr3:
                    raise RuntimeError("Ввод массивов не удался")
                results = None
                logger.info("Массив введен вручную")
            except Exception as e:
                logger.error(f"Ошибка ручного ввода: {e}")
                print("Ошибка ручного ввода:", e)


        # случайная генерация
        elif choice == "2":
            try:
                size = int(input("Введите размер массивов: "))
                arr1 = generate_array(size)
                arr2 = generate_array(size)
                arr3 = generate_array(size)
                if not arr1 or not arr2 or not arr3:
                    raise RuntimeError("Генерация массивов не удалась")
                print("Первый массив:", arr1)
                print("Второй массив:", arr2)
                print("Третий массив:", arr3)
                results = None
                logger.info("Массивы сгенерированы автоматически")
            except Exception as e:
                logger.error(f"Ошибка генерации массивов: {e}")
                print("Ошибка генерации массивов:", e)


        # вычисление
        elif choice == "3":
            try:
                if arr1 is None or arr2 is None or arr3 is None:
                    raise RuntimeError("Сначала введите или сгенерируйте массивы!")
                indexes = check_sum(arr1, arr2, arr3)
                if not indexes:
                    print("Нет индексов, где сумма первых двух чисел равна третьему.")
                    results = []
                else:
                    results = power_of_sum(arr1, arr2, arr3, indexes)
                    print("Подсчёт выполнен.")
                    logger.info("Подсчёт выполнен")
            except Exception as e:
                logger.error(f"Ошибка вычисления: {e}")
                print("Ошибка вычисления:", e)


        # вывод
        elif choice == "4":
            try:
                if arr1 is None or arr2 is None or arr3 is None:
                    raise RuntimeError("Массивы ещё не заданы")
                print("\nПервый массив: ", arr1)
                print("Второй массив: ", arr2)
                print("Третий массив: ", arr3)
                if results is not None:
                    print("Индексы: ", check_sum(arr1, arr2, arr3))
                    print("Результаты возведения суммы в степень:", results)
            except Exception as e:
                logger.error(f"Ошибка вывода: {e}")
                print("Ошибка вывода:", e)

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
            print("Неверный выбор!")
            logger.info("Неверный пункт меню")

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