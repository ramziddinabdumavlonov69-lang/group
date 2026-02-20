from flask import Flask, render_template, request, jsonify
import webview
from brain import process_input
from memory import Memory
from file_manager import save_file
import threading
import os

app = Flask(__name__)
memory = Memory()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    data = request.json
    user_text = data.get("message")

    response = process_input(user_text)
    return jsonify({"response": response})

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    filepath = os.path.join("files", file.filename)
    file.save(filepath)
    memory.add_memory("file", file.filename)
    return jsonify({"status": "success"})

def start():
    app.run(port=5000)

if __name__ == "__main__":
    t = threading.Thread(target=start)
    t.daemon = True
    t.start()

    webview.create_window("Smart Memory Bot", "http://127.0.0.1:5000")
    webview.start()
