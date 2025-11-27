# 📌 GARI TECH – Feedback Submission System

This project is a redesigned and improved **Feedback Experience Page** for GARI TECH.  
It provides a modern, responsive UI with dark/light mode and a backend feature to store user feedback securely.

This system was developed as part of a **final selection assignment**.

---

## 🚀 Features

- 🎨 Modern UI with professional visual design  
- 🌙 Light/Dark theme toggle  
- 🧾 Feedback form with input validation  
- 🗄 Stores submissions in SQLite database  
- 🔔 Displays success & error alerts  
- 📱 Fully responsive (Desktop + Mobile)

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML, CSS, Bootstrap 5 |
| Backend | Python (Flask) |
| Database | SQLite |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```
gari-tech-feedback-system/
│
├── app.py
├── feedback.db
├── requirements.txt
├── README.md
│
├── templates/
│   └── feedback.html
│
└── static/
    └── style.css
```

---

## ⚙️ How to Run the Project

### 1️⃣ Create a virtual environment

```bash
python -m venv venv
```

### 2️⃣ Activate it

Windows:

```bash
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Start the server

```bash
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🧪 View Saved Feedback (SQLite)

```sql
SELECT * FROM feedback;
```

---

## ✨ Future Enhancements

- 🔐 Admin login to view submissions  
- 📩 Email notifications on submission  
- 📊 Export feedback (CSV/Excel)  
- 📈 Analytics dashboard (charts + insights)

---

## 👤 Author

**Name:** Tanushri B  
**Purpose:** GARI TECH Final Selection Assignment  
**Role:** Developer  

---

✔ **Status:** Completed & Working  
