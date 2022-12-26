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

from time import sleep
from datetime import datetime
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
    time_create: datetime

    def pprint_info(self) -> None:
        """Красиво выводит информацию о контакте."""
        print(f"\nКОНТАКТ\t- дата создания: {datetime.strftime(self.time_create, '%H:%M %d.%m.%Y')}\n")
        print(f"1. Имя\t\t\t-\t{self.name}")
        print(f"2. Фамилия\t\t-\t{self.surname}")
        print(f"3. Номер телефона\t-\t{self.number_phone}")
        print(f"4. Электронная почта\t-\t{self.email}\n")

    def change_name(self) -> None:
        """Отдельное окно. Позволяет изменить имя (name)."""
        while True:
            clear_console()
            print("\nВведите новое имя")
            new_name = input("$_> ").capitalize()

            if not new_name:
                print("Вы ввели пустое имя. Изменения не засчитаны...")
                sleep(1)
                break
            elif len(new_name) >= MAX_WIDTH_NAME:
                print("Вы ввели слишком длинное имя. Изменения не засчитаны...")
                sleep(1)
                break

            self.name = new_name
            break

    def change_surname(self) -> None:
        """Отдельное окно. Позволяет изменить фамилию (surname)."""
        while True:
            clear_console()
            print("\nВведите новую фамилию")
            new_surname = input("$_> ").capitalize()

            if not new_surname:
                print("Вы ввели пустую фамилию. Изменения не засчитаны...")
                sleep(1)
                break
            elif len(new_surname) >= MAX_WIDTH_SURNAME:
                print("Вы ввели слишком длинную фамилию. Изменения не засчитаны...")
                sleep(1)
                break

            self.surname = new_surname
            break

    def change_number_phone(self) -> None:
        """Отдельное окно. Позволяет изменить номер телефона (number_phone)."""
        pass

    def change_email(self) -> None:
        """Отдельное окно. Позволяет изменить почту (email)."""
        pass


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
        if not isinstance(contact, ContactAddress):
            raise TypeError("Добавлять в книгу можно только контакты человека!")

        # TODO сделать проверку на то, существует ли уже такой же контакт, реализовать соответственное исключение, обработать его где оно может выброситься

        self[Book.__idx] = contact
        Book.__idx += 1

    def remove_contact(self, contact: ContactAddress) -> None:
        """Удаляет contact из телефонной книги.

        :param contact: Экземпляр класс ContactAddress
        :raise TypeError: Если contact не является экземпляром класс ContactAddress
        :raise ContactNotExists: Если contact не найден в телефонной книге
        :return: None
        """
        pass

    def edit_contact(self, contact: ContactAddress) -> None:
        """Редактирует contact в книге. Не проверяет наличие contact в книге.

        :param contact: ContactAddress
        :return: None
        """
        # TODO сделать сохранения изменений, т.е. сохранять ли изменения, показывая что было до изменений. В таком случаи нужно менять contact.pprint_info(something запихнуть) -> .copy()
        while True:
            clear_console()
            print("\nМЕНЮ РЕДАКТИРОВАНИЯ КОНТАКТА\n")

            contact.pprint_info()

            print("\nЧто вы можете сделать:\n")

            print("1 - Изменить Имя. (N)ame\n2 - Изменить Фамилию. (S)urname")
            print("3 - Изменить Номер телефона. (P)hone\n4 - Изменить почту. (E)mail\n0 - Выход. (e)xit\n")

            user_answer = input("$_> ").lower()
            match user_answer:
                case '1' | 'имя' | 'name' | 'N' | 'n':
                    contact.change_name()
                case '2' | 'фамилия' | 'surname' | 'S':
                    contact.change_surname()
                case '3' | 'телефон' | 'номер' | 'phone' | 'P':
                    contact.change_number_phone()
                case '4' | 'почта' | 'email' | 'E':
                    contact.change_email()
                case '0' | 'exit' | 'e':
                    clear_console()
                    break

    def show_book(self) -> None:
        """Рисует телефонную книгу в консоли. В 3 этапа. Заголовок, тело и низ.

        :return: None
        """
        header = {
            '№': MAX_WIDTH_ID,
            'Имя': MAX_WIDTH_NAME,
            'Фамилия': MAX_WIDTH_SURNAME,
            'Телефон': MAX_WIDTH_NUMBER_PHONE,
            'Почта': MAX_WIDTH_EMAIL
        }

        count_field_separators = len(header) + 1
        main_width_line = sum((count_field_separators, MAX_WIDTH_SURNAME, MAX_WIDTH_NUMBER_PHONE,
                               MAX_WIDTH_EMAIL, MAX_WIDTH_ID, MAX_WIDTH_NAME))
        main_line = '-' * main_width_line

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
            count_contacts = f'Всего контактов в книге {len(self)}'
            print(f'|{info} {" " * (main_width_line - len(info) - len(count_contacts) - 4)}{count_contacts} |')
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
        clear_console()
        while True:
            self.welcome()  # Приветствие пользователя с выводом возможных команд

            user_answer: str = input('$_> ')  # корректный ввод: 0..5, add, remove, show, search, edit, exit

            match user_answer:
                # Добавить контакт в телефонную книгу
                case '1' | 'add' | 'a':
                    self.interface_adding_contact()

                # Показать телефонную книгу пользователю
                case '2' | 'show' | 'sh' | 's':
                    self.board_display_interface()

                # Удалить контакт из телефонной книги
                case '3' | 'remove' | 'rem' | 'rm' | 'r':
                    # TODO дать выбрать пользователю тот контакт, который он возможно удалит.
                    clear_console()  # TEMP
                    print("...показ контактов, с последующим возможным удалением одного из них (3)")

                # Редактировать контакт в телефонной книге
                case '4' | 'edit' | 'ed':
                    self.interface_editing_contact()

                # Искать контакт в телефонной книге
                case '5' | 'search' | 'sr':
                    # TODO в отдельном окне запросить ввод одного из 4-ёх полей контакта с последующим поиском в книге
                    clear_console()  # TEMP
                    print("...отдельное окно с вводом одно из 4-ёх полей контакта, с последующим поиском в книге (5)")

                # Выйти из приложения
                case '0' | 'exit' | 'ex' | 'e':
                    exit_from_program()

                case _:
                    clear_console()

    def interface_adding_contact(self) -> None:
        """Обертка для Book.add_contact. Позволяет добавлять контакты в книгу.

        :return: None
        """
        clear_console()

        def _print_title() -> None:
            print("Вы находитесь в меню ввода нового контакта в телефонную книгу. Следуйте инструкциям ниже.\n")

            print("У вас будут запрошены 4 поля для контакта.\nВведите их и подтвердите введенные данные.")
            print('И тогда контакт будет в телефонной книге.')
            print('В будущем вы сможете его удалить  или редактировать по мере необходимости...\n')

        def valid_field(info_string: tuple[str, str], max_length: int) -> str:
            """Проверяет введенные пользователи строки на длину (проверяет валидность)

            :param info_string: tuple[str, str]. 2-е строки. 1 - для того, что должен ввести пользователь. 2 - если валидность провалена.
            :param max_length: int. Число, обозначающее максимальную длину введённой стоки пользователем.
            :return: str. Введённая строка пользователем.
            """
            while True:
                _print_title()
                print(info_string[0])
                var = input("$_> ").capitalize()
                if len(var) > max_length:
                    print('\n', info_string[1])
                    sleep(3)
                    clear_console()
                    continue
                clear_console()
                return var

        make_contact_status: bool = False

        while not make_contact_status:
            name: str = valid_field(
                info_string=("Введите имя для контакта:", "Слишком длинное имя! Введите имя по короче."),
                max_length=MAX_WIDTH_NAME
            )

            surname: str = valid_field(
                info_string=("Введите фамилию для контакта:", "Слишком длинная фамилия! Введите фамилию по короче."),
                max_length=MAX_WIDTH_SURNAME
            )

            number_phone: str = valid_field(
                info_string=("Введите имя номер телефона контакта:", "Слишком длинный номер! Введите номер по короче."),
                max_length=MAX_WIDTH_NUMBER_PHONE
            )

            email: str = valid_field(
                info_string=("Введите почту контакта:", "Слишком длинная почта! Введите почту по короче."),
                max_length=MAX_WIDTH_EMAIL
            )

            while True:
                clear_console()
                print("Вы только что ввели данные для контакта:\n")
                print(f"\tИмя\t\t-\t'{name}'\n\tФамилия\t\t-\t'{surname}'"
                      f"\n\tНомер телефона\t-\t'{number_phone}'\n\tПочта\t\t-\t'{email}'\n")

                print("Всё верно введено?\n")

                print("1 - Да.\t (y)es\n2 - Нет. (n)o\n0 - Выйти в главное меню. (e)xit\n")

                user_answer: str = input("$_> ").lower()
                match user_answer:
                    case '1' | 'да' | 'yes' | 'y':  # Всё что ввел пользователь верно - создается новый контакт и выход из цикла
                        make_contact_status = True

                        new_contact: ContactAddress = ContactAddress(
                            name=name,
                            surname=surname,
                            number_phone=number_phone,
                            email=email,
                            time_create=datetime.today()
                        )
                        self.core_address_book.add_contact(contact=new_contact)

                        clear_console()

                        print("\nКонтакт успешно сохранен!\n")
                        sleep(2)
                        break

                    case '2' | 'нет' | 'no' | 'n':  # Просто очищается консоль, и всё запрашивать по новой
                        clear_console()
                        break

                    case '0' | 'выход' | 'exit' | 'e':
                        make_contact_status = True
                        break

        clear_console()
        print()
        for i in range(3, 0, -1):
            print(f"Выход в главное меню через {i} сек...", end='\r\b')
            sleep(1)

        clear_console()

    def board_display_interface(self) -> None:
        """Обертка для Book.show_book. Позволяет перелистывать книгу.

        :return: None
        """
        while True:
            clear_console()

            self.core_address_book.show_book()  # Основная функция отрисовки таблицы*

            print("\n1 - Следующая страница.\t\t(n)ext\n2 - Предыдущая страница.\t(p)revious\n0 - Выход\t\t\t(e)xit\n")
            user_answer = input("$_> ")
            match user_answer:
                # Следующая страница
                case '1' | 'next' | 'n':
                    self.core_address_book.showing_page += 1

                # Предыдущая страница
                case '2' | 'previous' | 'prev' | 'pr' | 'p':
                    if (diff := self.core_address_book.showing_page - 1) < 1:  # чтобы не уйти в отрицательные числа
                        self.core_address_book.showing_page = 1
                    else:
                        self.core_address_book.showing_page = diff

                # Выход в главное меню
                case '0' | 'exit' | 'e':
                    clear_console()
                    break

    def interface_editing_contact(self) -> None:
        """Обертка для Book.edit_contact. Позволяет изменять существующие контакты в книге.

        :return: None
        """
        while True:
            clear_console()
            print("\nВведите ID контакта, который вы хотели бы изменить.\n")

            self.core_address_book.show_book()

            print("\n> - Следующая страница.\t\t(n)ext\n< - Предыдущая страница.\t(p)revious\n0 - Выход\t\t\t(e)xit\n")
            user_answer = input("$_> ")

            match user_answer:
                case '>' | 'next' | 'n':
                    self.core_address_book.showing_page += 1

                case '<' | 'previous' | 'prev' | 'pr' | 'p':
                    if (delta := self.core_address_book.showing_page - 1) < 1:
                        self.core_address_book.showing_page = 1
                    else:
                        self.core_address_book.showing_page = delta

                case '0' | 'exit' | 'e':
                    clear_console()
                    break

                case _ if user_answer.isdigit():

                    finish_range = COUNT_CONTACTS_VIEW * self.core_address_book.showing_page
                    start_range = finish_range - COUNT_CONTACTS_VIEW + 1

                    user_input_idx = int(user_answer)
                    needed_contact = self.core_address_book.get(user_input_idx - 1)

                    if start_range <= user_input_idx <= finish_range and needed_contact is not None:
                        self.core_address_book.edit_contact(contact=needed_contact)
                    else:
                        print(f"\nВы ввели не корректный ID для контакта. Контакта под ID-{user_input_idx} нет")
                        sleep(1)

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
        print('\nПриложение "Телефонная книга"\nАвтор: Qu1nel\n\nДля работы с приложением следуете инструкциям ниже.')
        print("\n1 - Добавить контакт в книгу.\t\t (a)dd\n2 - Показать телефонную книгу\t\t (s)how")
        print("3 - Удалить контакт из книги.\t\t (r)emove\n4 - Редактировать контакт в книге.\t (ed)it")
        print("5 - Найти контакт в книге.\t\t (sr)earch\n0 - Выйти из приложения.\t\t (e)xit\n")


def clear_console() -> None:
    """Просто очищает консоль."""
    os.system("cls||clear")


def exit_from_program() -> None:
    """Очищает консоль. Выводит сообщение о выходе их приложения. Выходит из приложения.

    :return: None
    """
    clear_console()
    print("\nВы вышли из приложения. Удачного времени суток, пока!\n")
    sleep(2)
    clear_console()
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
