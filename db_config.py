from dotenv import load_dotenv
from os import getenv
import sqlalchemy

load_dotenv()

PASSWD = getenv('password')
HOST = getenv('host')
PORT = getenv('port')
USER = getenv('user')

engine = sqlalchemy.create_engine(
    f'postgresql://{USER}:{PASSWD}@{HOST}/telega',
    execution_options={
        "isolation_level": "REPEATABLE_READ"
    }
)