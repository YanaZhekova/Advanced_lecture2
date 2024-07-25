n = int(input())
students_grades = dict()

for _ in range(n):
    name, grade = input().split()

    if name not in students_grades:
        students_grades[name] = list()
        students_grades[name].append(grade)
    else:
        students_grades[name].append(grade)

for student, grade in students_grades.items():
    average = sum(float(x) for x in grade)
    grades = " ".join(grade)
    print(f"{student} -> {grades} (avg: {(average / len(grade)):.2f})")
