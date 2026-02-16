from flask import Flask, request, jsonify, render_template, redirect, url_for
from pymongo import MongoClient
import json
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

app = Flask(__name__)

# -----------------------------
# MongoDB Connection
# -----------------------------
client = MongoClient(MONGO_URL)
db = client["task_db"]
collection = db["tasks"]


# -----------------------------
# API Route (Read from File)
# -----------------------------
@app.route("/api/tasks")
def api_tasks():
    with open("tasks.json", "r") as file:
        data = json.load(file)

    return jsonify(data)


# -----------------------------
# Home Page (Show Form)
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def home():

    error = None

    if request.method == "POST":

        try:
            title = request.form["title"]

            if not title:
                error = "Task title is required!"
                return render_template("index.html", error=error)

            collection.insert_one({
                "title": title,
                "status": "Pending"
            })

            return redirect(url_for("success"))

        except Exception as e:
            error = str(e)
            return render_template("index.html", error=error)

    return render_template("index.html", error=error)


# -----------------------------
# Success Page
# -----------------------------
@app.route("/success")
def success():
    return render_template("success.html")


# -----------------------------
# View All Tasks (From DB)
# -----------------------------
@app.route("/tasks")
def view_tasks():

    tasks = list(collection.find({}, {"_id": 0}))

    return jsonify(tasks)


# -----------------------------
# Run Server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
