# kafka-machine-learning-big-data
The projects predicts the human movemenrt/Postures using the live sensor data from the mobile phone sensors.
This project had three phases starting with generating sensor data from the
Accelerometer and Gyroscope of our phones and labeling this data.This was to be
done by creating a basic Android or IOS app that collects the required data via these
sensors and upload it to our Laptop via Flask Api or Bluetooth.After that this labeled
data was to be stored in a database whether that be MongoDB or MYSQL.The next
phase included ingesting the data in to the Kafka Environment and then processing and
classifying the Labels by using ML Classification model.The last stage included
implementing a frontend website using flask or any-other framework which would take
Live data from our Phone and predict the position or state of the Phone and later show
the readings of Accelerometer and Gyroscope on the Website along with the Predicted
State.
For the collection of data we developed an app using flutter and some opensource
flutter api code for the implementation(refrences given at the end).The app records the
X,Y and Z coordinates of both gyroscopeand accelerometer.The app takes a server
address from the user and hits the data onto that server , meanwhile a Flask api has
been implemented that takes the lives data being hit on that server as both the laptop
and the flutter application are on the same network (in our case samew wifi connection).
This is is processed , group name is added and the result is stored is a json file where
the parameters of both the sensors are in a json string list.The user just had to
hardcode the file name which will later be used as a label.
Once we had the data in json files we had the job to upload the data to our choosen
database that in our case was MongoDB. We used the concept of json file parsing as
taught to us during the semester to parse the json file extract our required information
and then post in on the database along with its assigned label.
