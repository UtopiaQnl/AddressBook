import os
from config import APP_PATH


def get_file_template(tempalte_name: str) -> str:
    tempalte_path = os.path.join(APP_PATH, 'templates', tempalte_name)

    with open(tempalte_path, mode='r', encoding="UTF-8") as f:
        text = f.read()

    return text


def clear_screen(flag: bool) -> None:
    if flag is True:
        os.system('cls||clear')


def render_template(context=None, template_name='menu.tmplt', clear=True) -> None:
    if not context:
        context = {}

    clear_screen(clear)

    template = get_file_template(template_name)

    print(template.format(**context), flush=True)
