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
    """Телефонная книга (словарь) для адресов людей.

    __idx - Указатель на следующее место в книге

    :methods:
        add_contact(contact: ContactAddress) - Добавляет экземпляр ContactAddress в книгу.
        remove_contact(contact: ContactAddress) - Удаляет экземпляр ContactAddress из книги.
        edit_contact() - Позволяет редактировать ContactAddress в книге.
        show_board() - Показывает пользователю телефонную книгу постранично.
        search_contact() - Ищет контакт в книге по 4 основным полям.
        _is_exists(contact: ContactAddress) - Предикат. Проверяет существует ли ContactAddress в книге.
    """

    __idx: int = 0

    def add_contact(self, contact: ContactAddress) -> None:
        """Добавляет contact в телефонную книгу.

        :param contact: Экземпляр класс ContactAddress
        :raise TypeError: Если contact не является экземпляром класс ContactAddress
        :return: None
        """

    def remove_contact(self, contact: ContactAddress) -> None:
        """Удаляет contact из телефонной книги.

        :param contact: Экземпляр класс ContactAddress
        :raise TypeError: Если contact не является экземпляром класс ContactAddress
        :raise ContactNotExists: Если contact не найден в телефонной книге
        :return: None
        """
        pass

    def edit_contact(self, contact: ContactAddress) -> None:
        pass

    def show_book(self) -> None:
        """Рисует телефонную книгу в консоли. В 3 этапа. Заголовок, тело и низ.

        :return: None
        """
        pass

    def search_contact(self) -> None:
        pass

    def _is_exists(self, contact: ContactAddress) -> bool:
        """ Предикат. Возвращает True если contact существует в книге, False иначе.

        :param contact: Экземпляр класс ContactAddress
        :return: bool[True, False]
        """
        pass


class MainCommandHandler:
    """Класс-обработчик пользовательских команд телефонной книги в консоли.

    :methods:
        run() - Запуск приложения, с дальнейшим развитием действий.
    """

    def __init__(self, address_book: Book):
        self.core_address_book = address_book

    def run(self) -> None:
        """Запускает приложение. Отлавливает начальные команды пользователя.

        1 | add - добавить контакт.

        2 | show - показать телефонную книгу.

        3 | remove - удалить контакт из книги.

        4 | edit - редактировать контакт в книге.

        5 | search - найти контакт в книге.

        0 | exit - выйти из приложения.

        :return: None
        """
        while True:
            os.system("cls||clear")  # Перед работой приложения, нужно очистить консоль - так лучше

            self.welcome()

            user_answer: str = input('$_> ')  # корректный ввод: 0..5, add, remove, show, search, edit, exit

            match user_answer:
                # Добавить контакт в телефонную книгу
                case '1' | 'add' | 'a':
                    pass

                # Показать телефонную книгу пользователю
                case '3' | 'show' | 'sh' | 's':
                    pass

                # Удалить контакт из телефонной книги
                case '3' | 'remove' | 'rem' | 'rm' | 'r':
                    pass

                # Редактировать контакт в телефонной книге
                case '4' | 'edit' | 'ed':
                    pass

                # Искать контакт в телефонной книге
                case '5' | 'search' | 'sr':
                    pass

                # Выйти из приложения
                case '0' | 'exit' | 'ex' | 'e':
                    pass

    @staticmethod
    def welcome() -> None:
        """Приветствует пользователя, выводя все инструкции и лого приложения.

        :return: None
        """
        logo = ("             _     _                     ____              _" + '\n' +
                r"    /\      | |   | |                   |  _ \            | |" + '\n' +
                r"   /  \   __| | __| |_ __ ___  ___ ___  | |_) | ___   ___ | | __" + '\n' +
                r"  / /\ \ / _` |/ _` | '__/ _ \/ __/ __| |  _ < / _ \ / _ \| |/ /" + '\n' +
                r" / ____ \\(_| | (_| | |  | __/\__ \__ \ | |_) | (_) | (_) |   <" + '\n' +
                "/_/    \\_\\\\___|\\____|_|  \\___||___/___/ |____/ \\___/ \\___/|_|\\_\\" + '\n' +
                r"Made by Qu1nel")

        print(logo)
        print('Приложение "Телефонная книга"\nАвтор: Qui1nel\n\nДля работы с приложением следуете инструкциям ниже.\n')
        print("1 - Добавить контакт в книгу.\t\t (a)dd\n2 - Показать телефонную книгу\t\t (s)how")
        print("3 - Удалить контакт из книги.\t\t (r)emove\n4 - Редактировать контакт в книге.\t (ed)it")
        print("5 - Найти контакт в книге.\t\t (sr)earch\n0 - Выйти из приложения.\t\t (e)xit\n")


def main() -> None:
    main_book = Book()

    program = MainCommandHandler(address_book=main_book)
    program.run()


if __name__ == '__main__':
    main()
