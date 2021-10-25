FROM python:3.9

WORKDIR /usr/src/app

COPY . .

RUN pip install -U pipenv && \
    pipenv install --ignore-pipfile --system --deploy

EXPOSE 80
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=80

CMD ["flask",  "run"]
