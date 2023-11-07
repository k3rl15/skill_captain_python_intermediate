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

    def __str__(self):
        """
        Return the product's information.

        Returns:
            str: A formatted string with the product details.
        """
        return f"Product: {self.name}\nPrice: ${self.price:.2f}\nQuantity: {self.quantity}"


class Cart:
    def __init__(self, user_name):
        """
        Initialize a new Cart.

        Args:
            user_name (str): The name of the user.
        """
        self.user_name = user_name
        self.products = []

    def add_to_cart(self, product):
        """
        Add a product to the cart.

        Args:
            product (Product): The product to be added to the cart.
        """
        self.products.append(product)

    def remove_from_cart(self, product_name):
        """
        Remove product from the cart.

        Args:
            product_name (str): The name of the product to be removed.
        """
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                break

    def display_cart(self):
        """
        Display the contents of the cart, including the username and total.

        Prints:
            User name, items in the cart and the details of each product.
        """
        cart_total = 0
        print(f"\nUser Name: {self.user_name}\nCart            Items:{len(self.products)}")
        for product in self.products:
            print(product)
            cart_total += product.price * product.quantity
        print(f"Total: ${cart_total:.2f}")


# Example usage:
product1 = Product("Mangoes", 5.95, 5)
product2 = Product("Tomatoes", 1.09, 3)
product3 = Product("Chives", .65, 10)

user = Cart("Knight")

user.add_to_cart(product3)
user.add_to_cart(product1)
user.add_to_cart(product2)

user.display_cart()

user.remove_from_cart("Chives")
user.display_cart()
