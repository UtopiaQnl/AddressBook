from core.Controller import Controller
from supportive.State import State
from views import render_template


def is_valid_user_request(request: str) -> bool:
    """Предикат. Проверяет пользовательский ввод в меню на валидность.

    Если строка является '0', '1', '2' или 'next', 'previous', 'exit'
    то валидация пройдет успешно.

    Args:
        request - Введенная строка от пользователя.

    Returns:
        Булевый тип.
    """
    if not request or request.startswith('-'):
        return False

    valid_str_value = (
        'n', 'ne', 'nex', 'next',
        'p', 'pr', 'pre', 'prev', 'previous'
    )

    if request.isdigit() and len(request) == 1:
        return True
    elif request.isalpha() and request in valid_str_value:
        return True

    return False


def get_new_state_from_request(request: str) -> State:
    """Получает состояние программы в зависимости от запроса от пользователя.

    Args:
        request - Проверенная строка (т.е является корректной: 0 1 2 next ...)
        введённая пользователем.

    Returns:
        State - Новое состояние
    """

    # TODO: добавить состояния продолжить (т.е. остаться в этом же контролере) и уже в нем делать изменения, которые
    # TODO: пойдут на отрисовку в view?

    return State.INIT


class ShowController(Controller):
    def run(self) -> State:
        render_template(template_name='show.tmplt', context=dict())

        user_request = input("$> ").lower().strip()

        output_state = State.INIT

        if is_valid_user_request(user_request):
            output_state = get_new_state_from_request(user_request)

        return output_state
