# Lab 5 — Cloud Run Portfolio Deployment

## Overview
This lab demonstrates deploying a containerized Flask web application to **Google Cloud Run** as part of the Northeastern MLOps curriculum. Instead of the default "Hello World" app, I modified the lab to deploy a **personal portfolio website** built from my own resume data.

## What I Built
A fully responsive personal portfolio website featuring:
- Hero section with key career metrics
- Technical skills grid
- Work experience timeline
- Featured projects section
- Education background
- Contact information

## Tech Stack
| Tool | Purpose |
|------|---------|
| Python + Flask | Web framework |
| HTML/CSS/JS | Frontend portfolio page |
| Docker | Containerization |
| Google Cloud Run | Serverless deployment |
| GCP Artifact Registry | Container storage |

## Project Structure
```
Cloud_Runner_Lab/
├── app.py                  # Flask application
├── Dockerfile              # Container configuration
├── requirements.txt        # Python dependencies
└── templates/
    └── index.html          # Portfolio webpage
```

## How to Run Locally
```bash
# Activate virtual environment
source /Users/sush/MLOps_Labs/.venv/bin/activate

# Install dependencies
pip install flask gunicorn

# Run the app
python app.py
```
Then open `http://localhost:8080` in your browser.

## How to Deploy to Cloud Run
```bash
gcloud run deploy portfolio-service \
  --source . \
  --region us-east1 \
  --allow-unauthenticated
```

## Live Deployment
🌐 **[https://portfolio-service-756491711716.us-east1.run.app](https://portfolio-service-756491711716.us-east1.run.app)**

## Modification from Original Lab
The original lab deploys a simple "Hello, World!" Flask app. I modified it to:
1. Serve a full HTML portfolio page using Flask's `render_template`
2. Include real resume data — experience, skills, projects, education
3. Add animations, scroll reveal effects, and a terminal-style UI card
4. Use a professional dark technical theme with responsive design

## Author
**Sushritha Bharadwaj** — MS Data Analytics Engineering, Northeastern University