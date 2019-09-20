FROM python:3.7

ADD requirements.txt /
RUN pip install --requirement ./requirements.txt

ADD neuraldistribution.py /
ADD DBInterface.py /
ADD config.py /
COPY . /model /


CMD [ "python","-u", "./neuraldistribution.py" ]
