from flask import json, request
from flask import jsonify
from flask.app import Flask
import socket as s
import os
from dotenv import load_dotenv
import requests

load_dotenv(".env")

app = Flask(__name__)

# DATABASE = os.getenv("DATABASE")
KEY = os.getenv("KEY")


@app.route("/ip", methods=["GET"])
def get_ip():
    hostname = s.gethostname()
    ip = s.gethostbyname(hostname)
    return jsonify({"hostname": hostname, "ip": ip}), 200


@app.route("/geo", methods=["GET"])
def get_geo():
    url = f"https://ipgeolocation.abstractapi.com/v1/?api_key={KEY}"
    response = requests.get(url)
    return response.content

