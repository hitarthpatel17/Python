str1 = input("Enter A String : ") 
if len(str1) >= 3:
    if str1.endswith('ing'):
        str1 += 'ly' 
    else:
        str1 += 'ing'
    print(f"String Updated Is {str1}")
else:
    print("There is no change in string ")
    print(f"The String Is {str1}")