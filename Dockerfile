# © TonyStarkBotz

# Don't Remove Credit @TonyStark_Botz
# Join our Telegram Channel For Amazing Bot @TonyStark_Botz
# Ask Doubt on telegram @TonyStarkBotzXSupport

FROM python:3.10.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /Stark-FILTER-BOT
WORKDIR /Stark-FILTER-BOT
COPY . /Stark-FILTER-BOT
CMD ["python", "bot.py"]
