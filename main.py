import argparse
import json 
from datetime import datetime
from schema.py import format_entry

expense_list = {}

#This function will handle adding a new item to the expense_list
def add(amount, description)
    format_entry(amount, description)
    return entry

    if amount in expenses == float:
        if description in expenses != str:
            expense_list.update(expenses)
        else:
            print("Your entry is invalid")
    id += 1
    return expense_list

#This will handle updating the expense list
def update(amount, description):
    if isinstance(amount, float):
        if isinstance(description, str):
            expense_list.update({description: amount})
        else:
            print("One of your entries is invalid")

#This will handle deleting an item matching the keyword from the expense list
def delete(item):
    if item in expense_list:
        del item
        print(item, "has been removed.")
    else:
        print(item, "is not on your expense list")

def view_expenses():
    expense_list.sort()
    print(expense_list)

