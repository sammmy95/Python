def calculate_total(m1, m2, m3):
    return m1 + m2 + m3


def calculate_percentage(total):
    return total / 3


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"