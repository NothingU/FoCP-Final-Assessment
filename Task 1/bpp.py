def calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app):
    # Constants
    PIZZA_COST = 12.0
    DELIVERY_COST = 2.5
    APP_DISCOUNT = 0.25
    TUESDAY_DISCOUNT = 0.5

    # Input validation
    while not num_pizzas.isdigit() or int(num_pizzas) < 0:
        print("Please enter a positive integer!")
        num_pizzas = input("How many pizzas ordered? ")

    delivery_required = delivery_required.lower()
    while delivery_required not in ['y', 'n']:
        print('Please answer "Y" or "N".')
        delivery_required = input("Is delivery required? ").lower()

    is_tuesday = is_tuesday.lower()
    while is_tuesday not in ['y', 'n']:
        print('Please answer "Y" or "N".')
        is_tuesday = input("Is it Tuesday? ").lower()

    used_app = used_app.lower()
    while used_app not in ['y', 'n']:
        print('Please answer "Y" or "N".')
        used_app = input("Did the customer use the app? ").lower()

    # Calculations
    total_pizza_cost = float(num_pizzas) * PIZZA_COST

    if is_tuesday == 'y':
        total_pizza_cost *= (1 - TUESDAY_DISCOUNT)

    if delivery_required == 'y':
        if int(num_pizzas) >= 5:
            total_delivery_cost = 0.0
        else:
            total_delivery_cost = DELIVERY_COST
    else:
        total_delivery_cost = 0.0

    total_price = (total_pizza_cost + total_delivery_cost) * (1 - (APP_DISCOUNT if used_app == 'y' else 0))

    # Display result
    print(f"\nTotal Price: £{total_price:.2f}.")

# Main program
print("BPP Pizza Price Calculator")
print("==========================\n")

num_pizzas = input("How many pizzas ordered? ")
delivery_required = input("Is delivery required? ").lower()
is_tuesday = input("Is it Tuesday? ").lower()
used_app = input("Did the customer use the app? ").lower()

calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app)
