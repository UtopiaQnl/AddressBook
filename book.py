from contact_address import ContactAddress
from tools import clear_console

from config import *


class ContactNotExists(Exception):
    def __init__(self, contact: ContactAddress):
        self.contact = contact

    def __str__(self):
        return f'Контакт {self.contact} не существует в телефонной книге!'


class Book(dict):
    """Телефонная книга (словарь) для адресов людей.

    __next_idx - Указатель на следующее место в книге
    showing_page - Индекс страницы (для корректного вырисовывания книги в консоль)

    :methods:
        add_contact(contact: ContactAddress) - Добавляет экземпляр ContactAddress в книгу.
        remove_contact(contact: ContactAddress) - Удаляет экземпляр ContactAddress из книги.
        edit_contact() - Позволяет редактировать ContactAddress в книге.
        show_board() - Показывает пользователю телефонную книгу постранично.
        search_contact() - Ищет контакт в книге по 4 основным полям.
        _is_exists(contact: ContactAddress) - Предикат. Проверяет существует ли ContactAddress в книге.
    """

    __next_idx: int = 1
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

        self[Book.__next_idx] = contact
        Book.__next_idx += 1

    def remove_contact(self, contact: ContactAddress) -> None:
        """Удаляет contact из телефонной книги.

        Сдвигает значения с ключами в лево к единице.

        :param contact: Экземпляр класс ContactAddress
        :raise TypeError: Если contact не является экземпляром класс ContactAddress
        :raise ContactNotExists: Если contact не найден в телефонной книге
        :return: None
        """

        def _get_agree_from_user(candidate: ContactAddress) -> bool:
            """Получает подтверждение на удаление контакта из книги от пользователя.

            :return: bool
            """
            while True:
                clear_console()
                print("\nВы уверены что хотите удалить этот контакт?")
                candidate.pprint_info()

                print("\n1 - Да.  (y)es")
                print("2 - Нет. (n)o")
                print("0 - Выход. (e)xit\n")

                user_answer = input("$_> ").lower()
                match user_answer:
                    case '1' | 'да' | 'yes' | 'y':
                        clear_console()
                        return True
                    case '2' | 'нет' | 'no' | 'n' | '0' | 'exit' | 'e':
                        clear_console()
                        return False

        if not isinstance(contact, ContactAddress):
            raise TypeError("Удалять из книги можно только контакты людей!")

        if self._is_exists(contact):
            for idx, member in self.items():
                if member == contact:
                    if _get_agree_from_user(contact) is False:
                        return None

                    del self[idx]
                    next_idx = len(self) + 1

                    for i in range(idx, next_idx):
                        self[i] = self[i + 1]

                    if idx != next_idx:
                        del self[next_idx]

                    self.__next_idx = next_idx
                    return None
        else:
            raise ContactNotExists(contact)

    @staticmethod
    def edit_contact(contact: ContactAddress) -> None:
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

            for idx in range(start_range + 1, finish_range + 1):
                block_id = '|' + str(idx).center(header['№'])
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

    def search_contact(self,
                       name: str | None = None,
                       surname: str | None = None,
                       phone: str | None = None,
                       email: str | None = None) -> None:
        """Производит поиск контакта в книге по одному из полей.

        Функция не работает, когда переданы несколько полей для поиска, иначе TypeError

        :param name: str. Имя по которому будет производиться поиск.
        :param surname: str. Фамилия по которой будет производиться поиск.
        :param phone: str. Номер телефона по которому будет производиться поиск.
        :param email: str. Почта по которой будет производиться поиск.
        :raise TypeError: В случаи передачи несколько ключевых аргументов.
        :return: None
        """
        if (count_of_none := (name, surname, phone, email).count(None)) != 3:
            raise TypeError(f"Метод принимает только один ключевой аргумент, а передано {4 - count_of_none}")

        target = f'{name}{surname}{phone}{email}'.replace('None', '').lower().strip()
        all_contacts: list[ContactAddress] = list(self.values())

        find_contacts: list[ContactAddress] = []

        for contact in all_contacts:

            name_eq: bool = isinstance(contact.name, str) and contact.name.lower().strip() == target
            surname_eq: bool = isinstance(contact.surname, str) and contact.surname.lower().strip() == target
            phone_eq: bool = isinstance(contact.number_phone, str) and contact.number_phone.lower().strip() == target
            email_eq: bool = isinstance(contact.email, str) and contact.email.lower().strip() == target

            if any((name_eq, surname_eq, phone_eq, email_eq)):
                find_contacts.append(contact)

        if (count_find_contacts := len(find_contacts)) == 0:
            print("Контакты не найдены!...")
        else:
            print(f"Найдено несколько контактов {count_find_contacts}")
            for contact in find_contacts:
                contact.pprint_info()

        input("Нажмите Enter для выхода в меню")

        print()
        for i in range(5, 0, -1):
            print(f"Выход в главное меню через {i} сек...", end='\r\b')
            sleep(1)

        clear_console()

    def _is_exists(self, contact: ContactAddress) -> bool:
        """ Предикат. Возвращает True если contact существует в книге, False иначе.

        :param contact: Экземпляр класс ContactAddress
        :return: bool[True, False]
        """
        for save_contact in self.values():
            if save_contact == contact:
                return True
        return False
