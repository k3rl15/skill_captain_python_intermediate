try:
    # Attempt to open the 'data.txt' file
    with open('data.txt', 'r') as file:
        line_count = 0

        # Iterate through each line in the file
        for line in file:
            line_count += 1

except FileNotFoundError:
    # Handle exception if file not found
    print("File not found!")

# Print the number of lines in the file
print(f"Total number of lines in the file: {line_count}")
