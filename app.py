from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

# Rota principal ("/")
@app.route("/")
def home():
    return "DevOps Job Monitor API is running"

# Rota de status
@app.route("/status")
def status():
    return jsonify({
        "job": "PKZ0930M",
        "status": random.choice(["SUCCESS", "FAIL", "RUNNING"])
    })

# 👉 Porta dinâmica (pro Render)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)