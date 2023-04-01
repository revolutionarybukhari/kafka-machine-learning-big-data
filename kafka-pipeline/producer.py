from flask import Flask,request
import json
from kafka import KafkaProducer
import time
from datetime import datetime

producer = KafkaProducer(bootstrap_servers = 'localhost:9092')

app = Flask(__name__)
@app.route('/', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    data = request.json
    producer.send('sensor_values', json.dumps(data).encode('utf-8'))
    return data
        
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')