def get_student_score() -> float:
    """
    Prompts the user to enter their score, validates input, and returns the numerical score.
    Returns:
        float: The validated numerical score entered by the user.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Error: Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric score.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score.
    Args:
        score (float): The student's numerical score.
    Returns:
        str: The corresponding letter grade.
    """
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
if __name__ == "__main__":
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")
