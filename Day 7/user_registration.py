from sys import exit


class User:
    def __init__(self, name, email, password):
        """
        Initialize a User class with name, email, and password.

        Args:
            name (str): The user's name.
            email (str): The user's email.
            password (str): The user's password.
        """
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        """
        Return a string representation of the User.

        Returns:
            str: A string containing the user's name and email.
        """
        return f"Name: {self.name}\nEmail: {self.email}"


def main():
    """
    Main program to interactively register users and manage the user database.
    """
    user_database = []
    while True:
        add_users = input("Do you want to register a user? (yes/no): ")
        if add_users.lower() == "no":
            exit()
        elif add_users.lower() == "yes":
            user_registration(user_database)
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def user_registration(database):
    """
    Register a new user and add them to the user database.

    Args:
        database (list): The list to store registered users.

    This function collects user information, validates the email, and ensures it is unique.
    """
    while True:
        new_user = register_user()
        if email_is_unique(new_user.email, database):
            database.append(new_user)
            print("Registration successful!")
        else:
            print("This email is already registered. Please use a different email.")

        register_another_user = input("Do you want to register another user? (yes/no)")
        if register_another_user.lower() != 'yes':
            break


def register_user():
    """
    Prompt the user for information and create a new User object.

    Returns:
        User: A User object with user information.
    """
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Create a password: ")
    return User(name, email, password)


def email_is_unique(email, database):
    """
    Check if the provided email is unique among registered users.

    Args:
        email (str): The email to be checked.
        database (list): The list of registered users.

    Returns:
        bool: True if the email is unique, False if it is already registered.
    """
    return not any(user.email == email for user in database)


if __name__ == "__main__":
    main()
