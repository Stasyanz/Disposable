from pathlib import Path
from os.path import dirname, abspath

from starlette.config import Config


config = Config("../.env")

DATABASE_URL = config("DATABASE_URL", cast=str, default="")
TEMPLATES_DIR = Path(dirname(dirname(abspath(__file__)))) / 'templates'

schema = "http://"
fqdn = "localhost"  # Need to  generate link
