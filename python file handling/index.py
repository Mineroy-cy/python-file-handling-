def read_and_modify_file():
    """
    Reads a file, modifies its content, and writes to a new file.
    Handles errors if the file doesn’t exist or can't be read.
    """
    try:
        # Ask the user for the filename
        filename = input("Enter the filename to read: ")

        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.readlines()

        # Modify the content (Example: Convert text to uppercase)
        modified_content = [line.upper() for line in content]

        # Define the new filename
        new_filename = "modified_" + filename

        # Write the modified content to a new file
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_content)

        print(f"Modified content has been saved to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
