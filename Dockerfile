FROM python:3.7

WORKDIR /role-admin
COPY . /role-admin

RUN pip install -r requirements.txt

CMD ["python"]