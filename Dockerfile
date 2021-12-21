FROM python:3.10.1-buster

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY src/ .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "python3", "web_calc.py" ]

EXPOSE 80