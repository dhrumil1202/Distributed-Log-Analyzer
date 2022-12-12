FROM python:3

WORKDIR /worker

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY logger.py logger.py

CMD ["python", "-u", "logger.py"]