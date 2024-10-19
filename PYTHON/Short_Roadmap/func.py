
_marks = [73, 89, 88, 88, 55]


# function for average
def average_mark(_marks):
    total = sum(_marks)
    one_sub = len(_marks)
    average = total / one_sub
    return average


# grade function
def calc_grade(average):
    if average >= 80:
        grade = 'A'
    elif average >= 70:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >= 50:
        grade = 'D'
    else:
        grade = "F"
    return grade


average = average_mark(_marks)
grade = calc_grade(average)
print(f"Your average SAD mark is {average}")
print(f"Your SAD grade is {grade}")
