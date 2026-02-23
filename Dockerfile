FROM python:3.10-slim-bullseye

WORKDIR /
COPY loadgen /loadgen
WORKDIR /loadgen

# setup app requirements
RUN pip3 install -r requirements.txt

CMD python3 app.py
