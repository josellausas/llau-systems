FROM python:3.8-alpine
RUN apk update && apk add postgresql postgresql-dev gcc python3-dev musl-dev
RUN pip install psycopg2
ENV PYTHONUNBUFFERED 1
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["./manage.py", "runserver", "0:8000"]
