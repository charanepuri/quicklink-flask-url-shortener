# QuickLink - Flask URL Shortener

## Overview

QuickLink is a lightweight, responsive Flask-based URL Shortener that allows users to quickly convert long web addresses into short, shareable links, dynamically generate QR codes, and track link visits.

---

## Features

### URL Shortening & Redirection
- **Instant URL Shortening**: Generates unique, compact 6-character short codes.
- **Auto-Protocol Handling**: Automatically prefixes `https://` if omitted.
- **URL Validation**: Ensures entered links are syntactically valid before shortening.
- **Fast Redirection**: Instantly routes users to the destination URL.
- **Visit Tracking**: Automatically counts clicks for each shortened link.

### QR Code & Sharing
- **Dynamic QR Code Generation**: Automatically creates a QR code for every shortened link.
- **One-Click Download**: Direct download button to save generated QR code images.
- **One-Click Copy**: Built-in clipboard copy button with user feedback.
- **Direct Link Preview**: Quick shortcut to test the generated URL immediately.

### User Interface & Experience
- Clean, modern layout built with **Bootstrap 5**.
- Inline dismissible alerts for error handling.
- Production-ready with reverse-proxy support (`ProxyFix`).

---

## Tech Stack

### Backend
- **Python 3**
- **Flask**
- **Flask-SQLAlchemy**
- **SQLite**
- **Gunicorn** (for production deployments)

### Frontend
- **HTML5** & **CSS3**
- **Bootstrap 5**
- **JavaScript (ES6+)**

### Additional Libraries
- **qrcode** & **Pillow** (QR code generation)
- **Werkzeug** (ProxyFix middleware)

---

## Project Structure

```text
Quick Link URL Shortener/
├── app.py                     # Application routes & core logic
├── config.py                  # App configuration & environment variables
├── models.py                  # SQLAlchemy URL database model
├── Procfile                   # Deployment process file (Render / Heroku)
├── requirements.txt           # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css          # Custom styling & Bootstrap enhancements
│   ├── js/
│   │   └── script.js          # Clipboard copy functionality
│   ├── qr/                    # Generated QR code image files
│   └── QuickLink-Documentation.pdf # Project documentation
├── templates/
│   ├── base.html              # Base HTML template with navbar & footer
│   └── index.html             # Main shortener UI & result container
└── instance/
    └── urls.db                # SQLite database
```

---

## Installation & Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/charanepuri/quicklink-flask-url-shortener.git
cd quicklink-flask-url-shortener
```

### 2. Create and Activate Virtual Environment
**Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```
Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## Author

**Charan Teja Epuri**  
- GitHub: [@charanepuri](https://github.com/charanepuri)  
- LinkedIn: [Charan Teja Epuri](https://www.linkedin.com/in/charan-teja-972aa9231/)  
- Repository: [quicklink-flask-url-shortener](https://github.com/charanepuri/quicklink-flask-url-shortener)
