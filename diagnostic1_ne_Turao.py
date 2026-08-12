print ("Hello and welcome to the checkout system of HypeKicks!")

def calculate_checkout(cart_total, shipping_speed): 
    speed = shipping_speed.lower()
    if speed == "express":
        shipping = 20
    elif speed == "overnight":
        shipping = 35
    elif speed == "standard" and cart_total >= 100:
        shipping = 0
    elif speed == "standard":
        shipping = 10
    else:
        print("Error")
        shipping = 0
    return shipping

def calculate_final_bill(cart_total, shipping_cost):
    final_bill = cart_total + shipping_cost
    return final_bill

if __name__ == "__main__":
    cart_total = float(input("Enter cart total: "))
    shipping_speed = input("Enter shipping speed (express, overnight, standard): ")
    shipping_cost = calculate_checkout(cart_total, shipping_speed)
    final_bill = calculate_final_bill(cart_total, shipping_cost)
    print(final_bill) 
    print("Thank you for shopping with HypeKicks!")
