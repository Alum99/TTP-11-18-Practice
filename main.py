from logger import logger
from task_1 import task_1_menu
from task_2 import task_2_menu
from task_3 import task_3_menu
from messages import Messages

"""
Главный модуль программы.
Обеспечивает интерфейс верхнего уровня и доступ к отдельным заданиям.
"""   

def main() -> None:
    """
    Запускает главное меню программы.

    Пользователь может выбрать одно из трёх заданий или завершить работу.
    Функция работает в цикле, пока пользователь явно не завершит программу.
    Взаимодействует с пользователем через консоль.
    Все действия пользователя логируются с помощью ``logger``.

    task_1_menu : Меню задания 1 (Подсчет общих чисел).
    task_2_menu : Меню задания 2 (Поиск индексов при условии).
    task_3_menu : Меню задания 3 (Сложение и сортировка массивов).
    """

    msgs = Messages.MENU_MAIN

    while True:
        print("\n" + msgs.title)
        for option in msgs.options:
            print(option)

        choice = input(msgs.prompt)
        logger.info(f"Пользователь выбрал главный пункт меню: {choice}")

        if choice == "1":
            task_1_menu()

        elif choice == "2":
            task_2_menu()

        elif choice == "3":
            task_3_menu()

        elif choice == "4":
            print(msgs.exit)
            logger.info("Пользователь завершил программу")
            break

        elif choice == "0":
            print("Выход...")
            break

        else:
            print(msgs.invalid_choice)
            logger.info("Ошибка: неверный пункт главного меню")


if __name__ == "__main__":
    main()