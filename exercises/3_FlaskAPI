app = Flask(__name__)
run_with_ngrok(app)   
  
@app.route("/", methods=['GET'])
def home():

    return "<h1>The server is up</h1>"
	
@app.route("/userinfo/", methods=['POST'])
def info():

    return "<h1>thanks for the info</h1>"
    
app.run()
