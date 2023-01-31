'''
Title: Restaurant Chatbot
Author: Arnab Shrestha
Progam: This program takes up orders, makes reservations, and provides information on items.
Refrences: My Bootcamp 1 Final Project
'''

'''
********************************** Part 1 **********************************
'''

# All the information for food items, dictinary for resturant inventory
inventory = [
  {'order': 1, 'food': 'dumplings', 'price': 6.99, 'spice': 2, 'ingredients': 'ground turkey, spices, flour'},
  {'order': 2, 'food': 'noodles', 'price': 9.99, 'spice': 3, 'ingredients': 'beef, chicken & beef stocking, spices, wheat flour'},
  {'order': 3, 'food': 'rice', 'price': 2.99, 'spice': 0, 'ingredients': 'white rice'},
  {'order': 4, 'food': 'chicken butter', 'price': 11.99, 'spice': 3, 'ingredients': 'white rice, chicken, butter, spices, tomato, onion, heavy cream'},
  {'order': 5, 'food': 'spring rolls', 'price': 5.99, 'spice': 0, 'ingredients': 'rice paper, cucumber, carrots, lettuce, red cabbage, shrimp'},
  {'order': 6, 'food': 'water', 'price': 0, 'spice': 0, 'ingredients': 'water'},
  {'order': 7, 'food': 'coke', 'price': 1.99, 'spice': 0, 'ingredients': 'coke'},
  {'order': 8, 'food': 'sprite', 'price': 1.99, 'spice': 0, 'ingredients': 'sprite'},
  {'order': 9, 'food': 'fanta', 'price': 1.99, 'spice': 0, 'ingredients': 'fanta'},
]

'''
********************************** Part 2 **********************************
'''

print("Welcome to Arnab's Restaurant!\n") # Introduction

# The display for the menu
print("     ***MENU***\n 1. Dumplings      | 6.99\n 2. Noodles        | 9.99\n 3. Rice           | 2.99\n 4. Butter Chicken | 11.99 \n 5. Spring Rolls   | 5.99\n 6. Water          | FREE\n 7. Coke           | 1.99\n 8. Sprite         | 1.99\n 9. Fanta          | 1.99\n")

def order(): # Function for ordering food
  tab = 0.00 # Amount that the user has to pay
  while True:
    try:
      order_choice = input("\nType the number of the item you want to order or the name of the item, and type done when your finished with your order. ") # Allows the user to choose items by numbers or name of item
    except:
      print("Sorry we don't have that order number.")
      
    if order_choice.lower() == 'done':
      break # Breaks out of the while loop

    for i in range(len(inventory)):
      if inventory[i]['food'] == order_choice: # Matches order_choice with a order number
        print(inventory[i]['food'], "added to tab") # Prints the food with that order number
        tab += inventory[i]['price'] # Adds price of the food to tab

  print("Final tab plus taxes is", round(tab * .0825 + tab, 2)) # Adds taxes and rounds the tab with two decimal points
  print("Thank you for dining!")
  exit() # Ends the code
  
'''
********************************** Part 3 **********************************
'''

# Asks users to choose 1 of 3 options
choice = int(input("What would you like to do today?\n\n 1) Order\n 2) Give information on an item\n 3) Make a reservation\n\n (type 1, 2, or 3): "))

if choice == 1: # If user types 1 then the function order() will play
  order()

if choice == 2: # If the user types 2 then they can see more info on an item
  while True:
    info_choice = int(input("\nType the number of the item you want more information on, and type 0 when your ready to order. ")) # Allows the user to select which item they want more info on
    if info_choice == 0: # Once the user is done with looking at information, they can order food
      order()
    elif info_choice > 9:
      print("Sorry we don't have that order number.")

    for i in range(len(inventory)):
      if inventory[i]['order'] == info_choice: # Matches info_choice with a order number
        print("\ninformation on", inventory[i]['food'],":")
        print("Spice level:", inventory[i]['spice'])
        print("Food contains", inventory[i]['ingredients'])

if choice == 3: # If the user types 2 then they can see more info on an item
  reservation = input("\nWhat time would you like to schedule a reservation? (#:##) ") # Gets the time of reservation
  name = input("Under what name do you want your reservation? ") # Gets the name for the reservation
  print("Reservation at", reservation, "for", name, "has been made.\nSee you then!") # Displays final reservation time with the name
  exit()