import os

def gradingStudents(grades):

    for i in range(len(grades)):
        if grades[i] >= 38:
            next_multiple = (grades[i]//5+1)*5
            if next_multiple - grades[i] < 3:
                grades[i] = next_multiple

    return grades

if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(grades)