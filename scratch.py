from datetime import datetime as dt
from pprint import pprint
bag = {
    "Camera": {
        "model": "Sony a7 V",
        "manufacture": "Sony",
        "price": 2898.00
    },

    "Book": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "published": "July 11,1960"
    }, 
    
    "Watch": {
        "model": "museum classic",
        "manufacture": "mavado",
        "year": 2016
    }
}

def update(item, price):
    if not isinstance(item, str):
        print(f"{item} is not a valid entry.")
    if not isinstance(price, float):
        print(f"{price} is not a valid entry.")
    elif not isinstance(price, float) and not isinstance(item, str):
        print(f"{item} is not a valid entry.")
        print(f"{price} is not a valid entry.")
    else:
        bag.update({item: price})
    return bag


def delete(item):
    if item in bag:
        del bag[item]
        print(item, "was deleted")
    else:
        print(item, "is not in your bag")


def create_order(item, description):
    today = dt.now()
    id_counter = lambda x: x + 1
    order_template = {
        "Item" : item,
        "Description" : description,
        "ID" : id_counter(0),
        "Time Stamp" : today.strftime("%Y-%m-%d")
    }
    return order_template

def add_to_bag(item, description):
    if not isinstance(item, str):
        print(f"{item} is not a valid entry")
    elif not isinstance(description, str):
        print(f"{description} is not a valid description")
    else:
        create_order(item, description)
        completed_order = create_order(item, description)
        bag.update(completed_order)
        sorted(bag)
        return create_order(item, description)


#update("Shoes", 23.14)
#edge case
#update(str(13), "stop sign")
#update("Water Bottle", 7.99)
#delete("Hippo")
#print(bag.keys())
add_to_bag("Soda", "Mountain DeV energy drink: It's for coding")
#add_to_bag("", "Mountain DeV energy drink: It's for coding")
pprint(bag, width=80, sort_dicts=False)

