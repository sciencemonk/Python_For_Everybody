import time
num = int(input('Enter a number'))

while num >= 0:
    if num >= 1:
        print(num)
        time.sleep(1)
    else:
        print('Lift off!')
    num -= 1
