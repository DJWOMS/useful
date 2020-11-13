FROM    python:3.8-buster as devstage
ENV     LANG C.UTF-8
ENV     USER useful
ENV     PROJECTPATH=/home/useful/app

RUN     set -x && apt-get -qq update \
        && apt-get install -y --no-install-recommends \
        libpq-dev python3-dev git \
        && apt-get purge -y --auto-remove\
        && rm -rf /var/lib/apt/lists/*

RUN     curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
        cd /usr/local/bin && \
        ln -s /opt/poetry/bin/poetry && \
        poetry config virtualenvs.create false

RUN     useradd -m -d /home/${USER} ${USER}\
        && chown -R ${USER} /home/${USER}

RUN     mkdir -p ${PROJECTPATH}
WORKDIR  ${PROJECTPATH}
ADD    pyproject.toml  ${PROJECTPATH}
#ADD    poetry.lock* ${PROJECTPATH}

RUN     poetry install

COPY    . ${PROJECTPATH}

ADD     https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait ${PROJECTPATH}/wait
RUN     chmod +x ${PROJECTPATH}/wait

USER    ${USER}






#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
#
#WORKDIR /app
#
#RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
#    cd /usr/local/bin && \
#    ln -s /opt/poetry/bin/poetry && \
#    poetry config virtualenvs.create false
#
#COPY ./pyproject.toml ./poetry.lock* /app/
#
#RUN poetry install
## --no-root --no-dev
##CMD uvicorn main:app --reload
#COPY . /app
