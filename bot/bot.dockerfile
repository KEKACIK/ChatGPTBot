FROM python:3.11-slim

COPY . /bot/

WORKDIR /bot

RUN pip install -r requirements.txt

ENTRYPOINT python run_bot.py