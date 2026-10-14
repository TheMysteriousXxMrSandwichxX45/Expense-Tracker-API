from datetime import datetime as dt


""" I wanted to create a seperate schema for the entry so it's more organized.
I also wanted to pracice importing functions from other files as well."""

def create_entry(amount, description):
    date = dt.strftime("%Y-%m-%d")
    id = lambda x: x + couter
    couter = 0
    entry = {
    "Description" : description,
    "Amount": amount,
    "Date": date,
    "ID": id(0)
}
    return entry
        
    
class Tag(object):
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = amount
        self.category = category

    def entertainment(self, description, category):
        self.description = description
        self.category = category

    def business(self, description, category):
        self.description = description
        self.category = category

    def food(self, description, category):
        self.description = description
        self.category = category