# Self-study Capabilities Test

> Do a self-study of the topics below, we will have a hands on activity later without references.

1. Loops
    - for
    - while
    - loop controls
        - else
        - continue
        - break

2. Iterators
    - range
    - zip
    - enumerate
    - count
    - sort

3. Comprehensions

4. Functions
    - yield
    - closures
    - global
    - lambda (Arrow Function)

## Additional

1. Py Collections

# Activity (11/26/26)

# Activity 1: Grade Book Analyzer

*Topic:* Python loops (for, zip(), enumerate(), continue, break, for...else, nested loops, loops inside functions)
*Level:* Beginner to intermediate
*Suggested time:* 60 to 90 minutes
*Work mode:* Individual or pairs

---

## Learning Objectives

By the end of this activity, students will be able to:

1. Use nested loops to process a list of lists.
2. Iterate over several lists at once with zip().
3. Number results with enumerate() and a custom start.
4. Control loop flow with continue and break.
5. Use for...else to detect when a loop finished without a break.
6. Organize loop logic into functions that take parameters and return values.

---

## Scenario

You are a teaching assistant for a programming class. The instructor gives you three parallel lists containing each student's name, quiz scores, and exam score. Write a program that computes final grades, ranks the students, and identifies who needs help.

### Starter Data

names = ["Ana", "Ben", "Cara", "Dan", "Ella"]

quiz_scores = [
    [85, 90, 78],
    [60, 55, 70],
    [92, 88, 95],
    [45, 50, 40],
    [75, 80, 70],
]

exam_scores = [88, 58, 94, 50, 72]

QUIZ_WEIGHT = 0.40
EXAM_WEIGHT = 0.60
PASSING_GRADE = 60

Each position matches across the lists. names[0], quiz_scores[0], and exam_scores[0] all belong to Ana.

---

## Tasks

### Task 1: Quiz Average (nested loop)

Write compute_quiz_average(scores), which takes one student's list of quiz scores and returns the average.

- Use a loop to add up the scores. **Do not use sum().**
- Return 0 if the list is empty.

### Task 2: Final Grades (zip)

Write compute_final_grades(names, quizzes, exams), which returns a list of (name, final_grade) tuples.

- Use *one* for loop with zip() over all three lists.
- Call compute_quiz_average() for each student.
- Final grade = quiz_average * QUIZ_WEIGHT + exam * EXAM_WEIGHT, rounded to 2 decimals.

### Task 3: Ranking (enumerate)

Write print_rankings(results).

- Sort the results from highest to lowest grade (hint: sorted() with key= and reverse=True).
- Use enumerate() with start=1 to print each rank.

### Task 4: At-Risk List (continue)

Write find_at_risk(results, passing), which returns a list of names of students whose grade is below passing.

- Use continue to skip students who passed.
- Do *not* use an if block wrapping the append. The point is to practice continue.

### Task 5: Class Status Check (for...else and break)

Write check_class_status(results, passing).

- Loop through the results. If a failing student is found, print their name and break.
- Use the loop's else clause to print "All students passed!" when no one failed.
- *Do not use a flag variable* such as found = False.

### Task 6: Main Report

Write main() that calls all the functions and prints a formatted report. Run it only under if __name__ == "__main__":.

---

## Starter Code

def compute_quiz_average(scores):
    # TODO
    pass


def compute_final_grades(names, quizzes, exams):
    # TODO
    pass


def print_rankings(results):
    # TODO
    pass


def find_at_risk(results, passing):
    # TODO
    pass


def check_class_status(results, passing):
    # TODO
    pass


def main():
    # TODO
    pass


if __name__ == "__main__":
    main()

---

## Expected Output

Your output should match these values. The formatting may differ slightly.

=== FINAL GRADES ===
Ana: 86.53
Ben: 59.47
Cara: 93.07
Dan: 48.0
Ella: 73.2

=== RANKINGS ===
1. Cara - 93.07
2. Ana - 86.53
3. Ella - 73.2
4. Ben - 59.47
5. Dan - 48.0

=== AT-RISK STUDENTS ===
Ben, Dan

=== CLASS STATUS ===
First failing student found: Ben
---

## Rules and Constraints

- No sum(), max(), or min() for the main logic.
- Every function must use return where specified, not print inside calculations.
- Use meaningful variable names and add a short comment above each function.
- Don't hard-code the number of students. The program must work for any list length.

---

## Hints

- zip(a, b, c) gives you one item from each list per iteration: for name, quizzes, exam in zip(...).
- sorted(results, key=lambda r: r[1], reverse=True) sorts tuples by the second element.
- In a for...else, the else runs only if the loop was *not* ended by break.
- If the else seems confusing, read it as "no break happened."

---

## Grading Rubric (100 points)

| Criteria | Points |
|---|---|
| *Task 1:* Correct average using a loop, handles empty list | 10 |
| *Task 2:* Correct use of zip() with three lists, correct weighted formula | 20 |
| *Task 3:* Correct sorting and enumerate(start=1) | 15 |
| *Task 4:* Correct use of continue, correct list returned | 15 |
| *Task 5:* Correct for...else with break, no flag variable, tested with the all-pass case | 20 |
| *Task 6:* Clean main(), formatted output, __main__ guard | 10 |
| *Code quality:* naming, comments, no hard-coded lengths | 10 |
| *Total* | *100* |