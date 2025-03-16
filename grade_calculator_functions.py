# grade_calculator_functions.py

"""
This module contains a simple program to calculate a student's letter grade
based on their numerical score. It prompts the user for input, validates the
score, and then returns the appropriate grade.
"""

def get_student_score() -> float:
    """
    Prompts the user to input their score and ensures it is a valid number.

    Returns:
        float: The student's score as a numerical value.
    """
    while True:
        try:
            score = float(input("Enter your score: "))  # Try to convert the input to a float
            if 0 <= score <= 100:
                return score  # Return the score if it is within the valid range
            print("Score must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the score.

    Args:
        score (float): The numerical score to evaluate.

    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'

# Main Program Flow
def main():
    """
    Main function to get the student's score and calculate the grade.
    """
    score = get_student_score()  # Get the score from the user
    grade = calculate_grade(score)  # Calculate the grade
    print(f"Your Grade is: {grade}")  # Display the grade

# If the script is being run directly, call the main function
if _name_ == "_main_":
    main()