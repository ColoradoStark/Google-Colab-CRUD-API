app = Flask(__name__)
run_with_ngrok(app)   
  
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
    
app.run()
