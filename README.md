# Kayode Ogunyemi 
# Healthcare Income & Expense Survey Tool

Implemented a Flask web application to collect participant data (Age, Gender, Total Income, and Expenses), stores the data in MongoDB, 
exports to CSV for analysis, includes a Jupyter notebook for visualization, exports charts into a PowerPoint, and includes deployment notes for AWS.


## Contents
- Flask_HealthCare_App.py: Flask Application 
- export_csv.py: script to export MongoDB data to CSV
- models.py: User class used to structure data
- notebooks/: Data_Visualisation_For_Flask (ipynb)
- Dockerfile: containerize app for AWS deployment


## Quickstart (Local)
1. Create virtualenv and install dependencies:
MONGO_URI="mongodb+srv://notefarm2015_db_user:mRj9V5lAyrwhSf5A@nexforddb.ry3slwj.mongodb.net/?retryWrites=true&w=majority&appName=NexFordDB"
FLASK_SECRET_KEY=#1234_4321$


```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Create `.env` from `.env.example` and fill `MONGO_URI` and `FLASK_SECRET_KEY`.
3. Start MongoDB. it is running on MONGO_URI="mongodb+srv://notefarm2015_db_user:mRj9V5lAyrwhSf5A@nexforddb.ry3slwj.mongodb.net/?retryWrites=true&w=majority&appName=NexFordDB".
4. Start app:

```bash
python3.9 Flask_HealthCare_App.py


5. Visit `http://localhost:5000/` and submit responses.
6. Export CSV from MongoDB:

```bash
python export_csv.py --out responses.csv
```

7. Open `notebooks/Data_visualisation.ipynb` in Jupyter and run the cells to generate `charts/`.


## AWS Deployment (summary)
- Create an account on AWS
- Start an instance and connect to it
- Use SSH to copy folder into flask 
- Store secrets in AWS Secrets Manager or environment variables in EB/ECS.
- Use HTTPS via load balancer certificates.


