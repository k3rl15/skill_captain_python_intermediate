class Product:
    def __init__(self, name, price, quantity):
        """
        Initialize a new Product.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def product_info(self):
        """
        Display the product's information.
        """
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity in Stock: {self.quantity}\n")


class ProductDatabase:
    def __init__(self):
        """
        Initialize an empty ProductDatabase.
        """
        self.products = []

    def register_product(self, name, price, quantity):
        """
        Register a new product and add it to the database.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.
        """
        product = Product(name, price, quantity)
        self.products.append(product)
        print("Product registered!")

    def find_product(self, name):
        """
        Find and display information for a product by its name.

        Args:
            name (str): The name of the product to find.
        """
        matching_product = [product for product in self.products if product.name == name]
        if matching_product:
            matching_product[0].product_info()
        else:
            print(f"{name} not in the product database.")

    def all_products(self):
        """
        Display information for all products in the database.
        """
        [product.product_info() for product in self.products]
        if not self.products:
            print("Products database empty.")


def main():
    """
    Main function to interact with the Product Registration System.
    """
    product_db = ProductDatabase()
    while True:
        print("""Product Registration System:
    1. Register product
    2. Find a product
    3. Display all products in the database
    4. Exit system""")
        user_input = input("Options (1/2/3/4): ")

        if user_input == '1':
            register(product_db)
        elif user_input == '2':
            find(product_db)
        elif user_input == '3':
            product_db.all_products()
        elif user_input == '4':
            exit()
        else:
            print("Invalid input. Option not available.")
        print()


def register(database):
    """
    Register a new product by collecting details from the user.

    Args:
        database (ProductDatabase): The product database where the product will be registered.
    """
    tries = 3
    while tries > 0:
        try:
            name = input("Enter the product name: ")
            price = float(input("Enter the product price: $"))
            quantity = int(input("Enter the product quantity: "))
            if price > 0 and quantity > 0:
                database.register_product(name, price, quantity)
                return
            else:
                print("Please provide positive numbers.")
        except ValueError:
            print("Invalid input.")
        tries -= 1

    print("Maximum attempts reached. Exiting registration.")


def find(database):
    """
    Find a product in the database by name and display its information.

    Args:
        database (ProductDatabase): The product database to search in.
    """
    name = input("Product Name: ")
    database.find_product(name)


if __name__ == '__main__':
    main()
