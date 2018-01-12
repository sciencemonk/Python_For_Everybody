# Scorer

try:
    score = float(input("Enter score between 0.0 and 1.0: "))
except:
    print("Error, please enter numberic input")
    quit()

if score > 1 or score < 0:
    print('Error, score outside range')
    quit()
elif score >= .9:
    grade = 'A'
elif score >= .8:
    grade = 'B'
elif score >= .7:
    grade = 'C'
elif score >= .6:
    grade = 'D'
else:
    grade = 'F'
print(grade)
