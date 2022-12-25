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

MAX_WIDTH_NAME = 20  # максимальная ширина для имени
MAX_WIDTH_SURNAME = 20  # максимальная ширина для фамилии
MAX_WIDTH_NUMBER_PHONE = 20  # максимальная ширина для номера телефона
MAX_WIDTH_EMAIL = 30  # максимальная ширина для электронной почты
MAX_WIDTH_ID = 5  # максимальная длина для id контакта
COUNT_CONTACTS_VIEW = 15  # кол-во показываемых контактов


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
    showing_page - Индекс страницы (для корректного вырисовывания книги в консоль)

    :methods:
        add_contact(contact: ContactAddress) - Добавляет экземпляр ContactAddress в книгу.
        remove_contact(contact: ContactAddress) - Удаляет экземпляр ContactAddress из книги.
        edit_contact() - Позволяет редактировать ContactAddress в книге.
        show_board() - Показывает пользователю телефонную книгу постранично.
        search_contact() - Ищет контакт в книге по 4 основным полям.
        _is_exists(contact: ContactAddress) - Предикат. Проверяет существует ли ContactAddress в книге.
    """

    __idx: int = 0
    showing_page: int = 1

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

        # Максимальная ширина таблицы (да-да, зависит от констант...можно и реальные размеры консоли взять)
        main_width_line = (6 + MAX_WIDTH_SURNAME + MAX_WIDTH_NUMBER_PHONE +
                           MAX_WIDTH_EMAIL + MAX_WIDTH_ID + MAX_WIDTH_NAME)
        main_line = '-' * main_width_line  # В отдельной переменной, чтобы по много раз не высчитывать строку

        header = {
            '№': MAX_WIDTH_ID,
            'Имя': MAX_WIDTH_NAME,
            'Фамилия': MAX_WIDTH_SURNAME,
            'Телефон': MAX_WIDTH_NUMBER_PHONE,
            'Почта': MAX_WIDTH_EMAIL
        }

        def _draw_header() -> None:
            """Рисует шапку таблицы (заголовки)."""
            print(main_line)
            for title, width in header.items():
                print('|' + title.center(width), end='')
            print('|')
            print(main_line)

        def _draw_body() -> None:
            """Рисует тело таблицы, т.е. все контакты."""

            # Диапазон вырисовываемых контактов
            finish_range = COUNT_CONTACTS_VIEW * self.showing_page
            start_range = finish_range - COUNT_CONTACTS_VIEW

            for idx in range(start_range, finish_range):
                block_id = '|' + str(idx + 1).center(header['№'])
                print(block_id, end='')

                if self.get(idx) is None:  # Если контакта нет
                    print('|' + '...'.center(header['Имя']) +
                          '|' + '...'.center(header['Фамилия']) +
                          '|' + '...'.center(header['Телефон']) +
                          '|' + '...'.center(header['Почта']) + '|')
                else:
                    block_name = '|' + self[idx].name.center(header['Имя'])
                    block_surname = '|' + self[idx].surname.center(header['Фамилия'])
                    block_phone = '|' + self[idx].number_phone.center(header['Телефон'])
                    block_email = '|' + self[idx].email.center(header['Почта'])

                    print(block_name + block_surname + block_phone + block_email, end='|\n')

        def _draw_floor() -> None:
            """Рисует низ таблицы контактов. + Показывает на какой страницы сейчас."""
            print(main_line)
            info = f' Страница {self.showing_page}'
            print(f'|{info}' + ' ' * (main_width_line - len(info) - 2), end='|\n')
            print(main_line)

        _draw_header()
        _draw_body()
        _draw_floor()

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
        os.system("cls||clear")  # Перед работой приложения, нужно очистить консоль - так лучше
        while True:
            self.welcome()  # Приветствие пользователя с выводом возможных команд

            user_answer: str = input('$_> ')  # корректный ввод: 0..5, add, remove, show, search, edit, exit

            match user_answer:
                # Добавить контакт в телефонную книгу
                case '1' | 'add' | 'a':
                    # TODO добавить "добавление" контакта в книгу. Отдельное окно.
                    os.system("cls||clear")  # TEMP
                    print("...добавление контакта (1)")

                # Показать телефонную книгу пользователю
                case '2' | 'show' | 'sh' | 's':
                    self.board_display_interface()

                # Удалить контакт из телефонной книги
                case '3' | 'remove' | 'rem' | 'rm' | 'r':
                    # TODO дать выбрать пользователю тот контакт, который он возможно удалит.
                    os.system("cls||clear")  # TEMP
                    print("...показ контактов, с последующим возможным удалением одного из них (3)")

                # Редактировать контакт в телефонной книге
                case '4' | 'edit' | 'ed':
                    # TODO дать выбрать пользователю тот контакт, который он возможно будет редактировать.
                    os.system("cls||clear")  # TEMP
                    print("...показ контактов, с последующим возможным редактированием одного их них (4)")

                # Искать контакт в телефонной книге
                case '5' | 'search' | 'sr':
                    # TODO в отдельном окне запросить ввод одного из 4-ёх полей контакта с последующим поиском в книге
                    os.system("cls||clear")  # TEMP
                    print("...отдельное окно с вводом одно из 4-ёх полей контакта, с последующим поиском в книге (5)")

                # Выйти из приложения
                case '0' | 'exit' | 'ex' | 'e':
                    exit_from_program()

                case _:
                    os.system("cls||clear")

    def board_display_interface(self) -> None:
        """Обертка для Book.show_book. Позволяет перелистывать книгу.

        :return: None
        """
        while True:
            os.system("cls||clear")  # Очистить консоль - дело святое

            self.core_address_book.show_book()  # Основная функция отрисовки таблицы*

            print("1 - Следующая страница.\t(n)ext\n2 - Предыдущая страница.\t(p)revius\n0 - Выход (e)xit\n")
            answer = input("$_> ")
            match answer:
                # Следующая страница
                case '1' | 'next' | 'n':
                    self.core_address_book.showing_page += 1

                # Предыдущая страница
                case '2' | 'prev' | 'pr' | 'p':
                    if (diff := self.core_address_book.showing_page - 1) < 1:  # чтобы не уйти в отрицательные числа
                        self.core_address_book.showing_page = 1
                    else:
                        self.core_address_book.showing_page = diff

                # Выход в главное меню
                case '0' | 'exit' | 'e':
                    os.system("cls||clear")  # Нужно очистить, т.к. в главном меню - главное меню, а не таблица
                    break

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


def exit_from_program() -> None:
    """Очищает консоль. Выводит сообщение о выходе их приложения. Выходит из приложения.

    :return: None
    """
    os.system("cls||clear")  # Очистка консоли где бы не был пользователь - так лучше.
    print("\nВы вышли из приложения. Удачного времени суток, пока!\n")
    sys.exit()


def main() -> None:
    main_book = Book()

    program = MainCommandHandler(address_book=main_book)
    try:
        program.run()
    except KeyboardInterrupt:
        exit_from_program()


if __name__ == '__main__':
    main()
