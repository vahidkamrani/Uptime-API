FROM python:latest

ENV PYTHONBUFFERED 1

WORKDIR /code

COPY packages.txt /code/

RUN pip install -U pip

RUN pip install -r packages.txt

COPY . /code/

EXPOSE 8000

CMD ["127.0.0.1:8000"]
