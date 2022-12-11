import matplotlib.pyplot as plt 
x = [ 
1,3,5,2,6,4,5,8,1,3,2,4,4,6,5,11,12,11,13,44,55,10,12,13,34,78,99,9,87,65,43,22,33,45.45,44,44,44,46,47,48,49 
]
plt.style.use('ggplot')
plt.hist(x,bins=10)
plt.show()