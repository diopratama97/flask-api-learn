# IMPORT LIBRARY
from flask import Flask, app, request
from flask_restful import Resource, Api
from flask_cors import CORS
from werkzeug.wrappers import response

# INISIASI OBJECT

app = Flask(__name__)

#inisiasi object flask_restful
api = Api(app)

#inisiasi object flask_cors
CORS(app)

#inisiasi variable kosong bertipe dictionary
identitas = {}

#membuat class resource
class ContohResource(Resource):
    #method get dan post
    def get(self):
        #response = {"message":"Hello World"}
        return identitas
    
    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"message": "Success poll"}
        return response

#setup resource
api.add_resource(ContohResource, "/helloworld", methods=["GET","POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5000)
