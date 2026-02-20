from flask import Flask, render_template, request, jsonify
import webview
import threading
import os
from memory import Memory

app = Flask(__name__)
memory = Memory()

UPLOAD_FOLDER = "files"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    data = request.json
    key = data.get("key")
    value = data.get("value")

    memory.save_data(key, value)

    return jsonify({"status": "success"})

@app.route("/search", methods=["POST"])
def search():
    data = request.json
    keyword = data.get("keyword")

    results = memory.search_data(keyword)

    return jsonify({"results": results})

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    memory.save_file(file.filename)

    return jsonify({"status": "success"})

def start_server():
    app.run(port=5000)

if __name__ == "__main__":
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()

    webview.create_window("Save Storage Bot", "http://127.0.0.1:5000")
    webview.start()
