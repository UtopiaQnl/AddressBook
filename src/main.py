"""
Таск проекта из книги "Byte of Python"

Создайте собственную программу «Адресная книга», работающую из командной строки и позволяющую просматривать,
добавлять, изменять, удалять или искать контактные данные ваших знакомых.
Кроме того, эта информация также должна сохраняться на диске для последующего доступа

author: Qu1nel
data: 24_12_2022

Python3.10+
"""
import os
from pathlib import Path
from typing import NoReturn, Type

import dill

from core import Core
from core.Controller import Controller

from supportive.State import State
from db.book_table import BookTable

from config import *


def path_exists(path: Path | str) -> bool:
    return (isinstance(path, Path) and path.exists()) or os.path.exists(path)


def read_address_book_from_local_file(path_to_database: Path | str) -> BookTable:
    if path_exists(path_to_database):
        with open(path_to_database, mode='rb') as file_database:
            book = dill.load(file_database)
    else:
        book: BookTable = BookTable()

    return book


def main() -> NoReturn:
    state_program: State = State.INIT

    db: BookTable = read_address_book_from_local_file(SAVE_DB_PATH)
    while True:
        controller: Type[Controller] = Core.get_controller_by_state(state_program)
        controller_entity = controller(state=state_program, data=db)
        state_program = controller_entity.run()


if __name__ == '__main__':
    main()
