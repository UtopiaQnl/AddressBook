import os
import sys
from time import sleep
from typing import NoReturn

from core.Controller import Controller

from views import render_template


class ExitController(Controller):
    def run(self) -> NoReturn:
        for sec in range(3, -1, -1):
            render_template(context={"second": sec}, template_name="exit.tmplt")
            sleep(1)

        os.system("cls||clear")
        sys.exit(0)
