# largest number in a list

def largest(list):
    largest = 0
    for i in list:
        if i > largest:
            largest = i
    return largest

list = [1,21,12,1334,1,9,44,99,10020,211]

print(largest(list))
