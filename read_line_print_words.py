# Program to read a txt file line by line and
# print the list of words that are in the file and 
# also print the owrd count

fname = input("Enter file name: ")
fh = open(fname,'r')
lst = list() #defining a variable of "list" type 
#nested for loops to read each line and then each word in that line
for line in fh:
    for i in range(len(line.split())):
        if (line.split()[i]) not in lst: 
            lst.append(line.split()[i])
lst.sort()
print(lst)
