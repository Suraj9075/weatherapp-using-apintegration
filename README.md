# Weather Application (API Integration)

A Django-based **Weather Application** that fetches real-time weather data using an **external Weather API**.  
This project demonstrates how to integrate third-party APIs in Django, process JSON responses, and display dynamic weather information using web templates.

---

## 🛠️ Technologies Used

- Python  
- Django  
- Weather API (API Integration)  
- HTML & CSS  
- SQLite  

---

## 📌 Top 5 Topics Covered

- Django Project & App Structure  
- API Integration in Django  
- Handling JSON Responses  
- Function-Based Views (FBV)  
- Dynamic Data Rendering with Templates
  
## Project Structure
weather-app/

│

├── core/

│ ├── settings.py

│ ├── urls.py

│ ├── asgi.py

│ └── wsgi.

│

├── weather/

│ ├── migrations

│ ├── templates/

│ ├── static/

│ ├── views.py

│ ├── urls.py

│ ├── models.py

│ └── apps.py

│
├── web/

│ ├── templates

│ └── static/

│

├── db.sqlite3

├── manage.py

└── README.md

---

## 📂 Folder Explanation

### `core/`
Main Django project configuration.
- Handles settings, middleware, and root URLs.

### `weather/`
Main app responsible for:
- API integration
- Fetching weather data
- Processing JSON responses
- Sending data to templates

### `web/`
Contains frontend templates and static files for UI rendering.

### `db.sqlite3`
SQLite database used for storing application data (if required).

### `manage.py`
Command-line utility to manage Django project operations.

---

## 🌐 How the Weather API Works

1. User enters a city name  
2. Django view sends a request to the Weather API  
3. API returns weather data in JSON format  
4. JSON data is processed in the backend  
5. Weather details are displayed on the web page  

---

## 🚀 How to Run the Project

1. Install required packages:
```bash
pip install django requests


2. Run the server:

python manage.py runserver


3. Open browser:

http://127.0.0.1:8000/
