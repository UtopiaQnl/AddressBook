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
import sys
import pickle

from dataclasses import dataclass


@dataclass
class ContactAddress:
    name: str
    surname: str
    number_phone: str
    email: str


class ContactNotExists(Exception):
    def __init__(self, contact: ContactAddress):
        self.contact = contact

    def __str__(self):
        return f'Контакт {self.contact} не существует в телефонной книге!'


class Book(dict):
    """

    """
    __idx: int = 0

    def add_contact(self, contact: ContactAddress) -> None:
        pass

    def remove_contact(self, contact: ContactAddress) -> None:
        pass

    def edit_contact(self, contact: ContactAddress) -> None:
        pass

    def show_book(self) -> None:
        pass

    def search_contact(self) -> None:
        pass

    def _is_exists(self, contact: ContactAddress) -> bool:
        pass


class MainCommandHandler:
    def __init__(self, address_book: Book):
        self.core_address_book = address_book

    def run(self) -> None:
        pass


def main() -> None:
    pass


if __name__ == '__main__':
    main()
