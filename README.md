                                               📌 GARI TECH – Feedback Submission System

This project is a redesigned and improved Feedback Experience Page for GARI TECH.
It provides a modern, responsive UI with light/dark mode and a backend system to store user feedback securely.

This prototype was developed as part of a final selection assignment.

🚀 Features

🎨 Modern UI redesign with professional layout

🌙 Light/Dark mode toggle

📬 Feedback form with validation

💾 Feedback stored in SQLite database

🔔 Success and error messaging

📱 Fully responsive (desktop + mobile)

🛠️ Tech Stack
Layer	        Technology Used
Frontend	    HTML, CSS, Bootstrap 5
Backend	        Python Flask
Database	    SQLite
Version Control	Git & GitHub


📂 Project Structure
gari-tech-feedback/
│
├─ app.py
├─ feedback.db
├─ requirements.txt
├─ README.md
│
├─ templates/
│   └─ feedback.html
│
└─ static/
    └─ style.css

⚙️ How to Run the Project

1️⃣ Create a virtual environment
python -m venv venv

2️⃣ Activate it

Windows:

venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
python app.py

5️⃣ View in Browser

Open:

http://127.0.0.1:5000/

📥 Database Details

User feedback is stored in feedback.db under the table:

feedback


To view entries:

SELECT * FROM feedback;

📈 Future Improvements (Optional Enhancements)

Admin dashboard to view submitted feedback

Export feedback as CSV or Excel

Authentication system for admin access

Email notification on new submissions

👤 Author

Name: Tanushri B
Role: Developer – Assignment Project
Purpose: GARI TECH Final Selection Submission

🏁 Status

✔️ Completed and Fully Functional
This project fulfills all required backend and frontend redesign criteria.
