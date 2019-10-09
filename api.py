from flask import Flask, request
from flask_restful import Resource, Api
from face_dataset import makeDataset
from face_recognition import recognition
from face_training import training
from ossys import *
from servomotor import *

app = Flask(__name__)
api = Api(app)


#Face recognition api
#dataset api
class DataSet(Resource):
    
    def get(self, name):
        makeDataset(name)
        return {name: name}


#Traing api
class Traning(Resource):
    
    def get(self, name):
        training()
        return {name: name}


#recognition api
class Recognition(Resource):
    
    def get(self, name):
        recognition()
        return {name: name}


#ServoMotor api
#LeftPan api
class LeftPan(Resource):
    
    def get(self, name):
        leftpan()
        return {name: name}


#RightPan api
class RightPan(Resource):
    
    def get(self, name):
        rightpan()
        return {name: name}


#UpTilt api
class UpTilt(Resource):
    
    def get(self, name):
        uptilt()
        return {name: name}


#DownTilt api
class DownTilt(Resource):
    
    def get(self, name):
        downtilt()
        return {name: name}


#ServoStart api
class ServoStart(Resource):
    
    def get(self, name):
        servostart()
        return {name: name}


#ServoStop api
class ServoStop(Resource):
    
    def get(self, name):
        servostop()
        return {name: name}


#streaming api          
#streaming api1
class OsSys(Resource):
    
    def get(self):
        ossys()


#streaming api2
class Streaming(Resource):
    
    def get(self):
        streaming()


#Face recognition
api.add_resource(DataSet, '/dataset/<string:name>')
api.add_resource(Traning, '/traning/<string:name>')
api.add_resource(Recognition, '/recognition/<string:name>')

#ServoMotor
api.add_resource(LeftPan, '/leftpan/<string:name>') #LeftPan api
api.add_resource(RightPan, '/rightpan/<string:name>') #RightPan api
api.add_resource(UpTilt, '/uptilt/<string:name>') #UpTilt api
api.add_resource(DownTilt, '/downtilt/<string:name>') #DownTilt api
api.add_resource(ServoStart, '/servostart/<string:name>') #ServoStart api
api.add_resource(ServoStop, '/servostop/<string:name>') #ServoStop api

#streaming
api.add_resource(OsSys, '/ossys') #streaming1
api.add_resource(Streaming, '/streaming') #streaming2

app.run(host='0.0.0.0',port=5000)

















