from supportive.State import State
from core.Controller import Controller

from views import render_template


def is_valid_user_request(request: str) -> bool:
    """Предикат. Проверяет пользовательский ввод на валидность.

    Если строка является 'a', 's', 'r', 'ed', 'sr', 'e' или
    '-1', '0', '1', '2', '3', '4', '5' то валидация пройдет успешно.

    Args:
        request - Введенная строка от пользователя.

    Returns:
        Булевый тип.
    """
    if not request:
        return False

    request = request[1:] if request.startswith('-') else request

    return len(request) == 1 and request.isdigit()


def get_new_state_from_request(request: str) -> State:
    """Получает состояние программы в зависимости от запроса от пользователя.

    Args:
        request - Проверенная строка (т.е является корректной: 1 0 -1 2 3 ...)
        введённая пользователем.

    Returns:
        State - Новое состояние, иначе состояние по-умолчанию (State.INIT)
    """
    code = int(request)

    match code:
        case -1 | 0:
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
