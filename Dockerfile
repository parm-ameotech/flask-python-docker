FROM python:3.7

RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /nvram/neuraldistribution/staging/web/app/static

ADD requirements.txt /
RUN pip install --requirement ./requirements.txt

ADD neuraldistribution.py /
ADD DBInterface.py /
ADD config.py /

CMD [ "python","-u", "./neuraldistribution.py" ]
