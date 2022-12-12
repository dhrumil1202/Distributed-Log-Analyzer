FROM python:3

WORKDIR /client

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app.py app.py

CMD ["python", "-u", "app.py"]