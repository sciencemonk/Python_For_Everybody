# Excercise 3.1

try:
    hours = float(input("Enter hours:"))
    rate = float(input("Enter rate/hour:"))
except:
    print("Error, please enter numberic input")
    quit()

print(hours, rate)
if hours > 40:
    regular_pay = rate * 40
    overtime = (hours - 40) * (rate * 1.5)
    pay = regular_pay + overtime
else:
    pay = rate * hours
print(pay)
