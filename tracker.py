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
