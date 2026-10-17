# Student Grade Calculator

**Author:** Junrey C. Roxas  
**Section:** IT3R10 (R10 Night Class - Software Engineering)  
**Instructor:** Alyssa Mae Libe  
**Course:** Software Engineering  
**Institution:** University of Science and Technology of Southern Philippines (USTP)  
**Repository:** [https://github.com/roxasjunrey14-blip/grade-calculator](https://github.com/roxasjunrey14-blip/grade-calculator)

---

## 📌 Project Overview
The **Student Grade Calculator** is a modular Python command-line application engineered to compute accurate weighted academic grades. It implements strict input verification, weighted evaluation breakdowns, and converts numerical results into the Philippine collegiate grading scale (1.00 to 5.00) alongside letter marks and pass/fail remarks.

---

## ⚙️ Key Features
- **Input Validation:** Handles non-numeric entries gracefully and enforces valid range (`0.00` - `100.00`).
- **Standard Assessment Weighting:**
  - Quizzes: **25%**
  - Assignments / Lab Activities: **15%**
  - Midterm Examination: **30%**
  - Final Examination: **30%**
- **Philippine College Grading Scale (1.00 - 5.00):** Converts weighted percentage into GPA and descriptive remarks (e.g., *Passed (Excellent)*, *Passed (Very Good)*, *Failed*).
- **Official Report Card Summary:** Displays a formatted table with breakdown per assessment component.
- **Continuous Evaluation Loop:** Calculate grades for multiple students in one session.

---

## 🚀 How to Run the Program

### Prerequisites
- Python 3.8 or higher installed on your computer.

### Step-by-Step Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/roxasjunrey14-blip/grade-calculator.git
   cd grade-calculator
   ```

2. **Execute the script:**
   ```bash
   python grade_calculator.py
   ```

3. **Follow the on-screen prompts:**
   - Enter student's name and section/ID.
   - Enter the percentage scores for quizzes, assignments, midterm, and final exam.
   - View the generated official report card.

---

## 🌿 Git Version Control & Branching Workflow
This repository was developed using professional Git version control practices:
- **Meaningful Commits:** Commits recorded across multiple days following standard conventional commit conventions.
- **Branching:** Created `feature/grade-output-formatting` to develop enhanced UI/receipt printing.
- **Merge Conflict Resolution:** Branch merged back into `main` with deliberate conflict resolution documented in the commit history.
- **Git Reflection:** Detailed write-up available in [REFLECTION.md](REFLECTION.md).

---

## 📝 Reflection Paper
A copy of the Git reflection paper is included in this repository:
- View the reflection document: [REFLECTION.md](REFLECTION.md)
