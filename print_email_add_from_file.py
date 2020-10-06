#program to read a file which contain email addresses and extract the email adresses from it

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
lst=list()
for line in fh:
    pos=0
    if "From" in line.split():
        pos=line.find("From")
        lst.append(line.split()[pos+1])
        count=count+1
for i in range(len(lst)):
    print(lst[i])
print("There were", count, "lines in the file with From as the first word")
