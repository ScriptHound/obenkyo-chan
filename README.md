# obenkyo-chan
Обенкё-тян это бот вк для изучения японской письменности.

# перед запуском

Чтобы бота развернуть понадобится провести несколько нехитрых манипуляций:
1. В docker-compose в сегменте obenkyo -> commands дописать python import_to_db.py, чтобы модели заимпортились в бд
2. Дописать свой дотенв, положить в config/.env и положить свой alembic.ini в корневую директорию, alembic.ini можно найти здесь: https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file там надо будет написать свои креденциалы для бд
3. docker-compose up --build

# вероятные ошибки
1. докер-композ возможно будет ругаться на /var/lib/postgres/data/, просто назначьте вместо этой директории в postgres сегменте докер-композа свою любую другую.

