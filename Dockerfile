FROM python:3.8-slim-buster

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "tcli.py"]