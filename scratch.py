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

#update("Shoes", 23.14)
#edge case
#update(str(13), "stop sign")
#update("Water Bottle", 7.99)
#delete("Hippo")
print(bag.keys())

