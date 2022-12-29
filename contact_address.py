from datetime import datetime
from dataclasses import dataclass

from tools import clear_console


@dataclass
class ContactAddress:
    name: str
    surname: str
    number_phone: str
    email: str
    time_create: datetime

    def __eq__(self, another_contact) -> bool:
        """Сравнивает контакт с another_contact.

        :param another_contact: Экземпляр класса ContactAddress
        :raise TypeError: Если another_contact не является экземпляром класс ContactAddress
        :return: bool
        """

        if not isinstance(another_contact, ContactAddress):
            raise TypeError("Для сравнения подходят только другие контакты!")

        set_of_pairs_attrs = ((self.name, another_contact.name), (self.surname, another_contact.surname),
                              (self.number_phone, another_contact.number_phone), (self.email, another_contact.email))

        for first_attr, second_attr in set_of_pairs_attrs:
            if first_attr != second_attr:
                return False
        return True

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
        while True:
            clear_console()
            print("\nВведите новый номер телефона")
            new_number_phone = input("$_> ").capitalize()

            if not new_number_phone:
                print("Вы ввели пустой номер телефона. Изменения не засчитаны...")
                sleep(1)
                break
            elif len(new_number_phone) >= MAX_WIDTH_NUMBER_PHONE:
                print("Вы ввели слишком длинный номер телефона. Изменения не засчитаны...")
                sleep(1)
                break

            self.number_phone = new_number_phone
            break

    def change_email(self) -> None:
        """Отдельное окно. Позволяет изменить почту (email)."""
        while True:
            clear_console()
            print("\nВведите новую почту")
            new_email = input("$_> ")

            if not new_email:
                print("Вы ввели пустую почту. Изменения не засчитаны...")
                sleep(1)
                break
            elif len(new_email) >= MAX_WIDTH_EMAIL:
                print("Вы ввели слишком длинную почту. Изменения не засчитаны...")
                sleep(1)
                break

            self.email = new_email
            break
