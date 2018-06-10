#Dependencies
#for starting server
from lib.flask import Flask
from lib.flask import render_template
#for parsing csv
from lib import csv
#for parsing json
from lib import json

#import custom made csv parser
from lib import csvParser

#load configurations
with open('./config/config.json', 'r') as f:
    #config is the json file
    #loaded up configurations to spec_names, specifications
    configuration = json.load(f)

#assign port number
portNumber = configuration["port"]
#assign hostname
hostName = configuration["host"]

#flask router config
#initialize flask app to run only when it is called directly by the interpreter
app = Flask(__name__)

#setting up routes

#homepage
@app.route('/')
def homepage():
    return render_template("index.html")
    #return "<body style='background:skyblue;'><h1 style='text-align:center;color:white;font-family:Helvetica;'>Welcome to our restful web service</h1><ul style='list-style-type:none;color:white;font-family:Helvetica;font-weight:bold;text-align:center;'>Allowed Routes:<li style='align:center;'>/health</li></ul><p style='color:white;font-family:Helvetica;font-weight:bold;text-align:center;'>This restful service is not token protected. Also CORS is not supported here.<p></body>"

#health api route
@app.route('/health')
def health():
    #this is where we will parse csv and then construct a dictionary out of it
    data = csvParser.csvParse("health","health")

    #return the dictionary(json data) in string format.
    #NOTE: it has to be in string format, browser cannot display json.
    return json.dumps(data)

#not found handler
@app.route('/<value>')
def notFound(value):
    if value != "" or value != "health":
        return "The route %s is not defined. I would love to decorate this page as well but who has the time."%value

#similarly set up other routes as well

#__name__ will be "main" if the file is directly run from python
#if the file is imported and run from another pythonfile then __name__ will be equal to server
#therefore we need to make sure that the latter part of code only runs if the server.py file is directly run from python interpreter
if __name__ == "__main__":
    app.run(host = hostName, port = portNumber, debug = True)
