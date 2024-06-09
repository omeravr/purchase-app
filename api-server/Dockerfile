FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install flask pymongo kafka-python
CMD ["python", "app.py"]

