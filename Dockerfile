FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update --fix-missing
RUN pip3 install poetry
RUN poetry install; exit 0
RUN pip3 install python-dotenv
RUN apt-get -y install git apt-utils libpython3-dev
RUN pip3 install sqlalchemy psycopg2 redis alembic
RUN pip3 install git+https://github.com/timoniq/vkbottle.git@v3-uploaders
WORKDIR /home/obenkyo
COPY . /home/obenkyo
