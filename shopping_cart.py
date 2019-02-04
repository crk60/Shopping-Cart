# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# TODO: write some Python code here to produce the desired functionality...




#Set up stuff is up here
import datetime as dt
checkout_start = dt.datetime.now()
taxr = 0.06 #washington DC has sucky taxes

#Pricing formatting found on github repository / from groceries exercise

def to_usd(myprice):
    return "${0:,.2f}".format(myprice)

#Input Section

#I was confused as to how the input function actually worked so I looked here
#https://www.w3schools.com/python/ref_func_input.asp

#x = input("Enter a ID Code")
#print('This is the ID you selected ' + x)

selected_ids = []

while True:
    selected_id = input("Please input a product identifier: ") #> "9" (string)
    if selected_id == "DONE":
        break
    else:
        selected_ids.append(selected_id)


#Begin Reciept:

print("~~~~~~~~~~~~~~~~~")
print("Lushious Legumes Grocery")
print("www.lushiouslegumes.com")
print("~~~~~~~~~~~~~~~~~")
print("CHECKOUT AT:" + checkout_start.strftime("%Y-%m-%d %I:%M %p"))


x = 1



""" while x < 5:
   y = input("Please input a product id: ")
   print(y)
   print(x)
   x = x + 1 """

running_total = 0

# I got really confused on the last bit from class - I thought we were setting up the input section. I had to reference the screencast to figure out that we were in fact building out the final list, and there is a whole other "while" function for inputs. 
# After referencing the screencast I moved our code to the below "for" loop and tried to recreat the while loop in the input section

print("SELECTED PRODUCTS:")

for selected_id in selected_ids:
      matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
      matching_product = matching_products[0]
      subtotal_price = subtotal_price + matching_product["price"]
print(" ... " + matching_product["name"] + " (" + to_usd(matching_product["price"]) + ")")





print("THE TOTAL PRICE IS: " + str(running_total))