from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/config")
def download_config():
    return "{Download config}"

@app.post("/config")
def upload_config():
    return "{Upload config}"
