#!/usr/bin/env python3
# NexFord BAN6420 Final Assigment
# Kayode Ogunyemi 



### Import Relevant Libraries 
from dataclasses import dataclass, field
from typing import Dict

@dataclass
class User:
    age: int
    gender: str
    total_income: float
    expenses: Dict[str, float] = field(default_factory=dict)

    def to_dict(self):
        return {
            "age": self.age,
            "gender": self.gender,
            "total_income": self.total_income,
            "expenses": self.expenses
        }