import re  # Import the 're' module for regular expression operations

def check_password_strength(password):
    """
    Checks the strength of a password based on predefined criteria:
    - Length of at least 8 characters
    - Presence of uppercase letters
    - Presence of lowercase letters
    - Presence of numbers
    - Presence of special characters
    """
    
    # Criteria for password strength
    length_criteria = len(password) >= 8  # Check if password length is at least 8 characters
    uppercase_criteria = re.search(r'[A-Z]', password) is not None  # Check for at least one uppercase letter
    lowercase_criteria = re.search(r'[a-z]', password) is not None  # Check for at least one lowercase letter
    number_criteria = re.search(r'[0-9]', password) is not None  # Check for at least one digit
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None  # Check for at least one special character

    # Initialize strength score and feedback list
    score = 0  # Variable to hold the password strength score
    feedback = []  # List to collect feedback messages
    #The score variable is used to keep track of how many of the password strength criteria the password meets.
    #For each criterion the password meets, the score is incremented by 1.

    # Check each criterion and provide feedback if not met
    if length_criteria:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")#This is the first thing you will see when inputting password

    if uppercase_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")#Then we move to uppercase

    if lowercase_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if number_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one number.")

    if special_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one special character (!@#$%^&*(),.?\":{}|<>).")

    # Determine password strength based on the score
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength = strength_levels[score]

    return strength, feedback

def main():
    """
    Main function to input password from user and check its strength.
    Prints the password strength and provides feedback.
    """
    
    # Input password from user
    password = input("Enter a password to check its strength please: ")

    # Check password strength
    strength, feedback = check_password_strength(password)

    # Print the password strength
    print(f"Password Strength: {strength}")

    # Print feedback if any criteria are not met
    if feedback:
        print("Feedback:")
        for f in feedback:
            print(f" - {f}")

if __name__ == "__main__":
    main()  # Call the main function to run the script
