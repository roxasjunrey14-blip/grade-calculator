# Git Reflection Paper

**Student Name:** Junrey C. Roxas  
**Section:** IT3R10 (R10 Night Class - Software Engineering)  
**Course:** Software Engineering  
**Instructor:** Alyssa Mae Libe  
**Assignment:** Finals Assignment 1: My First Real Repository  

---

## Reflection on Git Problem & Solution

One of the major problems I encountered while working with Git for this assignment was dealing with a merge conflict. When I tried to merge my feature branch back into the main branch, Git flagged a conflict because I had accidentally modified the exact same line of code in both branches-specifically, the final grade output statement. At first, I was confused and unsure how to resolve it safely without breaking the script.

To solve this, I opened the conflicting file in my code editor, where Git clearly marked the conflicting sections using conflict indicators like `<<<<<<<` and `>>>>>>>`. I carefully reviewed both versions, kept the updated formatting from my feature branch, and deleted the unnecessary markers. After saving the file, I ran `git add grade_calculator.py` to stage the resolved file, and then completed the process by running `git commit -m "Resolve merge conflict in output statement"`. This experience taught me how important it is to communicate and track changes carefully, and it gave me confidence in troubleshooting common Git issues independently.
