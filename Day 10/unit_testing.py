import unittest
from cart_testing import Product, Cart


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product1 = Product("apples", 2.50, 18)
        self.test_display = "Product: Apples\nPrice: $2.50\nQuantity: 18"

    def test_product_information(self):
        self.display = self.product1.__str__()
        self.assertEqual(self.test_display, self.display)


class TestCart(unittest.TestCase):
    def setUp(self):
        self.product1 = Product("apples", 2.50, 18)
        self.product2 = Product("banana", 3.10, 15)
        self.user_cart = Cart("Mowgli")

    def test_add_to_cart(self):
        self.user_cart.add_to_cart(self.product1)
        self.user_cart.add_to_cart(self.product2)

        self.assertIn(self.product1, self.user_cart.products)
        self.assertIn(self.product2, self.user_cart.products)

    def test_remove_from_cart(self):
        self.user_cart.add_to_cart(self.product1)
        self.user_cart.add_to_cart(self.product2)

        self.user_cart.remove_from_cart("banana")

        self.assertNotIn(self.product2, self.user_cart.products)

    def test_cart_info(self):
        self.user_cart.add_to_cart(self.product1)
        self.user_cart.add_to_cart(self.product2)
        test_display = ("\nUser Name: Mowgli\nItems: 2   Cart:\nProduct: Apples\nPrice: $2.50\n"
                        "Quantity: 18\nProduct: Banana\nPrice: $3.10\nQuantity: 15\nTotal: $91.50\n")

        self.assertEqual(self.user_cart.cart_information(), test_display)


if __name__ == "__main__":
    unittest.main()
