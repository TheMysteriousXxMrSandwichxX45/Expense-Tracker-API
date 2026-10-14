import argparse
import json 
from schema import create_entry

expense_list = {}

#This function will handle adding a new item to the expense_list
def add(amount, description):
    if amount in expense_list == float:
        if description in expense_list != str:
            expense_list.update(expense_list)
        else:
            print("Your entry is invalid")

        create_entry(amount, description)
        created_obj = create_entry(amount, description)
        expense_list.update(created_obj)
        return created_obj

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
    sorted(expense_list)
    print(expense_list)

