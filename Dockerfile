FROM python:3.9-alpine

WORKDIR /home/

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 80

COPY ./src /home/src

RUN ls

CMD ["uvicorn", "src.main.server:app", "--host", "0.0.0.0", "--port", "80"]