def get_student_score() -> float:
    """
    Prompts the user for their score, ensuring valid input.
    Returns the score as a float.
    """
    while True:
        try:
            # Prompting user for score input
            score = float(input("Enter your score: "))
            # Validate the score is within the 0 to 100 range
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            # Catching invalid input (non-numeric)
            print("Invalid input. Please enter a valid numerical score.")

def calculate_grade(score: float) -> str:
    """
    Calculates the grade based on the score.
    Returns the grade as a string ('A', 'B', 'C', 'D', 'F').
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    return 'F'

def main():
    """
    Main function to handle the grade calculation process.
    """
    # Step 1: Get the student's score
    score = get_student_score()
    
    # Step 2: Calculate the grade based on the score
    grade = calculate_grade(score)
    
    # Step 3: Output the result to the user
    print(f"Your Grade is: {grade}")

# Calling the main function to run the program
if __name__ == "__main__":
    main()
