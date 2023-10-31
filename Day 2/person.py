# Define a Python class Person to represent individuals.
class Person:
    # Constructor to initialize the 'name' and 'age' attributes for a person.
    def __init__(self, name, age):
        self.name = name  # Store the person's name
        self.age = age    # Store the person's age

    # Method to display a person's information
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}yrs")
        print()


# Create 2 instances of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Display information about the 2 individuals
person1.display_info()
person2.display_info()
