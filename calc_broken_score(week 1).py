def main():
    final_score = get_score(score)
    print(final_score)

score = float(input("Enter score: "))
def get_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score > 90:
            return "Excellent"
        elif score > 50:
            return "Passable"
        else:
            return "Bad"


main()