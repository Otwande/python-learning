
def grade(score):
 if score >=70 and score <=100:
    print("your score is", score, "and your grade is A")
 elif score>=60 and score<70:
    print("your scores is", score, "and your grade is B")
 elif score>=50 and score <60:
    print("your score is", score, "your grade is C")
 elif score>=40 and score<50:
    print("your score is", score, "and your grade is D")
 else:
    print("your score is", score, "and you have failed")
grade(76)
grade(56)
grade(32)
grade(66)

