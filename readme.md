# QuickLink - Flask URL Shortener & Analytics Platform

## Overview

QuickLink is a Flask-based URL Shortener and Analytics Platform that allows users to generate short URLs, track clicks, view analytics, generate QR codes, and interact with REST APIs. The application provides a modern dashboard with search, statistics, and data visualization features.

---

## Features

### URL Management

- Generate short URLs
- Redirect to original URLs
- Delete URLs
- Search URLs
- Click tracking

### Analytics

- Total URLs statistics
- Total clicks statistics
- Average clicks calculation
- Most visited URL
- Top 5 links chart using Chart.js

### Additional Features

- QR Code generation
- Copy URL functionality
- Responsive Bootstrap UI

---

## Tech Stack

### Backend

- Flask
- SQLAlchemy
- SQLite

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript
- Chart.js

### Additional Libraries

- qrcode
- Pillow

---

## Project Structure

url-shortener-flask/

├── app.py

├── models.py

├── config.py

├── requirements.txt

├── templates/

├── static/

│ ├── css/

│ ├── js/

│ └── qr/

└── instance/

```
└── urls.db
```

---

## Installation

1. Clone Repository

git clone https://github.com/charanepuri/quicklink-flask-url-shortener.git

2. Navigate to Project

cd quicklink-flask-url-shortener

3. Create Virtual Environment

python -m venv venv

4. Activate Environment

Windows:

venv\Scripts\activate

5. Install Dependencies

pip install -r requirements.txt

6. Run Application

python app.py

---

## Learning Outcomes

- Flask Application Development
- SQLAlchemy ORM
- REST API Development
- Database Design
- QR Code Generation
- Data Visualization
- Responsive UI Design
- Analytics Dashboard Development

---

## Author

Charan Teja Epuri

Aspiring Python Full Stack Developer
