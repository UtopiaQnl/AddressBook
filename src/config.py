from os.path import dirname, realpath, join
from pathlib import Path

global APP_PATH

APP_PATH = dirname(realpath(__file__))

SAVE_FILE_NAME: str = "database.db"
SAVE_DB_PATH: Path = Path(join(APP_PATH, SAVE_FILE_NAME))
