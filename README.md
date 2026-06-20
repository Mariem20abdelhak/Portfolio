# Mariem Abdelhak — Portfolio

Personal portfolio website built with **Flask (Python)** and deployed on **Vercel**.  
Cybersecurity-themed dark UI with matrix rain background, terminal animation, and filterable project cards.

## Features

- Cybersecurity dark theme with matrix rain canvas
- Animated terminal widget in the hero section
- Filterable project cards (full-stack / security / web / industrial)
- Scroll-reveal animations
- Fully responsive layout
- Deployed as a Python serverless function on Vercel

## Tech Stack

- **Backend**: Python 3.9 + Flask 3.0
- **Frontend**: Vanilla HTML/CSS/JS (Space Mono + DM Sans fonts)
- **Deployment**: Vercel (serverless)

## Local Development

```bash
# 1. Clone the repo
git clone https://github.com/Mariem20abdelhak/portfolio.git
cd portfolio

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run locally
python api/index.py
# Open http://localhost:5000
```

## Deploy to Vercel

```bash
# Install Vercel CLI
npm i -g vercel

# Login and deploy
vercel login
vercel

# Production deploy
vercel --prod
```

Vercel auto-detects Python via `vercel.json`. No extra config needed.

## Project Structure

```
portfolio/
├── api/
│   └── index.py          # Flask app (entry point for Vercel)
├── templates/
│   └── index.html        # Jinja2 template
├── static/
│   ├── css/style.css
│   └── js/main.js
├── requirements.txt
├── vercel.json
├── .gitignore
└── README.md
```

## Customization

All content (projects, experience, skills) lives in `api/index.py` in plain Python lists/dicts — no database needed. Edit and push to update the live site automatically.

## Contact

**Mariem Abdelhak** — mariemabdelhak5@gmail.com  
[GitHub](https://github.com/Mariem20abdelhak) · [LinkedIn](https://linkedin.com/in/abdelhak-mariem) · [Portfolio](https://portfolio-website-mariem.vercel.app/)
