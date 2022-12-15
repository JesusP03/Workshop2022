from auth import images, flavors, keys, security, networks
from flask import Flask
from flask import request
from flask import render_template
import requests
from resources import generate_token
from resources import *
from create import crear_instancia, generate_json
#Import all necessary libraries

app = Flask(__name__)

#Principal route
@app.route("/")
def index():
    return render_template("index.html", images=images(), networks=networks(), flavors=flavors(), keypairs=keys(), security_groups=security())

#Post for generate token
@app.route('/post', methods=['GET'])
def new_token():
    return generate_json()

#Creating de instance
@app.route('/crear_instancia', methods=['POST'])
def new_instance():
    return crear_instancia()

#Prin in console the token generated
print(generate_token())



if __name__ == '__main__':
    app.run(debug=True)