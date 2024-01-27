def calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app):
    PIZZA_COST = 12.0
    DELIVERY_COST = 2.5
    APP_DISCOUNT = 0.25
    TUESDAY_DISCOUNT = 0.5

    try:
        num_pizzas = int(num_pizzas)
    except ValueError:
        print("Please enter a valid number for the pizzas.")
        return

    # Calculations
    total_pizza_cost = num_pizzas * PIZZA_COST

    if is_tuesday == 'n':
        total_pizza_cost *= (1 - TUESDAY_DISCOUNT)

    if delivery_required == 'y':
        if num_pizzas >= 5:
            total_delivery_cost = 0.0
        else:
            total_delivery_cost = DELIVERY_COST
    else:
        total_delivery_cost = 0.0

    total_price = (total_pizza_cost + total_delivery_cost) * (1 - (APP_DISCOUNT if used_app == 'y' else 0))

    # Display result
    print(f"\nTotal Price: £{total_price:.2f}")

def main():
    print("BPP Pizza Price Calculator")
    print("==========================\n")

    num_pizzas = input("How many pizzas ordered? ")
    delivery_required = input("Is delivery required? (Y/N) ").lower()
    is_tuesday = input("Is it Tuesday? (Y/N) ").lower()
    used_app = input("Did the customer use the app? (Y/N) ").lower()

    calculate_total_price(num_pizzas, delivery_required, is_tuesday, used_app)

if __name__ == "__main__":
    main()