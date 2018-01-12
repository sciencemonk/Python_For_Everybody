#5.2 Write a program that repeatedly prompts a user for integer numbers
#until the user enters 'done'. Once 'done' is entered, print out the largest
#and smallest of the numbers. If the user enters anything other than a valid
#number catch it with a try/except and put out an appropriate message and
#ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None

while True:
    user_input = input('Enter an integer: ')

    if user_input.lower() == 'done':
        break
    try:
        user_number = int(user_input)
    except:
        print('Invalid input')
        continue
    if largest == None:
        largest = user_number
    elif user_number > largest:
        largest = user_number
    if smallest == None:
        smallest = user_number
    elif user_number < smallest:
        smallest = user_number
print("Maximum is",largest)
print("Minimum is",smallest)
