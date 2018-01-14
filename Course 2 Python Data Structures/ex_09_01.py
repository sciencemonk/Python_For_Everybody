#9.4 Write a program to read through the mbox-short.txt and figure out who has
#the sent the greatest number of mail messages. The program looks for 'From '
#lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to
#a count of the number of times they appear in the file. After the dictionary is
#produced, the program reads through the dictionary using a maximum loop to find
#the most prolific committer.

file_name = input('Enter file name:')
file_handler = open(file_name,'r')

email_list = []
email_dict = {}
for line in file_handler:
    current_line = line.split()
    if 'From' in current_line:
        email_list.append(current_line[1])


for name in email_list:
    email_dict[name] = email_dict.get(name, 0) + 1

#print(email_dict)

sender_max = None
sender_num = None

for key,value in email_dict.items():
    if sender_num is None or sender_num < value:
        sender_max = key
        sender_num = value

print(sender_max, sender_num)
