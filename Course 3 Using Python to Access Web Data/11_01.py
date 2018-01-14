# Read file, extract all numbers and compute sum
import re

file_name = input('Enter file name:')
file_handler = open(file_name, 'r')

int_list = []

# Find all integers and append to int_list
for line in file_handler:
    current_line = line.rstrip()
    if len(re.findall('[0-9]+',current_line)) != 0:
        for i in re.findall('[0-9]+',current_line):
            int_list.append(i)

# Convert list of strings into int
int_list = [int(i) for i in int_list]

print('Sum:',sum(int_list),'Number of integers',len(int_list))
