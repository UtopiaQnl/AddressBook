from supportive.State import State
from core.Controller import Controller

from views import render_template


def is_valid_user_request(request: str) -> bool:
    """Предикат. Проверяет пользовательский ввод в меню на валидность.

    Если строка является 'a', 's', 'r', 'ed', 'sr', 'e', 'exit' или
    '-1', '0', '1', '2', '3', '4', '5' то валидация пройдет успешно.

    Args:
        request - Введенная строка от пользователя.

    Returns:
        Булевый тип.
    """
    if not request:
        return False

    request = request.strip('-')

    valid_str_value = (
        'e', 'ex', 'exit',
    )

    if request.isdigit() and len(request) == 1:
        return True
    elif request.isalpha() and request in valid_str_value:
        return True

    return False


def get_new_state_from_request(request: str) -> State:
    """Получает состояние программы в зависимости от запроса от пользователя.

    Args:
        request - Проверенная строка (т.е является корректной: 1 0 -1 2 3 ...)
        введённая пользователем.

    Returns:
        State - Новое состояние, иначе состояние по-умолчанию (State.INIT)
    """

    code = int(request) if request.isdigit() else request

    match code:
        case -1 | 0 | 'e' | 'exit' | 'ex':
            output_state = State.EXIT
        case 1:
            output_state = State.ADD
        case 2:
            output_state = State.SHOW
        case _:
            output_state = State.INIT

    return output_state


class MenuController(Controller):
    def run(self) -> State:
        render_template(template_name="menu.tmplt")

        user_request = input("$> ").lower().strip()

        output_state = State.INIT

        if is_valid_user_request(user_request):
            output_state = get_new_state_from_request(user_request)

        return output_state
