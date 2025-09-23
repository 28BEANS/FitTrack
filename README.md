# FitTrack

A web application for gym goers and fitness enthusiasts who want to **organize their workout routines**, **track meals**, and **monitor weight**.  
Built with **Flask**, **Jinja**, and **SQLite**.

---

## Features

- 🏋️ Create and manage workout routines  
- 🍎 Log daily meals and track nutrition  
- ⚖️ Record and monitor weight progress over time  
- 👤 User authentication and personalized dashboard  
- 📊 Simple, clean interface powered by Flask & Jinja templates  

---

## Tech Stack

- **Backend**: [Flask](https://flask.palletsprojects.com/)  
- **Frontend**: Jinja templating, HTML5, CSS3, JavaScript  
- **Database**: SQLite  

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fittrack.git
   cd fittrack
   
2. Create a virtual environment and activate it:
   ```bash
    python3 -m venv venv
    source venv/bin/activate    # On macOS/Linux
    venv\Scripts\activate       # On Windows
   
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
6. Setup DB:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   
8. Run dev server:
   ```bash
   flask run
  

