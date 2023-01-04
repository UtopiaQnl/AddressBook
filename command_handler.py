from time import sleep
from datetime import datetime

from book import Book
from contact_address import ContactAddress
from tools import clear_console, exit_from_program

from config import *


class MainCommandHandler:
    """Класс-обработчик пользовательских команд телефонной книги в консоли.
    |
    |  Методы, определенные здесь:
    |
    |   run(self, /)
    |       Запускает приложение. Отлавливает команды из консоли.
    |
    |   interface_adding_contact(self, /)
    |       Добавляет контакт в книгу.
    |
    |   board_display_interface(self, /)
    |       Позволяет просматривать книгу (Book).
    |
    |   interface_removing_contact(self, /)
    |       Позволяет удалять контакт из книги (Book).
    |
    |   interface_editing_contact(self, /)
    |       Позволяет редактировать контакт в книге (Book).
    |
    |   interface_searching_contact(self, /)
    |       Позволяет искать контакт в книге (Book).
    |
    |   @staticmethod
    |   welcome(/)
    |       Выводит начальные инструкции для пользователя в консоль.
    """

    def __init__(self, address_book: Book):
        self.core_address_book: Book = address_book

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
                    self.interface_removing_contact()

                # Редактировать контакт в телефонной книге
                case '4' | 'edit' | 'ed':
                    self.interface_editing_contact()

                # Искать контакт в телефонной книге
                case '5' | 'search' | 'sr':
                    self.interface_searching_contact()

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
                var: str = input("$_> ")
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
            ).capitalize()

            surname: str = valid_field(
                info_string=("Введите фамилию для контакта:", "Слишком длинная фамилия! Введите фамилию по короче."),
                max_length=MAX_WIDTH_SURNAME
            ).capitalize()

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
                        make_contact_status: bool = True

                        new_contact: ContactAddress = ContactAddress(
                            dict(name=name,
                                 surname=surname,
                                 number_phone=number_phone,
                                 email=email,
                                 time_create=datetime.today()
                                 )
                        )
                        self.core_address_book.add_contact(contact=new_contact)

                        clear_console()

                        print("\nКонтакт успешно сохранен!\n")
                        sleep(1)
                        break

                    case '2' | 'нет' | 'no' | 'n':
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
            user_answer: str = input("$_> ")
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

    def interface_removing_contact(self) -> None:
        """Обертка для Book.remove_contact. Позволяет удалять контакты из книги.

        :return: None
        """
        while True:
            clear_console()
            print("\nВведите ID контакта, который вы хотели бы удалить.\n")

            self.core_address_book.show_book()

            print("\n> - Следующая страница.\t\t(n)ext\n< - Предыдущая страница.\t(p)revious\n0 - Выход\t\t\t(e)xit\n")
            user_answer: str = input("$_> ")

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

                    finish_range: int = COUNT_CONTACTS_VIEW * self.core_address_book.showing_page
                    start_range: int = finish_range - COUNT_CONTACTS_VIEW + 1

                    user_input_idx: int = int(user_answer)
                    needed_contact: ContactAddress = self.core_address_book.get(user_input_idx)

                    if start_range <= user_input_idx <= finish_range and needed_contact is not None:
                        self.core_address_book.remove_contact(contact=needed_contact)
                    else:
                        print(f"\nВы ввели не корректный ID для контакта. Контакта под ID-{user_input_idx} нет")
                        sleep(1)

    def interface_editing_contact(self) -> None:
        """Обертка для Book.edit_contact. Позволяет изменять существующие контакты в книге.

        :return: None
        """
        while True:
            clear_console()
            print("\nВведите ID контакта, который вы хотели бы изменить.\n")

            self.core_address_book.show_book()

            print("\n> - Следующая страница.\t\t(n)ext\n< - Предыдущая страница.\t(p)revious\n0 - Выход\t\t\t(e)xit\n")
            user_answer: str = input("$_> ")

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

                    finish_range: int = COUNT_CONTACTS_VIEW * self.core_address_book.showing_page
                    start_range: int = finish_range - COUNT_CONTACTS_VIEW + 1

                    user_input_idx: int = int(user_answer)
                    needed_contact: ContactAddress = self.core_address_book.get(user_input_idx)

                    if start_range <= user_input_idx <= finish_range and needed_contact is not None:
                        self.core_address_book.edit_contact(contact=needed_contact)
                    else:
                        print(f"\nВы ввели не корректный ID для контакта. Контакта под ID-{user_input_idx} нет")
                        sleep(1)

    def interface_searching_contact(self) -> None:
        """Обертка для Book.search_contact. Позволяет искать контакты в книге.

        :return: None
        """
        while True:
            clear_console()
            print("\nМЕНЮ ПОИСКА КОНТАКТА\n")

            print("\nЧто вы можете сделать:\n")

            print("1 - Найти по имени. (N)ame\n2 - Найти по фамилии. (S)urname")
            print("3 - Найти по номеру телефона. (P)hone\n4 - Найти по почте. (E)mail\n0 - Выход. (e)xit\n")

            user_answer: str = input("$_> ").lower()
            match user_answer:
                case '1' | 'имя' | 'имени' | 'name' | 'N' | 'n':
                    name: str = input("Введите имя:\n$_> ")
                    self.core_address_book.search_contact(name=name)
                    break
                case '2' | 'фамилия' | 'фамилии' | 'surname' | 'S':
                    surname: str = input("Введите фамилию:\n$_> ")
                    self.core_address_book.search_contact(surname=surname)
                    break
                case '3' | 'телефон' | 'номер' | 'номеру' | 'phone' | 'P':
                    number_phone: str = input("Введите номер телефона:\n$_> ")
                    self.core_address_book.search_contact(phone=number_phone)
                    break
                case '4' | 'почта' | 'почте' | 'email' | 'E':
                    email: str = input("Введите почту:\n$_> ")
                    self.core_address_book.search_contact(email=email)
                    break
                case '0' | 'exit' | 'e':
                    clear_console()
                    break

    @staticmethod
    def welcome() -> None:
        """Приветствует пользователя, выводя все инструкции и лого приложения.

        :return: None
        """
        logo: str = ("             _     _                     ____              _" + '\n' +
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
