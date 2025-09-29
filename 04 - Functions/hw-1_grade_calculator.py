# Grade Calculator Exercise
"""
## Problem
You're building a grade calculator for a teacher who needs to calculate final grades for students. The teacher needs to:

1. Calculate the average of multiple test scores
2. Apply a curve (add points to boost grades)
3. Convert numerical grades to letter grades
4. Format the output nicely

## Requirements
Without using functions, you would need to repeat the same calculations for each student. Your task is to:

1. Create functions that eliminate code repetition
2. Make the main program easy to read and understand
3. Handle the grade calculations for multiple students

## Expected Behavior
The program should ask for student names and their test scores, then display:
- Student name
- Original average
- Curved average
- Letter grade

## Sample Run
```
Enter student name (or 'done' to finish): Alice
Enter test scores separated by spaces: 85 92 78 88
Student: Alice
Original Average: 85.8
Curved Average: 90.8 (+5 curve)
Letter Grade: A-

Enter student name (or 'done' to finish): Bob  
Enter test scores separated by spaces: 72 68 75 70
Student: Bob
Original Average: 71.2
Curved Average: 76.2 (+5 curve)
Letter Grade: B-

Enter student name (or 'done' to finish): done
```

## Hints
Think about what code you would repeat for each student and turn those into functions:
- Calculating averages
- Applying curves
- Converting to letter grades
- Formatting output
"""
def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def cal_average(numbers):
    average = sum(numbers)/len(numbers)
    return average

def cal_curved_score(score, curve):
    return score  + curve

def cal_grade(score):
    float(score)
    grade = ""
    if score > 90:
        grade  = "A"
    elif score > 80:
        grade  = "B"
    elif score > 70:
        grade  = "C"
    elif score > 60:
        grade  = "D"
    else:
        grade = "F"
    return grade

def format(name, average, curved_average, curve, grade):
    print(f"Student: {name}")
    print(f"Original Average: {average}")
    print(f"Curved Average: {curved_average} (+{curve} curve)")
    print(f"Letter Grade: {grade}")
    print()
    

name = input("Enter student name (or 'done' to finish): ")

while name.lower() != "done":
    input_scores = input("Enter test scores separated by spaces: ")
    list_scores = list(input_scores.split()) #make a list of scores using split to separate by space
    scores = []
    for score in list_scores: #put float score in scores
        scores.append(float(score))
    average  = cal_average(scores)
    curve = 5
    curved_score  =  cal_curved_score(average, curve)
    grade = cal_grade(curved_score)
    format(name, average, curved_score,curve, grade) 
    name = input("Enter student name (or 'done' to finish): ")

print()
print("---Program ended---")
