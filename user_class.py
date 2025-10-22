#!/usr/bin/env python3
# NexFord BAN6420 Final Assigment
# Kayode Ogunyemi 


###====================================
###USER CLAAS TO LOOP THROUGH COLLECTED DATA
###====================================



### Import Relevant Libraries 
import csv



### Create a USER class
class User:
    def __init__(self, age, gender, income, expenses):
        self.age = age
        self.gender = gender
        self.income = income
        self.expenses = expenses
      
      
    @staticmethod
    def save_to_csv(data, filename='user_data.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Age", "Gender", "Income", "Expenses"])
            for d in data:
                writer.writerow([d.age, d.gender, d.income, d.expenses])