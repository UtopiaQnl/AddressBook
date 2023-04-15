from typing import Type

from core.Controller import Controller

from controllers.MenuController import MenuController
from controllers.ExitController import ExitController
from controllers.ShowController import ShowController

from supportive.State import State


DefaultController = MenuController

CONTROLLERS = {
    State.INIT: DefaultController,
    State.EXIT: ExitController,
    State.SHOW: ShowController,
}


def get_controller_by_state(state: State) -> Type[Controller]:
    required_controller = CONTROLLERS.get(state)

    if required_controller is not None:
        return required_controller

    return DefaultController
