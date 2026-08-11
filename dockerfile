FROM python:3.12.3-alpine3.19

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip \
    && pip --no-cache-dir install -r requirements.txt

CMD ["python", "wsgi.py"]
