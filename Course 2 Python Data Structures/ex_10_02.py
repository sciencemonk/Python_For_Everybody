#10.2 Write a program to read through the mbox-short.txt and figure out the
#distribution by hour of the day for each of the messages. You can pull the
#hour out from the 'From ' line by finding the time and then splitting the
#string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour as shown below.

file_name = input('Enter file name:')
file_handler = open(file_name, 'r')

hour_list = []
for line in file_handler:
    current_line = line.split()
    if 'From' in current_line:
        hour = current_line[5]
        hour_list.append(hour[0:2])

hour_dict = {}
for hour in hour_list:
    hour_dict[hour] = hour_dict.get(hour, 0) + 1

temp_list = []

for key,value in hour_dict.items():
    new_tuple = (key,value)
    temp_list.append(new_tuple)

temp_list = sorted(temp_list)

for key,value in temp_list:
    print(key,value)
