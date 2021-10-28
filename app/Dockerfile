FROM python:3.9

WORKDIR /usr/src/app

COPY . .

RUN pip install -U pipenv && \
    pipenv install --ignore-pipfile --system --deploy

