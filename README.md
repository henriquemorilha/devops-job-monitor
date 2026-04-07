# 📊 Mainframe Job Monitor API

A simple API that simulates mainframe job status monitoring, inspired by real-world enterprise environments.

This project was created to demonstrate backend fundamentals, API design, and containerization using Docker.

---

## 🚀 Tech Stack

* Python
* Flask
* Docker

---

## 📡 Endpoint

### GET /status

Returns the current status of a simulated mainframe job.

### Example Response

```json
{
  "job_name": "JOB001",
  "status": "SUCCESS",
  "timestamp": "2026-04-07T12:00:00"
}
```

---

## ▶️ How to Run

### Run with Docker

```bash
docker build -t job-monitor .
docker run -p 5000:5000 job-monitor
```

---

## 🎯 Purpose

This project aims to simulate monitoring of batch jobs in a mainframe-like environment, which is a common scenario in large enterprise systems.

---

## 📌 Future Improvements

* Add multiple job tracking
* Integrate with a database
* Add logging and observability
* Expose metrics for monitoring (Prometheus)

---

## 👨‍💻 Author

**Henrique Morilha**

IT Specialist | Mainframe Operations & Infrastructure
SRE & DevOps Practices | Automation & Observability

📍 Brazil
🔗 LinkedIn: https://www.linkedin.com/in/hmorilha/
