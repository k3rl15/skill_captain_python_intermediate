# Define a base class (superclass) called Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand  # Initialize the brand attribute
        self.model = model  # Initialize the model attribute

    def display_info(self):
        # Method to display vehicle information
        return f"Brand: {self.brand}, Model: {self.model}"


# Define a subclass (Truck) that inherits from the Vehicle class
class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)  # Initialize the brand and model attributes using the superclass's constructor
        self.load_capacity = load_capacity  # Initialize the load_capacity attribute

    def display_info(self):
        # Override the display_info method in the Truck subclass to include load capacity
        vehicle_info = super().display_info()  # Get the vehicle information
        return f"{vehicle_info}, Load capacity: {self.load_capacity}"  # Combine vehicle information with load capacity
