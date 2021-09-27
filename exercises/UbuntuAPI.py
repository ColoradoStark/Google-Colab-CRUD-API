from flask import Flask, request, jsonify

from flask import request

class PlayerInfo:
  ip = ""
  name = "No Hosts Found"

HostingPlayer = PlayerInfo()
print(HostingPlayer.ip)

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():

    return "<h1>The server is up</h1>"

@app.route("/hostgame/", methods=['POST'])
def hostgame():

    HostingPlayer.name = request.get_json()['name']
    HostingPlayer.ip = request.get_json() ['ip']
    return jsonify(isError=False, message="Success", statusCode=200, ip=HostingPlayer.ip, name=HostingPlayer.name), 200

@app.route("/findhost/", methods=['GET'])
def findhost():

    return jsonify(isError=False, message="Success", statusCode=200, ip=HostingPlayer.ip, name=HostingPlayer.name), 200

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)
