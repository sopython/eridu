FROM python:3.5-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY . /usr/src/app

RUN pip install .

ENTRYPOINT ["python"]
CMD ["bin/run_eridu.py"]
