# 📝 Django Blog App

A simple Django blog application built to showcase backend development skills using Django. It supports creating and displaying blog posts with detail views.

## 🚀 Features

- List blog posts on homepage
- View individual blog post
- Admin dashboard to manage posts
- Responsive layout using Bootstrap

## 🛠️ Built With

- Django
- HTML + Bootstrap
- SQLite (default, easy to switch to PostgreSQL)
- Python 3.x


## 🧰 Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

```bash
git clone https://github.com/IbrahimAce/django-blog.git
cd django-blog
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
