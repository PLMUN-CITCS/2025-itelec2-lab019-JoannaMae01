# Function to handle user input and return the student's score
def get_student_score() -> float:
    """Prompts the user to enter a numerical score and returns it as a float."""
    while True:
        try:
            score = float(input("Enter your score: "))
            # Check if the score is within a valid range (0-100)
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid numerical score.")

# Function to calculate the letter grade based on the score
def calculate_grade(score: float) -> str:
    """Returns the letter grade based on the numerical score."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Main Program Flow
def main():
    # Step 1: Get the student's score
    score = get_student_score()
    
    # Step 2: Calculate the grade
    grade = calculate_grade(score)
    
    # Step 3: Display the grade
    print(f"Your Grade is: {grade}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
