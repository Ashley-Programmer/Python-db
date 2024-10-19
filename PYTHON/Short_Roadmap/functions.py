# function without an argument
def greet():
    msg = "Hello"
    nm = "Jake"
    print(f'{msg} {nm}')


greet()


# function with an argument
def greetings(name):
    msg = "Hello"
    print(f"{msg} {name}")
    print("How do you do?")


greetings("Jacob")


def my_func(name, age):
    print(f"I am {name} and I am {age} years old.")
    print("Hello to you all.")


my_func("Ashley Programmer", 24)

print("---------------------------")


def add(x, y):
    result = x + y
    return result


num1 = '2'
num2 = '4'
result = add(int(num1), int(num2))
print(f'The sum is {result}')

print("-------________---------")

# built-in functions
# marks = [55, 33, 22, 11]

# length = len(marks)
# print(f'Length is {length}')
# sum = sum(marks)
# print(f"Sum is {sum}")


def average_mark(marks):
    total = sum(marks)
    subjects_num = len(marks)
    average = total / subjects_num
    return average


def com_grade(average):
    if average >= 80:
        grade = 'A'
    elif average >= 60:
        grade = 'B'
    elif average >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade


marks = [55, 64, 75, 80, 65]
average = average_mark(marks)
grade = com_grade(average)
print(f"Your average is {average}")
print(f"Your grade is {grade}")
