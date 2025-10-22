#!/usr/bin/env python3
# NexFord BAN6420 Final Assigment
# Kayode Ogunyemi 



### Import Relevant Libraries 
from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from models import User
import os
from dotenv import load_dotenv





load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client.get_database("survey_db")
collection = db.get_collection("users")

EXPENSE_CATEGORIES = ["utilities", "entertainment", "school_fees", "shopping", "healthcare"]

@app.route("/")
def index():
    return render_template("index.html", categories=EXPENSE_CATEGORIES)

@app.route("/submit", methods=["POST"])
def submit():
    age = request.form.get("age")
    gender = request.form.get("gender")
    total_income = request.form.get("total_income")
    
    expenses = {}
    for cat in EXPENSE_CATEGORIES:
        checked = request.form.get(f"expense_{cat}")
        amount = request.form.get(f"amount_{cat}") or 0
        expenses[cat] = float(amount) if checked else 0.0
    
    user = User(age=int(age), gender=gender, total_income=float(total_income), expenses=expenses)
    collection.insert_one(user.to_dict())
    
    flash("Survey submitted successfully!")
    return render_template("success.html")
    
    
    

    
    
    
    
    

if __name__ == "__main__":
    app.run(debug=True)