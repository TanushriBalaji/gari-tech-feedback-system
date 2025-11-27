from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

DB_NAME = "feedback.db"

app = Flask(__name__)
app.secret_key = "change_this_secret_key"  # for flash messages


def init_db():
    """Create feedback table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        """
    )
    conn.commit()
    conn.close()


@app.route("/", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        # Validation
        if not name or not email or not message:
            flash("⚠️ All fields are required.", "error")
            return redirect(url_for("feedback"))

        # Save to SQLite
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO feedback (name, email, message, created_at) VALUES (?, ?, ?, ?)",
            (name, email, message, datetime.utcnow().isoformat())
        )
        conn.commit()
        conn.close()

        flash("✅ Thank you! Your feedback has been submitted.", "success")
        return redirect(url_for("feedback"))

    return render_template("feedback.html")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
