student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# ๐จ Don't change the code above ๐

# Scores 91 - 100: Grade = "Outstanding"
#
# Scores 81 - 90: Grade = "Exceeds Expectations"
#
# Scores 71 - 80: Grade = "Acceptable"
#
# Scores 70 or lower: Grade = "Fail"

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.๐
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif 80 < score < 90:
        student_grades[student] = "Exceeds Expectations"
    elif 70 < score < 80:
        student_grades[student] = "รcceptable"
    elif score > 70:
        student_grades[student] = "Fail"

# ๐จ Don't change the code below ๐
print(student_grades)
