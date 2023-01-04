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

import os
import pickle

from command_handler import MainCommandHandler
from contact_address import ContactAddress
from book import Book

from tools import exit_from_program, create_file
from config import *


def read_address_book_from_file() -> Book:
    """Читает базу данных контактов из файла если та существует, иначе создает новую.

    :return: Book
    """
    if os.path.exists(SAVE_FILE_NAME):
        if os.path.getsize(SAVE_FILE_NAME) == 0:
            book: Book = Book()
        else:
            with open(SAVE_FILE_NAME, 'rb') as file_address_book:
                book: Book = Book(pickle.load(file_address_book))
    else:
        book: Book = Book()
        if create_file(SAVE_FILE_NAME) is False:
            print("ОШИБКА! НЕ УДАЛОСЬ СОЗДАТЬ БАЗУ ДАННЫХ КОНТАКТОВ...")
            exit_from_program()

    return book


def main() -> None:
    main_book: Book = read_address_book_from_file()

    program: MainCommandHandler = MainCommandHandler(address_book=main_book)
    try:
        program.run()
    except KeyboardInterrupt:
        exit_from_program()


if __name__ == '__main__':
    main()
