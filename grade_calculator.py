"""
Student Grade Calculator
Author: Junrey C. Roxas
Course: Software Engineering
Section: IT3R10
"""

def get_valid_score(prompt: str) -> float:
    while True:
        val = input(prompt).strip()
        try:
            score = float(val)
            if 0.0 <= score <= 100.0:
                return score
            print("[Error] Score must be between 0.00 and 100.00.")
        except ValueError:
            print("[Error] Please enter a valid numerical score.")

def calculate_grade(quiz: float, assignment: float, midterm: float, final_exam: float) -> float:
    return (quiz * 0.25) + (assignment * 0.15) + (midterm * 0.30) + (final_exam * 0.30)

def get_transmuted_grade(score: float) -> tuple[str, str]:
    if score >= 98.0: return "1.00", "Passed (Excellent)"
    elif score >= 95.0: return "1.25", "Passed (Very Good)"
    elif score >= 92.0: return "1.50", "Passed (Very Good)"
    elif score >= 89.0: return "1.75", "Passed (Good)"
    elif score >= 86.0: return "2.00", "Passed (Good)"
    elif score >= 83.0: return "2.25", "Passed (Fair)"
    elif score >= 80.0: return "2.50", "Passed (Fair)"
    elif score >= 77.0: return "2.75", "Passed"
    elif score >= 75.0: return "3.00", "Passed"
    else: return "5.00", "Failed"

def main():
    print("=== Student Grade Calculator ===")
    student_name = input("Enter Student Name: ").strip()
    student_id = input("Enter Student ID / Section: ").strip()
    
    quiz = get_valid_score("Enter Quiz Score (25%): ")
    assignment = get_valid_score("Enter Assignment Score (15%): ")
    midterm = get_valid_score("Enter Midterm Exam Score (30%): ")
    final_exam = get_valid_score("Enter Final Exam Score (30%): ")
    
    final_grade = calculate_grade(quiz, assignment, midterm, final_exam)
    gpa, remarks = get_transmuted_grade(final_grade)
    
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
    print(f" Final Grade Output: {final_grade:.2f}% | Scale: {gpa} ({remarks})")
    print("=" * 54)

if __name__ == "__main__":
    main()
