FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN rm -rf /tmp
COPY . /app/

CMD sh run.sh