#Exercise 1: Write a program which repeatedly reads numbers until the user
# enters "done". Once "done" is entered, print out the total, count,
#and average of the numbers. If the user enters anything other than a
#number, detect their mistake using try and except and print an error message
#and skip to the next number.

count = 0
total = 0.0
while True :
    user_input = input('Enter a number: ')
    if user_input.lower() == 'done':
        break
    try:
        user_number = float(user_input)
    except:
        print('Error, please enter a number or done')
        continue
    count += 1
    total += user_number
print('All Done')
print(total, count, total/count)
