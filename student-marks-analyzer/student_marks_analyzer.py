name = input('Enter your name: ')

mathematics = float(input('Enter your Mathematics marks: '))
science = float(input('Enter your Science marks: '))
social = float(input('Enter your Social Science marks: '))
english = float(input('Enter your English marks: '))

marks = [mathematics, science, social, english]
total = int(input('Enter the maximum possible marks: '))
subjects = ["Mathematics", "Science", "Social Science", "English"]

def calculate_average(marks): # Calculates average marks
    total_marks = 0

    for mark in marks:
        total_marks += mark    
    average = total_marks / len(marks)
    
    return average


def calculate_percentage(marks, total): # Calculates percentage
    total_marks = 0

    for mark in marks:
        total_marks += mark

    percentage = (total_marks/(total*len(marks)))*100
    return percentage

def find_highest(marks, subjects): # Calculates highest marks with subject
    highest = marks[0]
    highest_index = 0

    for i in range(len(marks)):
        if marks[i] > highest:
            highest = marks[i]
            highest_index = i

    return subjects[highest_index], highest

def find_lowest(marks, subjects): # Calculates lowest marks with subject
    lowest = marks[0]
    lowest_index = 0

    for i in range(len(marks)):
        if marks[i] < lowest:
            lowest = marks[i]
            lowest_index = i

    return subjects[lowest_index], lowest

def display_report(name, marks, subjects, total): # Displays Report Card
    highest_subject, highest_marks = find_highest(marks, subjects)
    lowest_subject, lowest_marks = find_lowest(marks, subjects)
    print('*'*20)
    print(f'''
\n-----REPORT CARD-----\n

Congratulations, {name}!\n
You have received an average of {calculate_average(marks):.2f}
You have secured {calculate_percentage(marks, total):.2f}%\n
You have scored highest in {highest_subject} with {highest_marks} marks
You have scored lowest in {lowest_subject} with {lowest_marks} marks\n
''')
    print('-'*20)

def main():
    display_report(name, marks, subjects, total)

if __name__ == "__main__":
    main()
