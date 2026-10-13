"""
Student Grade Calculator
Author: Junrey C. Roxas
Course: Software Engineering
Section: IT3R10
"""

def calculate_grade(quiz, assignment, midterm, final_exam):
    # Weights: Quizzes 25%, Assignments 15%, Midterm 30%, Final Exam 30%
    weighted_score = (quiz * 0.25) + (assignment * 0.15) + (midterm * 0.30) + (final_exam * 0.30)
    return weighted_score

def main():
    print("=== Student Grade Calculator ===")
    student_name = input("Enter Student Name: ")
    
    quiz = float(input("Enter Quiz Score (0-100): "))
    assignment = float(input("Enter Assignment Score (0-100): "))
    midterm = float(input("Enter Midterm Exam Score (0-100): "))
    final_exam = float(input("Enter Final Exam Score (0-100): "))
    
    final_grade = calculate_grade(quiz, assignment, midterm, final_exam)
    print(f"\nFinal Grade for {student_name}: {final_grade:.2f}")

if __name__ == "__main__":
    main()
