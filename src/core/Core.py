from typing import Type

from ..supportive.State import State

from ..controllers.MenuController import MenuController

from Controller import Controller

DefaultController = MenuController

CONTROLLERS = {
    State.INIT: DefaultController,
}


def get_controller_by_state(state: State) -> Type[Controller]:
    required_controller = CONTROLLERS.get(state)

    if required_controller is not None:
        return required_controller

    return DefaultController
