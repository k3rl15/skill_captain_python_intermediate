from string import ascii_uppercase
from random import choices


def main():
    """
    Main function to generate unique names and save them to a file.
    """
    number_names = generate_user_input()
    names_generated = generate_unique_names(number_names)
    save_name_to_file(names_generated, 'character_names.txt')


def generate_user_input():
    """
    Prompt the user for the number of characters names to generate.

    Returns:
        int: The number of character names to generate.
    """
    while True:
        try:
            num_names = int(input("Enter the number of character names to generate: "))
            if num_names <= 0:
                print("Please input a positive number.")
            else:
                return num_names
        except ValueError:
            print("Invalid input. Please input a positive number.")


def generate_unique_names(num):
    """
    Generate unique character names.

    Args:
        num (int): The number of character names to generate.

    Returns:
        set: A set of unique character names.
    """
    unique_names = set()
    while len(unique_names) < num:
        name = generate_random_name()
        unique_names.add(name)
    return unique_names


def generate_random_name():
    """
    Generate a random three-syllable character name.

    Returns:
        str: A random character name consisting of three uppercase letters.
    """
    return ''.join(choices(ascii_uppercase, k=3))


def save_name_to_file(names, filename):
    """
    Save generated character to a text file

    Args:
        names (set): A set of character names to be saved.
        filename (str): The name of the output file.
    """
    try:
        with open(filename, 'w') as file:
            for name in names:
                file.write(name + '\n')
    except FileNotFoundError:
        print("File not found!")


if __name__ == '__main__':
    main()
