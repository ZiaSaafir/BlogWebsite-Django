# COLAB Blog 🚀

A full-stack monolithic blogging web application built with **Python**, **Django**, **Bootstrap 5**, and **SQLite**. Developed as a reference full-stack application for the **ZIA SAAFIR** peer-learning tech curriculum.

---

## 🌟 Key Features

* **Authentication System:** Secure user registration, login, and logout workflows powered by Django's authentication framework.
* **Object-Level Authorization:** Author-only permissions for editing and deleting posts (`post.author == request.user` verification on both backend and frontend).
* **Full CRUD Functionality:** Create, Read, Update, and Delete blog posts seamlessly.
* **Dynamic Routing:** Clean dynamic URL patterns (`/post/<int:pk>/`) with safe `get_object_or_404` error handling.
* **Responsive UI:** Modern, clean interface styled with Bootstrap 5 grid layout and custom CSS.

---

## 🛠️ Tech Stack

* **Backend Framework:** Django 5.x (Python 3.x)
* **Frontend:** HTML5, CSS3, Bootstrap 5 (Django Template Language)
* **Database:** SQLite (Development)
* **Version Control:** Git & GitHub

---

## 📁 Project Architecture

colab_blog_workspace/
├── manage.py
├── db.sqlite3                  # SQLite Database
├── colab_project/              # Project Configuration
│   ├── settings.py             # Configured Apps, Static files & Auth URLs
│   └── urls.py                 # Root URL Router
└── blog/                       # Core Application
├── admin.py                # Admin Panel Configuration
├── forms.py                # ModelForm definitions (PostForm)
├── models.py               # Database Models (Post, User)
├── urls.py                 # App Route Endpoints
├── views.py                # Business Logic & Authorization Checks
├── static/blog/            # Static CSS Assets
└── templates/blog/         # Modular DTL Templates (Base, Feed, Auth)


---

## 🚀 Quickstart Guide

Follow these steps to run the application locally on your machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/ZiaSaafir/BlogWebsite-Django.git](https://github.com/ZiaSaafir/BlogWebsite-Django.git)
cd BlogWebsite-Django

2. Set Up Virtual Environment (Optional but Recommended)
Bash

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
Bash

pip install django

4. Run Database Migrations
Bash

python3 manage.py makemigrations
python3 manage.py migrate

5. Create Admin Superuser
Bash

python3 manage.py createsuperuser

6. Start Development Server
Bash

python3 manage.py runserver

Visit http://127.0.0.1:8000/ in your browser.
🗺️ Upcoming Roadmap (Phase 2)

    [ ] Django REST Framework (DRF): Convert monolithic views into RESTful JSON API endpoints.

    [ ] JWT Authentication: Implement SimpleJWT for secure headless token authentication.

    [ ] Decoupled Frontend: Integrate React SPA frontend.

    [ ] Docker & PostgreSQL: Package application containers for cloud deployment.

👤 Author

Zia Saafir

BS Computer Science Student & Software Developer

Peshawar, Pakistan


---

### Terminal Command to Save & Push the README

Run these commands in your Ubuntu terminal:

```bash
# Save the text into README.md
git add README.md
git commit -m "Add professional project README documentation"
git push origin main

InshaAllah, in our next phase we will take this solid monolith foundation and transform it into an executive-grade, decoupled application using Django REST Framework (DRF), JWT Authentication, and Swagger API documentation! All the best with your presentation!
