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
#TypeError: can't multiply sequence by non-int of type 'float'
taxr = 0.06 #washington DC has sucky taxes



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

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Lushious Legumes Grocery")
print("www.lushiouslegumes.com")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("CHECKOUT AT:" + checkout_start.strftime("%Y-%m-%d %I:%M %p"))


x = 1

#  Error recieved in Anaconda prompt:
# File "shopping_cart.py", line 88, in <module>
 #   subtotal_price = subtotal_price + matching_product["price"]
#NameError: name 'subtotal_price' is not defined
# same issue as  matching items variable: will try subtotal_price [0]
#https://www.learnpython.org/en/Variables_and_Types

subtotal_price = 0

#******* The above code was the reason everything kept messing up. A core variable (subtotal_price) needed to be defined, and ina cursory google search I thought it needed to be defined as [0]. 
# The issue with this is that defined subtotal_price as a list, and every equation where it was integrated it should have been an integer and there were countless format or invalid syntax errors
# After messaging Hiep I finally found the error and the rest of my code worked!


# File "shopping_cart.py", line 94, in <module>
 #   subtotal_price = subtotal_price + matching_product["price"]
#TypeError: can only concatenate list (not "float") to list

""" while x < 5:
   y = input("Please input a product id: ")
   print(y)
   print(x)
   x = x + 1 """



# I got really confused on the last bit from class - I thought we were setting up the input section. I had to reference the screencast to figure out that we were in fact building out the final list, and there is a whole other "while" function for inputs. 
# After referencing the screencast I moved our code to the below "for" loop and tried to recreat the while loop in the input section

#Pricing formatting found on github repository / from groceries exercise

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#Error Recieved:TypeError: can only concatenate list (not “float”) to list
# https://stackoverflow.com/questions/19286023/typeerror-can-only-concatenate-list-not-float-to-list

print("SELECTED PRODUCTS:")

for selected_id in selected_ids:
      matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
      matching_product = matching_products[0]
      fetch_price = matching_product["price"]
      subtotal_price = subtotal_price + fetch_price
print(" ... " + matching_product["name"] + " (" + to_usd(fetch_price) + ")")




#Final Equations

total_tax = subtotal_price * taxr

total_price = subtotal_price + total_tax


#Result Print Out

print("THE TOTAL PRICE IS: " + str(subtotal_price))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Subtotal: " + to_usd(subtotal_price))
print('Tax: ' + to_usd(totaltax))
print('Total: ' + to_usd(totalprice))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("See you again real soon!") 

#Kept getting this error with the above code
#  File "shopping_cart.py", line 123, in <module>
#    print("Subtotal: " + to_usd(subtotal_price))
 # File "shopping_cart.py", line 97, in to_usd
  #  return "${0:,.2f}".format(z)
#TypeError: unsupported format string passed to list.__format__

'''print("---------------------------------")
print("SUBTOTAL: " + to_usd(subtotal_price))
print("TAX: " + to_usd(total_tax))
print("TOTAL: " + to_usd(total_price))
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")'''

