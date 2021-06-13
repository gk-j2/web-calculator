FROM python:3.7.10-buster

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY src/ .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "python3", "web_calc.py" ]

EXPOSE 80