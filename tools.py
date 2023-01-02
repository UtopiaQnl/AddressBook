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
