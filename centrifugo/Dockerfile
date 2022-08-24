FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
COPY . /app/
CMD python manage.py runserver 0.0.0.0:8001
