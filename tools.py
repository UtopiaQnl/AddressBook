import os
import sys
from time import sleep


def clear_console() -> None:
    """Очищает консоль."""
    os.system("cls||clear")


def exit_from_program() -> None:
    """Очищает консоль. Выходит из приложения, сообщая об этом в консоль.

    :return: None
    """
    clear_console()
    print("\nВы вышли из приложения. Удачного времени суток, пока!\n")
    sleep(2)
    clear_console()
    sys.exit()


def create_file(file_name: str) -> bool:
    """Создает файл с именем file_name.

    В случаи успешного создания файла возвращает True; False иначе.

    :param file_name: Имя создаваемого файла.
    :return: bool
    """
    f: IO | None = None
    try:
        f = open(file_name, 'tw')
    except Exception as exc:
        print(exc)

    if f is None:
        return False
    return True


def valid_name(string: str) -> bool:
    if not string.isalpha():
        print('Имя должно содержать только буквы!')
        sleep(2)
        return True
    return False


def valid_surname(string: str) -> bool:
    if not string.isalpha():
        print('Фамилия должно содержать только буквы!')
        sleep(2)
        return True
    return False


def valid_number_phone(string: str) -> bool:
    if string[0] != '+' or not string[1:].isdigit():
        print('Номер телефона должен начинаться с "+" и содержать только цифры без пробелов')
        sleep(2)
        return True
    return False


def valid_email(string: str) -> bool:
    if '@' not in string or '.' not in string or ' ' in string:
        print('Почта должна содержать "@" с точкой и без пробелов!')
        sleep(2)
        return True
    return False
