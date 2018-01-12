#Exercise 1: Write a program which repeatedly reads numbers until the user
# enters "done". Once "done" is entered, print out the total, count,
#and average of the numbers. If the user enters anything other than a
#number, detect their mistake using try and except and print an error message
#and skip to the next number.

def reader():
    status = True
    total = 0
    while status:
        user_input = input('Enter a number:')
        if user_input.lower() == 'done':
            return total
            status = False
        try:
            user_number = float(user_input)
        except:
            print('Error, please enter a number or done')
            continue

        total += user_number
    return(total)

print("Total:",reader())
