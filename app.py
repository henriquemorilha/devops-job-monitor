from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/status")
def status():
    return jsonify({
        "job": "PKZ0930M",
        "status": random.choice(["SUCCESS", "FAIL", "RUNNING"])
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)