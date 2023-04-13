#!/c/pythons/Python310/python.exe
"""
Таск проекта из книги "Byte of Python"

Создайте собственную программу «Адресная книга», работающую из командной строки и позволяющую просматривать,
добавлять, изменять, удалять или искать контактные данные ваших знакомых.
Кроме того, эта информация также должна сохраняться на диске для последующего доступа

author: Qu1nel
data: 24_12_2022

Python3.10+
"""

__author__ = 'Qu1nel'
__version__ = 1.0


import os
from pathlib import Path
from typing import NoReturn, Type

import dill

from core.Controller import Controller

from .supportive.State import State
from core import Core
from db.book_table import BookTable

from config import *


def read_address_book_from_local_file(path_to_database: Path | str) -> BookTable:
    """Читает базу данных контактов из файла если та существует, иначе создает новую."""

    if (isinstance(path_to_database, Path) and path_to_database.exists()) or \
            os.path.exists(path_to_database):
        with open(path_to_database, mode='rb') as file_database:
            _book = dill.load(file_database)
    else:
        _book: BookTable = BookTable()

    return _book


def main() -> NoReturn:
    state_program: State = State.INIT

    db: BookTable = read_address_book_from_local_file(SAVE_DB_PATH)
    while True:
        controller = Core.get_controller_by_state(state_program)
        controller_entity = controller(state=state_program, data=db)
        state_program = controller_entity.run()


if __name__ == '__main__':
    main()
