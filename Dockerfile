FROM python:3.7

ADD requirements.txt /
RUN pip install -r ./requirements.txt

COPY web/ /web
WORKDIR /web

EXPOSE 5000
CMD ["python", "server.py"]
