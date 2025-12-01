student_results = []

def calculate_grade(marks):
    if marks >= 90:
        return "A+", "Outstanding performance!"
    elif marks >= 80:
        return "A", "Excellent work!"
    elif marks >= 70:
        return "B", "Good job, keep improving."
    elif marks >= 60:
        return "C", "Fair, but needs more effort."
    elif marks >= 50:
        return "D", "Passed, but can do better."
    else:
        return "F", "Failed. Needs improvement."

while True:
    name = input("\nEnter student name: ")
    num_subjects = int(input("Enter number of subjects: "))
    
    marks = []
    for i in range(num_subjects):
        score = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(score)
    
    average = sum(marks) / num_subjects
    grade, comment = calculate_grade(average)
    
    student_results.append({
        "Name": name,
        "Marks": marks,
        "Average": round(average, 2),
        "Grade": grade,
        "Comment": comment
    })
    
    print(f"\n{name}'s Result:")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print(f"Comment: {comment}")
    
    choice = input("\nAdd another student? (y/n): ").lower()
    if choice != 'y':
        break

print("\n===== All Student Results =====")
for s in student_results:
    print(f"{s['Name']} -> Avg: {s['Average']} | Grade: {s['Grade']} | {s['Comment']}")
