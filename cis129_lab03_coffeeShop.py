def main():
    coffee_price = 5
    muffin_price = 4
    tax_rate = 0.06
    print("Welcome to the Coffee Shop!")
    coffee_qty = int(input("How many coffees would you like to order? "))
    muffin_qty = int(input("How many muffins would you like to order? "))
    print_receipt(coffee_qty, muffin_qty, coffee_price, muffin_price, tax_rate)

def print_receipt(coffee_qty, muffin_qty, coffee_price, muffin_price, tax_rate):
    subtotal = (coffee_qty * coffee_price) + (muffin_qty * muffin_price)
    tax_amount = subtotal * tax_rate
    total_cost = subtotal + tax_amount
    print("\n----- Coffee Shop Receipt -----")
    if coffee_qty > 0:
        print(f"{coffee_qty} Coffee(s) at ${coffee_price} each: ${coffee_qty * coffee_price:.2f}")
    if muffin_qty > 0:
        print(f"{muffin_qty} Muffin(s) at ${muffin_price} each: ${muffin_qty * muffin_price:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax (6%): ${tax_amount:.2f}")
    print(f"Total: ${total_cost:.2f}")
    print("-------------------------------\n")

if __name__ == "__main__":
    main()
