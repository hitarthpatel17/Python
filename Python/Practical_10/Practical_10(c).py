import matplotlib.pyplot as plt
labels = ['pyhon','java','c++','Ruby']
sizes = [245, 215, 210, 150]
colors = ['gold','yellowgreen','lightcoral','lightskyblue']
explode = [0.1,0,0,0]
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', 
shadow='True',startangle=140)
plt.axis('equal')
plt.show()