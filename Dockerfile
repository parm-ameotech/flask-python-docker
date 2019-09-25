FROM python:3.7

ADD requirements.txt /
RUN pip install -r ./requirements

ADD . /code
WORKDIR /code
CMD python app.py

