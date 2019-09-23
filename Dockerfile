FROM python:3.7

ENV STATIC_URL /static
ENV STATIC_PATH /nvram/neuraldistribution/staging/web/app/static

ADD requirements.txt /
RUN pip install --requirement ./requirements.txt

ADD neuraldistribution.py /
ADD DBInterface.py /
ADD config.py /

COPY web ./web

CMD [ "python","-u", "./web/main.py" ]
