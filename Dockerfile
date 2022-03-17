FROM python:3.10

ADD main.py .
ADD results.json .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "./main.py"]