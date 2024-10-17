def get_grade(score1, score2, score3):
    scores = [score1, score2, score3]
    avg = sum(scores) / len(scores)

    # In Python, you have the ability to use multiple comparison operators
    # in the same expression 
    match avg: 
        case avg if 90 <= avg <=  100:
            return 'A'
        case avg if 80 <= avg < 90:
            return 'B'
        case avg if 70 <= avg < 80:
            return 'C'
        case avg if 60 <= avg < 70:
            return 'D'
        case _:
            return 'F'

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True