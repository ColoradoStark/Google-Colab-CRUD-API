# -*- coding: utf-8 -*-
"""Rest-Uni.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ShIG-Kbznms3UrVfQDyWmlARNxts6VRu
"""

# Install Dependencies

!pip install flask-ngrok

from flask import Flask, request, jsonify
from flask_ngrok import run_with_ngrok
from flask import request
import json

# Define a Player Object

class player:

    def __init__(self, name, ip, hp, mana):
        self.name = name
        self.ip = ip
        self.hp = hp
        self.mana = mana
  

    def update(self, name, ip, hp, mana):
        self.name = name
        self.ip = ip
        self.hp = hp
        self.mana = mana

# Create a "list" (Something like an Array) of Player Objects

players = [player("gandalf","1.1.1.1", 30,100), player("froto","2.2.2.2", 20,5), player("boromir", "3.3.3.3", 50, 0)]

# Define a function that will convert the list to JSON and write it to the disk

def Backup():

  backupdata = json.dumps([ob.__dict__ for ob in players])
  f = open("backup.csv", "w")
  f.write(backupdata)
  f.close()

# Exectue a backup of the data in the list

Backup()

app = Flask(__name__)
run_with_ngrok(app)   
  
@app.route("/", methods=['GET'])
def home():

    return "<h1>The server is up</h1>"

@app.route("/create/", methods=['POST'])
def create():

    name = request.get_json()['name']
    ip = request.get_json() ['ip']
    hp = request.get_json() ['hp']
    mana = request.get_json() ['mana']
    players.append(player(name, ip, hp, mana))

    uid = next((i for i, item in enumerate(players) if item.name == name), -1)

    Backup()
    
    return jsonify(message="Successfully Created Player", id=uid), 200

@app.route("/getallplayers/", methods=['GET'])
def getallplayers():

    allplayers = json.dumps([ob.__dict__ for ob in players])

    return allplayers, 200

@app.route("/getplayerinfo/", methods=['GET'])
def getplayerinfo():

    uid = request.get_json()['id']

    return jsonify(name = players[uid].name, ip = players[uid].ip, hp=players[uid].hp, mana=players[uid].mana), 200


@app.route("/update/", methods=['PUT'])
def update():
    
    name = request.get_json()['name']
    ip = request.get_json() ['ip']
    hp = request.get_json() ['hp']
    mana = request.get_json() ['mana']
    uid = request.get_json() ['id']
    
    players[uid].name = name
    players[uid].ip = ip 
    players[uid].hp = hp 
    players[uid].mana = mana 

    Backup ()
    
    return jsonify(message="Successfully Updated Player", id=uid), 200


@app.route("/delete/", methods=['DELETE'])
def delete():

    uid = request.get_json() ['id']
    
    players[uid].name = "null"
    players[uid].ip = "null" 
    players[uid].hp = 0 
    players[uid].mana = 0 

    Backup ()
    
    return jsonify(message="Successfully Deleted Player Data", id=uid), 200
 
app.run()