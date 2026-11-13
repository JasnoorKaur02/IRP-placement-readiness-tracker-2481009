"""Record practice scores and summarize placement readiness."""

# Fictional practice records. Roll numbers are strings to keep leading zeroes.
STUDENTS = [
    {"name": "Aarav Mehta", "roll_no": "001", "aptitude": 84, "verbal": 80, "coding": 91},
    {"name": "Diya Shah", "roll_no": "002", "aptitude": 58, "verbal": 67, "coding": 55},
    {"name": "Kabir Rao", "roll_no": "003", "aptitude": 41, "verbal": 37, "coding": 42},
    {"name": "Meera Sethi", "roll_no": "004", "aptitude": 33, "verbal": 35, "coding": 37},
    {"name": "Rehan Ali", "roll_no": "005", "aptitude": 74, "verbal": 88, "coding": 78},
]


def average(student):
    """Return the unrounded mean of the three practice scores."""
    return (student["aptitude"] + student["verbal"] + student["coding"]) / 3


def grade(avg):
    """Apply grade thresholds from highest to lowest."""
    if avg >= 80:
        return "A"
    if avg >= 60:
        return "B"
    if avg >= 40:
        return "C"
    return "Needs practice"


def top_scorer(students):
    """Return the highest-scoring record; ties keep the first record."""
    return max(students, key=average)


def needs_practice(students, limit=40):
    """Return the records with averages strictly below the limit."""
    return [student for student in students if average(student) < limit]


def print_results(students):
    """Print an aligned row for each student and summarize the group."""
    roll_width = max(4, max(len(s["roll_no"]) for s in students))
    name_width = max(15, max(len(s["name"]) for s in students))
    header = (
        f"{'Roll':<{roll_width}}  {'Name':<{name_width}}  "
        f"{'Apt':>3} {'Verb':>4} {'Code':>4} {'Avg':>6}  Grade"
    )
    print("\nResults")
    print(header)
    print("-" * (len(header) + 9))
    for student in students:
        avg = average(student)
        print(
            f"{student['roll_no']:<{roll_width}}  {student['name']:<{name_width}}  "
            f"{student['aptitude']:>3} {student['verbal']:>4} {student['coding']:>4} "
            f"{avg:>6.2f}  {grade(avg)}"
        )

    leader = top_scorer(students)
    practice = needs_practice(students)
    print(f"\nTop scorer: {leader['name']} ({average(leader):.2f})")
    names = ", ".join(student["name"] for student in practice)
    print(f"Extra practice (average below 40): {names or 'None'}")
    print(f"Students needing practice: {len(practice)}")
