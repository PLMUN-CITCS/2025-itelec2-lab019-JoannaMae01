"""
Enhanced Grade Calculator

This program prompts the user to enter a numerical score, validates the input, 
determines the corresponding letter grade, and displays the result.

Features:
- Function decomposition for modularity
- Input validation to ensure a valid score
- Conditional logic to determine grades
"""

def get_student_score() -> float:
    """
    Prompts the user to enter their score, validates input, and returns a numerical score.

    Returns:
        float: The valid numerical score entered by the user.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid numeric value.")


def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score.

    Args:
        score (float): The student's numerical score.

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
    return 'F'  # No need for "else" since return exits the function


def main():
    """
    Main function to get the student's score, calculate the grade, and display the result.
    """
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")


if __name__ == "__main__":
    main()
