from dotenv import load_dotenv
from pathlib import Path
from os import getenv
import sqlalchemy

env_path = Path('.') / 'config/.env'
load_dotenv(dotenv_path=env_path)

PASSWD = getenv('PASSWORD')
HOST = getenv('HOST')
USER = getenv('USER')
NAME = getenv('NAME')
print(NAME)
engine = sqlalchemy.create_engine(
    f'postgresql://{USER}:{PASSWD}@{HOST}/{NAME}',
    execution_options={
        "isolation_level": "REPEATABLE_READ"
    }
)