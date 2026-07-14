# PYTHON PROGRAMMING TASK 2: STOCK PORTFOLIO TRACKER

# Panda library to display portfolio as an organised table
import pandas as pd

# Hardcoded dictionary to define stock name and prices
prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 415,
    "NVDA": 875,
}

# Print the title at the start of program
print("=" * 40)
print(" STOCK PORTFOLIO TRACKER ")
print("=" * 40)

portfolio_data = [] # List to record each purchase
total = 0   # Running grand total of all purchases
item_no = 1 # Track current entry number

# Outer loop
# Keeps on asking for stock name until user types 'done'
while True:
    symbol = input("Enter stock name (or done): ").upper()

    # Exit the loop when user types 'done'
    if symbol == "DONE":
        break

    # Invalidate input if the symbol isn't found in the hardcoded dictionary
    if symbol not in prices:
        print("----------------------------------")
        print("Stock Not Found. Please Try Again.")
        print("----------------------------------")
        continue    # Ask for stock name again

    # Inner loop
    # Keeps on asking for quantity until user types a valid positive number
    while True:
        try:
            qty = int(input(f"Quantity of {symbol}: "))

            # Invalidate user input if zero or negative quantities is given
            if qty <= 0:
                print("------------------------------------")
                print("Please enter a valid numerical value")
                print("------------------------------------")
                continue    # Ask for valid quantity again
            break   # Exit inner loop when valid positive number is given
        except ValueError:  # Triggered when non-numerical value is given (e.g. alphabetical letters)
            print("------------------------------------")
            print("Please enter a valid numerical value")
            print("------------------------------------")
            continue    # Ask for valid quantity again

    price = prices[symbol]  # Look up stock's prices
    total_value =  price * qty  # Calculate the value of current purchase (price * quantity)
    total += total_value    # Add it to the running grand total

    # Save current purchase (to be used for the table later on)
    portfolio_data.append({
        "No.": item_no,
        "Stock": symbol,
        "Quantity": qty,
        "Price": price,
        "Total Value": total_value})
    
    # Increment item number (by 1) to move to next entry
    item_no += 1
    
    # Print to confirm purchase to the user
    print(f"{symbol} x {qty} = $ {total_value}")

# Convert the list of purchases into a pandas DataFrame (table)
df = pd.DataFrame(portfolio_data)

# Print the final portfolio summary table
print("\n" + "=" * 40)
print(" PORTFOLIO SUMMARY ")
print("=" * 40)
print(df.to_string(index=False)) # Print the table without the default row index

# Print the grand total with comma separators and 2 decimals
print(f"\nTOTAL INVESTMENT VALUE: ${total:,.2f}\n")

# Ask the user if they'd like to save the results to a txt file
save = input("Save results into a file? (yes/no): ").lower()

# If user types 'yes', a txt file containing the portfolio summary will be created
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("=" * 40 + "\n")
        file.write(" STOCK PORTFOLIO TRACKER \n")
        file.write("=" * 40 + "\n")
        file.write(df.to_string(index=False))
        file.write("\n")
        file.write(f"\nTOTAL INVESTMENT VALUE: ${total:,.2f}\n")
        print("\nResults saved in portfolio_summary.txt")






