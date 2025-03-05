def get_student_score() -> float:
    """
    Handles user input to obtain the student's score.
    
    Returns:
        float: The numerical score entered by the user.
    """
    while True:
        try:
            score = float(input("Enter your score (0-100): "))
            if 0 <= score <= 100:
                return score
            print("Error: Please enter a score between 0 and 100.")
        except ValueError:
            print("Error: Invalid input. Please enter a numerical value.")

def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score.

    Parameters:
        score (float): The student's numerical score.

    Returns:
        str: The corresponding letter grade.
    """
    grade_boundaries = {
        (90, 100): "A",
        (80, 89): "B",
        (70, 79): "C",
        (60, 69): "D",
        (0, 59): "F",
    }
    
    for (low, high), grade in grade_boundaries.items():
        if low <= score <= high:
            return grade

def display_grade(grade: str):
    """
    Displays the student's letter grade.

    Parameters:
        grade (str): The letter grade to display.
    """
    print(f"Your Grade is: {grade}")

def main():
    """Main program flow for grade calculation."""
    student_score = get_student_score()
    grade = calculate_grade(student_score)
    display_grade(grade)

if __name__ == "__main__":
    main()
