# kafkaGoogleMapsReactTryout
A python based emitter emits a json resembling { PostalCode: '', Type: 'seller' / 'Buyer'} to kafka, another python websocket server receives this and a react client connects to this websocket and renders the latlong markers to a google map component in real time

Create images for dockerfiles inside pythonWebsockerServer folder and GoogleMapsReactFrontEnd/map-renderer folder using 
```
docker build -t python-ws-server .
docker build -t react-client . 
```

Run the docker-compose file on kafkaInstallation folder using
```
docker-compose up
```

Access the react-client by accessing *localhost:3000* on the browser

To view the kafka messages being sent to the react-client through the python ws server Kafka needs to receive the messages from somewhere, this project has an emitter which sends the message to kafka. 
To run the emitter use

```
pip install kafka-python
python kafkaGoogleMapsReactTryout/emitter.py
```
For safety do the above on a venv
