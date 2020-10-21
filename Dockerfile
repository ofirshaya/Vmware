FROM python:3.6
COPY . /app/
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]
EXPOSE 80
