<h2 align="center">Useful</h2>


### Описание проекта:
Скоро

### Инструменты разработки

**Стек:**
- Python >= 3.8
- FastAPI >= 0.61
- Tortoise ORM
- Postgres

**Ссылки**:
- [Сайт](https://djangochannel.com)
- [Канал Youtube](https://www.youtube.com/channel/UCFCaz7mA2qNodfTh0x1ET5Q)
- [Telegram](https://t.me/fastapiru)
- [Группа в VK](https://vk.com/djangochannel)
- [Поддержать проект](https://donatepay.ru/don/186076)

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

    прописать конект к smtp

##### 4) В корне проекта создать .env.dev

    SECRET_KEY=fuf823rg2388gc828^&%&^%^&T^&gf
    POSTGRES_DB=useful_dev
    POSTGRES_USER=useful_user
    POSTGRES_PASSWORD=useful_pass
    POSTGRES_HOST=useful-db

##### 5) Создать образ

    docker-compose build

##### 6) Запустить контейнер

    docker-compose up
    
##### 7) Создать миграции

    docker exec -it useful-back aerich init-db
    
##### 8) Создать суперюзера

    docker exec -it useful-back python scripts/createsuperuser.py

##### 10) Если не выполняет команды

- Войти в контейнер - _docker exec -it useful-back bash_
- Выполнить команды без _docker exec -it useful-back_ 
                                                        
##### 10) Если нужно очистить БД

    docker-compose down -v
 
## License

[BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause)

Copyright (c) 2020-present, DJWOMS - Omelchenko Michael



