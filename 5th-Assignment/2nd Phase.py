def check_voting_eligibility():
    age = int(input("Enter your age: "))
    
    if age >= 18:
        nationality = input("Do you have a nationality of 'Pakistani'? (yes/no): ").strip().lower()
        if nationality == 'yes':
            print("You are eligible to vote.")
        else:
            print("Please obtain a valid ID to vote.")
    else:
        print("You are not eligible to vote yet.")

# Run the function
check_voting_eligibility()
