# Create a main function to enter an order
def main():
    #Coffee price
    coffee_price = 5
    #Muffin Price
    muffin_price = 4
    #Tax Price
    tax_rate = 0.06
    print("Welcome to the Coffee Shop!")
    # Amount input
    coffee_qty = int(input("How many coffees would you like to order? "))
    muffin_qty = int(input("How many muffins would you like to order? "))
    #Print receipt of the order
    print_receipt(coffee_qty, muffin_qty, coffee_price, muffin_price, tax_rate)

#Calculate the receipt amount with a tax of 6% and print Coffee and Muffin prices.
def print_receipt(coffee_qty, muffin_qty, coffee_price, muffin_price, tax_rate):
    # Total without including the tax
    subtotal = (coffee_qty * coffee_price) + (muffin_qty * muffin_price)
    #Total tax for the order
    tax_amount = subtotal * tax_rate
    #Total of the order with tax
    total_cost = subtotal + tax_amount
    print("\n----- Coffee Shop Receipt -----")
    # Every time you enter a number higher than 0, it will print the line with the order detail.
    if coffee_qty > 0:
        print(f"{coffee_qty} Coffee(s) at ${coffee_price} each: ${coffee_qty * coffee_price}")
    if muffin_qty > 0:
        print(f"{muffin_qty} Muffin(s) at ${muffin_price} each: ${muffin_qty * muffin_price}")
    print(f"Subtotal: ${subtotal}")
    print(f"Tax (6%): ${tax_amount}")
    print(f"Total: ${total_cost}")
    print("-------------------------------\n")
# Using this if statement allows the current script to run as the main program.
if __name__ == "__main__":
    main()
