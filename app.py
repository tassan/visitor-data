from flask import json, request
from flask import jsonify
from flask.app import Flask
import socket as s
import os
from dotenv import load_dotenv
from flask.templating import render_template
import requests
from markupsafe import escape

load_dotenv(".env")

app = Flask(__name__)
KEY = os.getenv("KEY")


@app.route("/")
def index():
    hostname = s.gethostname()
    ip = s.gethostbyname(hostname)
    url = f"https://ipgeolocation.abstractapi.com/v1/?api_key={KEY}&ip_address={ip}"
    response = requests.get(url)
    geo = response.json()
    return render_template('index.html', content=geo)


@app.route("/ip", methods=["GET"])
def get_ip():
    hostname = s.gethostname()
    ip = s.gethostbyname(hostname)
    return jsonify({"hostname": hostname, "ip": ip}), 200

@app.route("/geo", methods=["GET"])
def get_geo():
    hostname = s.gethostname()
    ip = s.gethostbyname(hostname)
    url = f"https://ipgeolocation.abstractapi.com/v1/?api_key={KEY}&ip_address={ip}"
    response = requests.get(url)
    return response.content

@app.route("/geo/<ip>", methods=["GET"])
def get_geo_by_ip(ip):
    ip_address = escape(ip)
    url = f"https://ipgeolocation.abstractapi.com/v1/?api_key={KEY}&ip_address={ip_address}"
    response = requests.get(url)
    return response.content

