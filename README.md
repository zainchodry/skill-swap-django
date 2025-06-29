# 🧠 Skill Swap - Django Project

Skill Swap is a Django-based web platform that allows users to **sign up, log in, and exchange skills**. The system is designed to let users offer and request skills using a simple form-based interface.

---

## 🚀 Features

- ✅ User Registration & Authentication (Signup/Login)
- 🎯 Skill Offer and Request Forms
- 📄 HTML Templates with Bootstrap UI
- 🛠 Django Admin Panel Support
- 🔐 Secure user data handling

---

## 📁 Project Structure

skill-swap-django/
├── oscar/ # Main Django App (business logic)
│ ├── migrations/ # DB migrations
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
│
├── skillswap/ # Project settings
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── templates/ # HTML templates
│ ├── base.html
│ ├── home.html
│ ├── login.html
│ ├── offer_form.html
│ ├── request_form.html
│ └── signup.html
│
├── venv/ # Virtual environment (should be ignored in Git)
├── manage.py # Django management script
├── requirements.txt # Python dependencies
├── db.sqlite3 # SQLite DB (should be ignored in production)
└── .gitignore # Git ignore rules



---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/skill-swap-django.git
cd skill-swap-django


#Set up Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


#. Install Dependencies
pip install -r requirements.txt


#Run Migrations

python manage.py makemigrations
python manage.py migrate


#Run the Development Server
python manage.py runserver


