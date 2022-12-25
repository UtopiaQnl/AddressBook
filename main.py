"""
Таск из "Byte of Python"

Создайте собственную программу «Адресная книга», работающую из командной строки и позволяющую просматривать,
добавлять, изменять, удалять или искать контактные данные ваших знакомых.
Кроме того, эта информация также должна сохраняться на диске для последующего доступа

author: Qu1nel
data: 24_12_2022
"""

__author__ = 'Qu1nel'

import os
import sys
import pickle

from dataclasses import dataclass


@dataclass
class ContactAddress:
    pass


class ContactNotExists(Exception):
    pass


class Book(dict):
    pass


class MainCommandHandler:
    pass


def main() -> None:
    pass


if __name__ == '__main__':
    main()
