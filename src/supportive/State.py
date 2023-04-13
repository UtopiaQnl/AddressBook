from dataclasses import dataclass
from enum import Enum
from typing import TypeAlias, Literal

Code: TypeAlias = Literal[
    -1, '-1', 0, '0',
    1, '1', 2, '2',
]


@dataclass(slots=True, frozen=True)
class StateProgram:
    """_StateProgram - Хранит семантический код (состояние) программы в неизменяемом виде.

    Возможные коды:
        -1 - Статус выхода. Обозначает выход из программы.
         0 - Статус инициализации. Обозначает запуск программы.
         1 - Статус показа информации. Обозначает вывод контактов.
         2 - Статус добавление контакта в базу контактов.
    """
    code: Code = 0

    def __str__(self) -> str:
        return f'<State {self.code} code>'


class State(Enum):
    """State - Хранит типы статусов программы.

    Возможные типы:
        EXIT - Статус выхода.
        INIT - Статус инициализации. Программа запущена. Отрисовка меню.
        SHOW - Статус вывода контактов. Отрисовка меню с контактами.
        ADD - Статус добавление контакта в базу. Отрисовка меню добавления.
    """
    EXIT = StateProgram(-1)
    INIT = StateProgram(0)
    SHOW = StateProgram(1)
    ADD = StateProgram(2)
