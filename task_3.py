import random
from logger import logger

# генерация случайных массивов с обработкой ошибок
def random_array(size, min_val=0, max_val=50):
    """
    Генерирует два массива случайных целых чисел одинакового размера.

    Параметры:
        :param size: количество элементов в каждом массиве
        :param min_val: минимальное возможное значение элемента (включительно)
        :param max_val: максимальное возможное значение элемента (включительно)

    Возвращает:
        :return:  кортеж из двух массивов (arr1, arr2)
    """

    logger.info("Генерация случайного массива")
    try:
        if size <= 0:
            raise ValueError("Размер массива должен быть положительным числом")
        arr1 = [random.randint(min_val, max_val) for _ in range(size)]
        arr2 = [random.randint(min_val, max_val) for _ in range(size)]
        return arr1, arr2

    except Exception as e:
        logger.error(f"Ошибка генерации массива: {e}")
        print("Ошибка генерации массива:", e)
        return [], []


# ручной ввода массивов с обработкой ошибок
def manual_input():
    """
    Выполняет ручной ввод двух массивов одинакового размера.

    Пользователь вводит размер массивов, затем элементы
    каждого массива через пробел. Если количество введённых
    элементов не совпадает с заданным размером, возникает ошибка.

    Возвращает:
        :return:  кортеж из двух массивов (arr1, arr2)

    Ошибки:
        :raises ValueError: если количество введённых чисел не совпадает с размером массивов
    """

    logger.info("Ввод массива вручную")
    try:
        size = int(input("Введите размер массивов: "))
        if size <= 0:
            raise ValueError("Размер массива должен быть положительным числом")

        arr1 = list(map(int, input("Введите элементы первого массива через пробел: ").split()))
        arr2 = list(map(int, input("Введите элементы второго массива через пробел: ").split()))

        if len(arr1) != size or len(arr2) != size:          # Проверка размера
            raise ValueError(f"Ошибка: нужно ввести {size} чисел, а введено {len(arr1)} и {len(arr2)}")

        return arr1, arr2

    except ValueError as ve:
        logger.error(f"Ошибка ввода: {ve}")
        print("Ошибка ввода:", ve)
        return [], []

    except Exception as e:
        logger.error(f"Неизвестная ошибка ввода: {e}")
        print("Произошла ошибка:", e)
        return [], []


# сортировка массивов по условиям
def sort_arrays(arr1, arr2):
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

    logger.info("Сортировка массивов по условию")
    try:
        arr1_sorted = sorted(arr1, reverse=True)   # убывание
        arr2_sorted = sorted(arr2)                 # возрастание
        return arr1_sorted, arr2_sorted
    except Exception as e:
        logger.error(f"Ошибка сортировки: {e}")
        print("Ошибка сортировки массивов:", e)
        return [], []


# правило сложения массивов
def sum_arrays(arr1, arr2):
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
    """

    logger.info("Сложение двух массивов по условию")
    try:
        if len(arr1) != len(arr2):
            raise ValueError("Массивы должны быть одинакового размера для сложения")
        result = [0 if a == b else a + b for a, b in zip(arr1, arr2)]
        return result # итог НЕ по возрастанию
    except Exception as e:
        logger.error(f"Ошибка сложения массивов: {e}")
        print("Ошибка сложения массивов:", e)
        return []


# меню для 3 задания с обработкой ошибок
def task_3_menu():
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

    arr1 = arr2 = arr1_sorted = arr2_sorted = result = None
    
    while True:
        print("\n===== ЗАДАНИЕ 3 =====")
        print("1. Ввести массивы вручную")
        print("2. Сгенерировать массивы случайно")
        print("3. Показать массивы и результат")
        print("4. Назад в главное меню")
        print("5. Отключить логирование (CRITICAL)")

        choice = input("Выберите пункт: ")
        logger.info(f"Пользователь выбрал пункт меню task_3: {choice}")

        # ручной ввод и преобразования
        if choice == "1":
            arr1, arr2 = manual_input()
            if arr1 and arr2:
                arr1_sorted, arr2_sorted = sort_arrays(arr1, arr2)
                result = sum_arrays(arr1_sorted, arr2_sorted)
                print("\nМассивы введены и обработаны.")
                logger.info("Массив введен вручную и преобразован")

        # генерация случайных массивов
        elif choice == "2":
            try:
                size = int(input("Введите размер массивов: "))
                arr1, arr2 = random_array(size)
                if arr1 and arr2:
                    arr1_sorted, arr2_sorted = sort_arrays(arr1, arr2)
                    result = sum_arrays(arr1_sorted, arr2_sorted)
                    print("\nМассивы сгенерированы и обработаны.")
                    logger.info("Массивы сгенерированы автоматически")
            except Exception as e:
                logger.error(f"Ошибка генерации массивов: {e}")
                print("Ошибка генерации массивов:", e)

        # результат и вывод
        elif choice == "3":
            try:
                if arr1 is None or arr2 is None:
                    raise RuntimeError("Массивы ещё не введены или не сгенерированы")
                print("\nПервый массив:", arr1)
                print("Второй массив:", arr2)
                print("Первый массив отсортированный:", arr1_sorted)
                print("Второй массив отсортированный:", arr2_sorted)
                print("Результат сложения:", sorted(result))
                logger.info("Вывод массивов и результата успешен")
            except Exception as e:
                logger.error(f"Ошибка при выводе: {e}")
                print("Ошибка:", e)

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
            print("Неверный выбор!")
            logger.info("Неверный пункт меню")


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