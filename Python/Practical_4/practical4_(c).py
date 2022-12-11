dict1 = {'red':'123','green':'675','black':'324','white':'897'}
print(dict1)
print("sort by key:")

sortkey={key:value for key, value in sorted(dict1.items(),key= lambda item:item[0])}
print(sortkey)

print("sort by value:")
sortvalue={key: value for key, value in sorted(dict1.items(),key=lambda item:item[1])}
print(sortvalue)