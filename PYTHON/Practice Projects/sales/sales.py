# Initializing the lists with product details
product_code = ['P001', 'P002', 'P003', 'P004', 'P005']
product_name = ['Laptop', 'Smartphone', 'Tablet', 'Smartwatch', 'Monitor']
product_price = [999.99, 499.99, 299.99, 199.99, 149.99]


# Function to display the sales menu
def display_menu():
    # Displaying the welcome title
    print("_" * 35)
    print("Welcome to the Sales Menu!")
    print("_" * 35)

    # Displaying the header
    print("-" * 50)
    print(f"{'Product Code':<15}{'Product Name':<20}{'Product Price':<10}")
    print("-" * 50)

    # Using a for loop to display each row of the table
    for i in range(len(product_code)):  # Looping through the lists
        print(f"{product_code[i]:<15}{product_name[i]:<20}R{product_price[i]:<10.2f}")


# Call the function to display the sales menu
display_menu()

# Prompting the user for the number of items to be purchased
num_items = int(input("\nEnter the number of items you wish to purchase: "))

# Initialize an empty list to store the product
# code and quantity for each purchase
purchased_items = []

# Outer for loop to capture the product code and quantity for each item
for i in range(num_items):
    # Prompting the user for the product code
    code = input(f"\nEnter product code for item {i+1}: ")

    # Search in the product_code list to check if the code exists
    if code in product_code:
        # Find the index of the product code
        index = product_code.index(code)

        # Display product name and price based on the found index
        print(f"Product: {product_name[index]} | Price: R{product_price[index]:.2f}")

        # Prompt for quantity
        quantity = int(input(f"Enter quantity for {code}: "))

        # Append the product code and quantity to the purchased_items list
        purchased_items.append((code, quantity))
    else:
        print(f"Error: Product code {code} does not exist. Please try again.")

# Displaying the user's purchased items
print("\nYour purchased items:")
print(f"{'Product Code':<15}{'Quantity':<10}")
print("-" * 25)
for item in purchased_items:
    print(f"{item[0]:<15}{item[1]:<10}")
