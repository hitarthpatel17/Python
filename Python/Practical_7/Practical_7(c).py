print("To write a python program to count a number of words in a file")
src = open("src.txt","r")
d = dict()
count = 0
for line in src:
    line = line.strip()
    words = line.split(" ")
    count += len(words) 
print(f"The number of words in file is : {count}")