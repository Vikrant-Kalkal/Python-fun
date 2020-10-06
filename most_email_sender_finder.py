#Write a program to read through the file and tell who sent the most number of emails
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emails=dict()
frequent_email=None
frequency_email=None
for line in handle:
    linesplit=line.split()
    if "From" in linesplit:
        pos=0
        pos=line.find("From")
        emails[linesplit[pos+1]]=emails.get(linesplit[pos+1],0)+1
#the following code runs properly and is used coz but we can also use the "max" function directly 
for key,val in emails.items():
    if frequent_email is None or val>frequency_email:
        frequent_email= key
        frequency_email=val
print(frequent_email,frequency_email)