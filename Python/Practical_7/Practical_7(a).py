print("\n\nTo read and write from a file \n")
source = open("src.txt","r")
des = open("des.txt","w")
while True:
    new_line = source.readline()
    if new_line == "":
        break
    des.write(new_line)
print("Copying is done\n")
source.close()
des.close()