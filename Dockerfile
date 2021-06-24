FROM python:3.8-alpine

# GENERAL PACKAGES
RUN apk add --no-cache postgresql-libs \
    && apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev curl


# WAIT
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait


# PYTHON & POETRY
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV POETRY_HOME "/opt/poetry"
ENV PATH "$POETRY_HOME/bin:$PATH"

RUN curl -sSL 'https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py' | python \
    && poetry --version

# Creating folders, and files for a project:
COPY ./app /app
COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml

RUN poetry install
RUN poetry add gunicorn

WORKDIR /app
