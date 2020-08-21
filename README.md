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

## Разработка с Docker

##### 1) Сделать форк репозитория

##### 2) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 3) В папке `src.config` файл `local_config.py-example` переименовать в `local_config.py`

##### 4) В корне проекта создать .env.dev

    SECRET_KEY=fuf823rg2388gc828^&%&^%^&T^&gf
    POSTGRES_DATABASE=useful_dev
    POSTGRES_USER=useful_user
    POSTGRES_PASSWORD=useful_pass
    POSTGRES_HOST=db

##### 5) Создать образ

    docker-compose build

##### 6) Запустить контейнер

    docker-compose up
    
##### 7) Создать миграции

    docker exec -it useful_back poetry run alembic revision --autogenerate
    
##### 8) Выполнить миграции

    docker exec -it useful_back poetry run alembic upgrade head
    
##### 9) Создать суперюзера

    docker exec -it useful_back python scripts/createsuperuser.py

##### 10) Если не выполняет команды

- Войти в контейнер - _docker exec -it useful_back bash_
- Выполнить команды без _docker exec -it useful_back_ 
                                                        
##### 10) Если нужно очистить БД

    docker-compose down -v

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



