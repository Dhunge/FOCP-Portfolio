import random

def check_random_letter(password):
    """Picks a random letter and asks the user to guess it."""
    index = random.randint(0, len(password) - 1)
    guess = input(f"Enter letter at position {index + 1}: ")
    
    # Returns True if correct, False if wrong
    return guess == password[index]

def main():
    password = input("Enter your password: ")
    print()

    if len(password) < 9:
        print("Password too short.")
        return

    # Run the check 3 times
    for i in range(3):
        is_correct = check_random_letter(password)
        
        if is_correct:
            print("Correct\n")
        else:
            print("Incorrect")
            print("Security check failed.")
            return

    print("Security check passed.")

if __name__ == "__main__":
    main()