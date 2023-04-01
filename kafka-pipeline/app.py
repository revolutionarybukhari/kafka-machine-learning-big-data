import random
import time
import re
import sys
from flask import Flask, render_template
import threading
from turbo_flask import Turbo
from kafka import KafkaConsumer
import json
import pickle
import pandas as pd
import sklearn as sk
app = Flask(__name__)

turbo = Turbo(app)

loaded_model1 = pickle.load(open('models/dcf.pkl', 'rb'))
# loaded_model2 = pickle.load(open('models/KNN.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

consumer = KafkaConsumer('sensor_values', bootstrap_servers='localhost:9092', auto_offset_reset='earliest', enable_auto_commit = False)

labels = ['Walking', 'Standing', 'Running', 'Not in Use', 'Phone in Use']

def most_common(lst):
    return max(set(lst), key=lst.count)

@app.context_processor
def inject_load():
    for message in consumer:
        i = json.loads(message.value)
        temp=json.loads(i["accelerometer"]) 
        temp2=json.loads(i["gyroscope"])
        a1=temp[0]
        a2=temp[1]
        a3=temp[2]
        b1=temp2[0]
        b2=temp2[1]
        b3=temp2[2]
        load = [a1, a2, a3, b1, b2, b3]
        # df = pd.DataFrame(list(zip(a1, a2, a3, b1, b2, b3)), columns =["acc_x","acc_y","acc_z", "gyr_x","gyr_y","gyr_z"])
        # print(df)
        dict = {"accex":load[0], "accey":load[1], "accez":load[2], "gyrox":load[3], "gyroy":load[4], "gyroz":load[5]}
        df = pd.DataFrame(dict, index=[0])
        # print(df)
        # result = []
        result = loaded_model1.predict(df)[0]
        # result = (loaded_model2.predict(df)[0])
        # print(result[0], result[1])
        print(result)
        del df
        return {"accex":load[0], "accey":load[1], "accez":load[2], "gyrox":load[3], "gyroy":load[4], "gyroz":load[5], "predict":labels[result - 1]}
    # consumer.close()

@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()

def update_load():
    with app.app_context():
        while True:
            time.sleep(1)
            turbo.push(turbo.replace(render_template('sensors.html'), 'send_data'))