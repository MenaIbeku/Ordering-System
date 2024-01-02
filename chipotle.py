# Author   : Mena Ibeku
# Email    : cibeku@umass.edu
# Spire ID : 34151261


def get_protein(order):
    menu={"chicken":2.5,"steak":3.5,"barbacoa":3.5,"carnitas":3.0,"veggies":2.5}
    
    for i in menu:
        if i in order:
            return menu[i]
        else:
            continue
    if i not in order:
        return 0
def get_rice(order):
    menu={"white":2.5,"brown":3.5}
    
    for i in menu:
        if i in order:
            return menu[i]
        else:
            continue
    if i not in order:
        return 0
def get_beans(order):
    menu={"black":2.5,"pinto":2.5}
    
    for i in menu:
        if i in order:
            return menu[i]
        else:
            continue
    if i not in order:
        return 0
def get_burrito(order):
    menu={True:2.0,False:0}
    for i in menu:
        if i in order:
            return menu[i]
        else:
            continue
def get_toppings(order):
    menu={"guacamole":2.75,"tomato salsa":2.5,"chili corn salsa":1.75,"tomatillo green chili salsa":2.0,"sour cream":2.5,"fajita veggies":2.5,"cheese":2.0,"queso blanco":2.75}
    sum=0
    for i in menu:
        if i in order:
            if ("veggies" in order) and (i=="guacamole"):
                sum+=0
            elif ("veggies" in order) and (i=="fajita veggies"):
                sum+=0
            else:
                sum+=menu[i]
        else:
            continue
    if sum==0:
        return 0
    else:
        return sum
def apply_discount(order,total_price):
    discount_code = {"MAGIC":0.95*total_price,"SUNDAYFUNDAY":0.9*total_price,"FLAT3":total_price-3}
    for i in discount_code:
        if i in order:
            return discount_code[i]
    if i not in order:
        return total_price
def approximate_time(order):
    delivery_time={"amherst":15,"north amherst":15,"south amherst":15,"hadley":15,"northampton":30,"south hadley":30,"belchertown":30,"sunderland":30,"holyoke":45,"greenfield":45,"deerfield":45,"springfield":45}
    for i in delivery_time:
        if i in order:
            return delivery_time[i]
def generate_invoice(order):
    
    customer_name = order[0]
    protein_price = get_protein(order)
    rice_price = get_rice(order)
    beans_price = get_beans(order)
    burrito_price = get_burrito(order)
    toppings_price = get_toppings(order)
    total_price = protein_price + rice_price + beans_price + burrito_price + toppings_price
    discount_price = apply_discount(order, total_price)
    approximate_delivery_time = approximate_time(order)
    toppings = order[7:]
    print(f"Welcome to Chipotle Mexican Grill Hadley, {customer_name}.")
    print("Your invoice is displayed below:")
    print(f"Protein: {order[3]} - ${protein_price}")
    print(f"Rice: {order[4]} rice - ${rice_price}")
    print(f"Beans: {order[5]} beans - ${beans_price}")
    print(f"Burrito: {'Yes' if order[6] else 'No'} - ${burrito_price}")
    print(f"Toppings: {', '.join(toppings)} - ${toppings_price}")
    print(f"Subtotal: ${total_price}")
    print(f"Discount Code: {order[2]}")
    print(f"Total: ${discount_price}")
    print(f"You Save: ${total_price - discount_price}")
    print(f"Your order will be ready in {approximate_delivery_time} minutes.")
    print("Enjoy your meal and have a good day!")


mena="He is too good"
print(mena.split())