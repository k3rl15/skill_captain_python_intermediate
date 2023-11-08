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
        return f"Product: {self.name.capitalize()}\nPrice: ${self.price:.2f}\nQuantity: {self.quantity}"


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

    def cart_information(self):
        """
        Display the contents of the cart, including the username and total.

        Prints:
            User name, items in the cart and the details of each product.
        """
        cart_total = 0
        cart_info = f"\nUser Name: {self.user_name}\nItems: {len(self.products)}   Cart:\n"
        for product in self.products:
            cart_info += str(product) + '\n'
            cart_total += product.price * product.quantity
        cart_info += f"Total: ${cart_total:.2f}\n"

        return cart_info


def main():
    product1 = Product("apples", 2.50, 18)
    product2 = Product("banana", 3.10, 15)

    user = Cart("hi")
    user.add_to_cart(product1)
    user.add_to_cart(product2)

    print(user.cart_information())


if __name__ == "__main__":
    main()
