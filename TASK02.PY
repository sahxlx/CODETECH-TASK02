def calculate_gpa(average_grade):
    if average_grade >= 90:
        return 'A', 4.0
    elif average_grade >= 80:
        return 'B', 3.0
    elif average_grade >= 70:
        return 'C', 2.0
    elif average_grade >= 60:
        return 'D', 1.0
    else:
        return 'F', 0.0

def main():
    grades = []
    
    while True:
        subject = input("Enter the subject name (or type 'done' to finish): ")
        if subject.lower() == 'done':
            break
        
        while True:
            try:
                grade = float(input(f"Enter the grade for {subject}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")
    
    if not grades:
        print("No grades entered.")
        return
    
    average_grade = sum(grades) / len(grades)
    letter_grade, gpa = calculate_gpa(average_grade)
    
    print(f"Average Grade: {average_grade:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa:.2f}")

if __name__ == "__main__":
    main()