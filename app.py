from flask import Flask, jsonify
import random
import os
from datetime import datetime, timedelta

app = Flask(__name__)

# Lista de jobs simulados
jobs = [
    {"job_name": "PKZ0930M", "system": "Z/OS", "queue": "BATCH01"},
    {"job_name": "PKZ0931N", "system": "Z/OS", "queue": "BATCH02"},
    {"job_name": "PKZ0932O", "system": "Z/OS", "queue": "BATCH01"},
]

status_options = ["SUCCESS", "FAIL", "RUNNING"]

def random_start_time():
    """Gera um horário de início aleatório nas últimas 2 horas"""
    now = datetime.now()
    start = now - timedelta(minutes=random.randint(0, 120))
    return start.strftime("%Y-%m-%dT%H:%M:%S")

def random_duration():
    """Gera uma duração aleatória em hh:mm:ss"""
    minutes = random.randint(1, 60)
    seconds = random.randint(0, 59)
    return f"00:{minutes:02}:{seconds:02}"

def generate_job_status(job):
    return {
        "job_name": job["job_name"],
        "status": random.choice(status_options),
        "start_time": random_start_time(),
        "duration": random_duration(),
        "system": job["system"],
        "queue": job["queue"]
    }

# Rota principal
@app.route("/")
def home():
    return "DevOps Job Monitor API is running"

# Rota de status
@app.route("/status")
def status():
    all_jobs = [generate_job_status(job) for job in jobs]
    return jsonify(all_jobs)

# Porta dinâmica (pro Render)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)