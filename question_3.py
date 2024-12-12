# question(i) 
def age_eligibility():
    age = int(input("Enter your age:"))
    if age >= 18:
        print('You are eligible.')
    else:
        print('You are not eligible.')
age_eligibility()       


# question(ii) 
def grade_students(mark):
    if 90 <= mark <= 100:
        return ' A'
    elif 80 <= mark < 90:
        return ' B'
    elif 70 <= mark < 80:
        return 'C'
    elif 60 <= mark < 70:
        return 'D'
    elif 0 <= mark < 60:
        return 'F'
    else:
        return 'Invalid mark'

# (iii) Testing with a mark of 85
mark = 85
print(f"The grade for {mark} is: {grade_students(mark)}")

# (v) Enhance the function 
def grade_students_with_message(mark):
    grade = grade_students(mark)
    messages = {
        'A': "Excellent",
        'B': "Excellent",
        'C': "Good",
        'D': "Satisfactory",
        'F': "Needs Improvement"
    }
    if grade in messages:
        return f"Grade: {grade}, Message: {messages[grade]}"
    else:
        return grade


print(grade_students_with_message(85))  
print(grade_students_with_message(50))  
print(grade_students_with_message("xyz"))  
