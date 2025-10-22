#!/usr/bin/env python3
# NexFord BAN6420 Final Assigment
# Kayode Ogunyemi 




###========================
###Read users from MongoDB and write to CSV (one row per user, expenses flattened).
###========================


### Import Relevant Libraries 
import argparse
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from models import User


### Load the MONGODB Connections Details
load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI) if MONGO_URI else MongoClient('mongodb+srv://notefarm2015_db_user:mRj9V5lAyrwhSf5A@nexforddb.ry3slwj.mongodb.net/?retryWrites=true&w=majority&appName=NexFordDB')
db = client.get_database('survey_db')
users_col = db.get_collection('users')

EXPENSES_CATEGORIES = ['utilities','entertainment','school_fees','shopping','healthcare']



### Export to CSV from MONGO DB
def export(out_path):
    cursor = users_col.find()
    with open(out_path, 'w', newline='', encoding='utf-8') as f:
        import csv
        writer = csv.writer(f)
        writer.writerow(User.csv_headers(EXPENSES_CATEGORIES))
        for doc in cursor:
            expenses = doc.get('expenses', {})
            user = User(age=doc.get('age', 0), gender=doc.get('gender', ''), total_income=doc.get('total_income', 0), expenses=expenses)
            writer.writerow(user.to_csv_row(EXPENSES_CATEGORIES))




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', default='responses.csv', help='Output CSV file')
    args = parser.parse_args()
    export(args.out)
    print('Exported to', args.out)
