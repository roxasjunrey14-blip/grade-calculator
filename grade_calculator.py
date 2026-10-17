"""
Student Grade Calculator
Author: Junrey C. Roxas
Course: Software Engineering
Section: IT3R10
Instructor: Alyssa Mae Libe
Institution: University of Science and Technology of Southern Philippines (USTP)
"""

def get_valid_score(prompt: str) -> float:
    """Prompt the user for a valid score between 0.00 and 100.00."""
    while True:
        val = input(prompt).strip()
        try:
            score = float(val)
            if 0.0 <= score <= 100.0:
                return score
            print("[Error] Score must be between 0.00 and 100.00. Please try again.")
        except ValueError:
            print("[Error] Invalid input. Please enter a numerical score.")

def calculate_grade(quiz: float, assignment: float, midterm: float, final_exam: float) -> float:
    """
    Computes final grade using standard weighted components:
    - Quizzes: 25%
    - Assignments / Lab Activities: 15%
    - Midterm Examination: 30%
    - Final Examination: 30%
    """
    return (quiz * 0.25) + (assignment * 0.15) + (midterm * 0.30) + (final_exam * 0.30)

def get_transmuted_grade(score: float) -> tuple[str, str, str]:
    """
    Converts numerical grade percentage to Philippine University grading scale (1.00 - 5.00),
    letter rating, and qualitative remarks.
    """
    if score >= 98.0:
        return "1.00", "A+", "Passed (Excellent)"
    elif score >= 95.0:
        return "1.25", "A", "Passed (Very Good)"
    elif score >= 92.0:
        return "1.50", "A-", "Passed (Very Good)"
    elif score >= 89.0:
        return "1.75", "B+", "Passed (Good)"
    elif score >= 86.0:
        return "2.00", "B", "Passed (Good)"
    elif score >= 83.0:
        return "2.25", "B-", "Passed (Fair)"
    elif score >= 80.0:
        return "2.50", "C+", "Passed (Fair)"
    elif score >= 77.0:
        return "2.75", "C", "Passed"
    elif score >= 75.0:
        return "3.00", "C-", "Passed"
    else:
        return "5.00", "F", "Failed"

def print_grade_card(student_name: str, student_id: str, quiz: float, assignment: float,
                     midterm: float, final_exam: float, final_grade: float,
                     gpa: str, letter: str, remarks: str):
    """Displays structured official grade report card."""
    print("\n" + "=" * 54)
    print("            OFFICIAL GRADE REPORT CARD            ")
    print("=" * 54)
    print(f" Student Name : {student_name}")
    print(f" Student ID   : {student_id}")
    print("-" * 54)
    print(f"  Component            | Weight | Score  | Weighted")
    print("-" * 54)
    print(f"  Quizzes              |  25%   | {quiz:6.2f} | {quiz * 0.25:6.2f}")
    print(f"  Assignments/Acts     |  15%   | {assignment:6.2f} | {assignment * 0.15:6.2f}")
    print(f"  Midterm Examination  |  30%   | {midterm:6.2f} | {midterm * 0.30:6.2f}")
    print(f"  Final Examination    |  30%   | {final_exam:6.2f} | {final_exam * 0.30:6.2f}")
    print("-" * 54)
    print(f" Final Weighted Grade : {final_grade:6.2f}%")
    print(f" Numerical Rating     : {gpa} ({letter})")
    print(f" Academic Remarks     : {remarks}")
    print("=" * 54 + "\n")

def run_calculator():
    print("\n" + "#" * 54)
    print("    WELCOME TO THE STUDENT GRADE CALCULATOR SYSTEM    ")
    print("#" * 54)
    
    student_name = input("\nEnter Student Full Name : ").strip()
    while not student_name:
        student_name = input("Name cannot be empty. Please enter Student Full Name: ").strip()
        
    student_id = input("Enter Student ID / Section: ").strip()
    if not student_id:
        student_id = "IT3R10"
        
    print("\n--- Enter Assessment Scores (0.00 - 100.00) ---")
    quiz = get_valid_score("1. Quizzes Average Score (25%)       : ")
    assignment = get_valid_score("2. Assignments / Lab Score (15%)     : ")
    midterm = get_valid_score("3. Midterm Exam Score (30%)          : ")
    final_exam = get_valid_score("4. Final Exam Score (30%)            : ")
    
    final_grade = calculate_grade(quiz, assignment, midterm, final_exam)
    gpa, letter, remarks = get_transmuted_grade(final_grade)
    
    print_grade_card(student_name, student_id, quiz, assignment, midterm, final_exam, final_grade, gpa, letter, remarks)

def main():
    while True:
        run_calculator()
        choice = input("Do you want to calculate grades for another student? (y/n): ").strip().lower()
        if choice not in ('y', 'yes'):
            print("\nThank you for using the Student Grade Calculator. Goodbye!\n")
            break

if __name__ == "__main__":
    main()
