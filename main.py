#!/c/pythons/Python310/python.exe
"""
Таск из "Byte of Python"

Создайте собственную программу «Адресная книга», работающую из командной строки и позволяющую просматривать,
добавлять, изменять, удалять или искать контактные данные ваших знакомых.
Кроме того, эта информация также должна сохраняться на диске для последующего доступа

author: Qu1nel
data: 24_12_2022

Python3.10+
"""

__author__ = 'Qu1nel'

from command_handler import MainCommandHandler
from contact_address import ContactAddress
from book import Book

from tools import exit_from_program


def main() -> None:
    main_book = Book()

    program = MainCommandHandler(address_book=main_book)
    try:
        program.run()
    except KeyboardInterrupt:
        exit_from_program()


if __name__ == '__main__':
    main()
