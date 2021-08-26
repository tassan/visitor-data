from flask import request
from flask import jsonify
from flask.app import Flask
import socket as s
import os
from dotenv import load_dotenv
import requests

load_dotenv(".env")

app = Flask(__name__)


@app.route("/ip", methods=["GET"])
def get_ip():
    hostname = s.gethostname()
    ip = s.gethostbyname(hostname)
    return jsonify({"hostname": hostname, "ip": ip}), 200


@app.route("/geo", methods=["GET"])
def get_geo():
    key = os.getenv("KEY")
    url = f"https://ipgeolocation.abstractapi.com/v1/?api_key={key}"
    response = requests.get(url)
    return response.content
