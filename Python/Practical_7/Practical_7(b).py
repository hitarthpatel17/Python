print("To write a python program to find the most frequent words from a file")
source = open("src.txt","r")
d = dict()
maximum = 0
max_key = []
for line in source:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
for key in list(d.keys()):
    print(f"{key} : {d[key]}")
    if d[key] >= maximum:
        maximum = d[key]
        max_key.append(key)
print("The maximum occured words : ")
for key in max_key:
 print(f"{key} : {d[key]}")
