FROM python:3.10

RUN apt update


RUN mkdir /Dispo

WORKDIR /Dispo

RUN mkdir /commands

COPY ./src ./src
COPY ./commands ./commands

COPY requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r ./requirements.txt

CMD ["bash"]
