import math
j=print
def welcome_message():
    j("="*30)
    j("welcome to the grade calculator")
    j("="*30)

def get_test_scores():
    score_1=float(input("enter your first grade here:"))
    score_2=float(input("enter your second grade here:"))
    score_3=float(input("enter your third grade here:"))
    return score_1,score_2,score_3

def calculate_average(score_1,score_2,score_3):
    average=(score_1+score_2+score_3)/3
    j(f"your average is {average:.2f}")
    return average





def get_letter_grade(average):
    if average>= 90:
        return"A"
    elif average >= 80:
        return"B"
    elif average>= 70:
        return"C"
    elif average >=60:
        return"D"
    else:
        return"F"
    j(f"your average is {get_letter_grade:.2f}")
def display_result(score_1, score_2, score_3, average, get_letter_grade):
    end=j(f"your 3 scores are {score_1:.2f}, {score_2:.2f},{score_3:.2f}. with an average of {average:.2f} and a grade {get_letter_grade(average)}")


def main(welcome_message,calculate_average,get_test_scores, get_letter_grade):
    welcome_message()
    score_1,score_2,score_3 = get_test_scores()
    average = calculate_average(score_1, score_2,score_3)
    display_result(score_1, score_2, score_3, average, get_letter_grade)