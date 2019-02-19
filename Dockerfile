#TAG:v1.4
FROM python:3
RUN mkdir /app
WORKDIR /app
COPY controller/* /app/controller/
COPY exceptions/* /app/exceptions/
COPY model/*  /app/model/
COPY routes/* /app/routes/
COPY settings/* /app/settings/
#COPY scripts/* /app/scripts/
COPY venv/* /app/venv/
#COPY config/* /app/config/
#COPY config/data/* /app/config/data/
COPY index.py /app/index.py
COPY requirements.txt /app/requirements.txt
ENV MONGO_URI mongodb://127.0.0.1:27017/api_db
ENV JWT_KEY " "
ENV API_U " "
ENV API_P " "
RUN pip3 install --upgrade pip
RUN pip3 install -U -r /app/requirements.txt
EXPOSE 5554 8200
CMD [ "python", "index.py" ]
