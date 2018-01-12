# largest number in a list

def largest(list):
    largest = 0
    for i in list:
        if i > largest:
            largest = i
    return largest

list = [3,41,2,9,74,15]

print(largest(list))
