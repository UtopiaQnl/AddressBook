from os.path import dirname, realpath, join
from pathlib import Path

MAX_WIDTH_NAME = 20  # максимальная ширина для имени
MAX_WIDTH_SURNAME = 20  # максимальная ширина для фамилии
MAX_WIDTH_NUMBER_PHONE = 20  # максимальная ширина для номера телефона
MAX_WIDTH_EMAIL = 30  # максимальная ширина для электронной почты
MAX_WIDTH_ID = 5  # максимальная длина для id контакта
COUNT_CONTACTS_VIEW = 15  # кол-во показываемых контактов

global APP_PATH

APP_PATH = dirname(realpath(__file__))

SAVE_FILE_NAME: str = "database.db"
SAVE_DB_PATH: Path = Path(join(APP_PATH, SAVE_FILE_NAME))
