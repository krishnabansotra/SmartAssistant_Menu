#Hotel Menu project

menu = {
    'Pizza' : 80,
    'Pasta': 40,
    'Burger' : 60,# (defiing the hotel menu)
    'Salad': 120,
    'Coffe' : 150,
    'French Fries' : 100,
}

#Greet
print("Welcome to Student cafe")
print("Pizza : Rs80\nPasta : Rs40\nBurger : Rs60\nSalad : Rs120\nCoffe : Rs150\nFrench Fries : Rs100")

order_total = 0

item1 = input("Enter the name of dish you want to order = ").capitalize()

if item1 in menu :
    order_total += menu[item1]
    print(f"Your item {item1} has been added to your order. . . . .")

else:
    print(f"Order item {item1} is not avilable yet !\n Please Order something else")

another_order1 = input("Do you want to add another item ? (Yes / No )").capitalize()
if another_order1 == "Yes":
    item2 =  input("Enter the name of your 2nd dish you want to order = ")
    if item2 in menu:
        order_total += menu[item2]
        print(f"Orderd item {item2} is added to to your order. . . . . ")
    else:
        print(f"Ordered item {item2} is yet not avilable !")

print(f"The Total amount of item is {order_total}: ")
print("\n Thankyou for Order \n Your dish is ordered wait few minutes. . . . ")