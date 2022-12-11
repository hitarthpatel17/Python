my_dict = {1:1,2:4,3:9,4:16,5:20}
print("New dictionary is created in the name:my_dict",my_dict)
my_dict[5]= 25
print("change an element in dictionary:",my_dict)
my_dict[6]= 36
print("Add an element in dictionary:",my_dict)
print("Remove the arbitory element from the dictionary:",my_dict.pop(5))
print("Remove the using.pop(5) element from the dictionary:",my_dict)
del my_dict[6]
print("Delete the element from the dictionary:",my_dict)