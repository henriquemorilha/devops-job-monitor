# Mainframe Job Monitor API

Simple API that simulates mainframe job status.

## Tech Stack
- Python (Flask)

## Endpoint
GET /status

## How to run with Docker

```bash
docker build -t job-monitor .
docker run -p 5000:5000 job-monitor