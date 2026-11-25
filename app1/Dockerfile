FROM python:3.12-alpine

COPY ./requirements.txt /requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r /requirements.txt

COPY . /app/

RUN adduser -S www

USER www

ENTRYPOINT [ "python3" ]

CMD [ "app1.py" ]
