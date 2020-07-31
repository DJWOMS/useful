<h2 align="center">Useful</h2>


### Описание проекта:
Скоро

### Инструменты разработки

**Стек:**
- Python >= 3.8
- FastAPI >= 0.61
- PostgreSQL

**Ссылки**:

## Старт

#### 1) Создать образ

    docker-compose build

##### 2) Запустить контейнер

    docker-compose up
    
##### 3) Перейти по адресу

    http://127.0.0.1:8000/docs

## Разработка

##### 1) Сделать форк репозитория и поставить звездочку)

##### 2) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории
    
##### 3) Установить poetry

    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
    
[help docs](https://python-poetry.org/docs/)
    
##### 4) Устанавливить зависимости
    
    poetry install

##### 5) В папке `src.config` файл `local_config.py-exp` переименовать в `local_config.py` и прописать конект к базе

##### 6) Активировать виртуальное окружение

    poetry shell
       
##### 7) Создание миграций

    poetry run alembic revision --autogenerate

##### 8) Применить миграции

    poetry run alembic upgrade head
    
##### 10) Создать суперпользователя

    в разработке
    
##### 11) Запустить сервер

    uvicorn main:app --reload
    
##### 12) Перейти по адресу

    http://127.0.0.1:8000/docs
 
## License

[BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

Copyright (c) 2020-present, DJWOMS - Omelchenko Michael



