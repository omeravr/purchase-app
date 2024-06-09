from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from kafka import KafkaConsumer
import threading
import json
import logging

app = Flask(__name__)
client = MongoClient('mongodb://root:example@mongodb:27017/')
db = client.purchaseDB

logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buy', methods=['POST'])
def buy():
    data = request.json
    db.purchases.insert_one(data)
    return jsonify({'status': 'Purchase added'}), 201

@app.route('/getAllUserBuys', methods=['GET'])
def get_all_user_buys():
    purchases = list(db.purchases.find({}, {'_id': 0}))
    return jsonify(purchases)

def consume_kafka():
    consumer = KafkaConsumer('purchases', bootstrap_servers='kafka:9092')
    for message in consumer:
        purchase = json.loads(message.value.decode())
        logging.info(f"Received message: {purchase}")
        result = db.purchases.insert_one(purchase)
        logging.info(f"Inserted purchase with ID: {result.inserted_id}")

def start_consumer():
    consumer_thread = threading.Thread(target=consume_kafka)
    consumer_thread.daemon = True
    consumer_thread.start()

if __name__ == '__main__':
    start_consumer()
    app.run(host='0.0.0.0')

