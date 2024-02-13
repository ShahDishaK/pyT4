import matplotlib.pyplot as plt
x=[1,2,3]
y=[2,4,1]
plt.plot(x,y)
plt.xlabel('x-axis')
plt.xlabel('x-axis')
plt.title("my first graph")
plt.show()

import matplotlib.pyplot as plt
x1=[1,2,3]
y1=[2,4,1]
plt.plot(x1,y1,label="line1")
y2=[4,1,3]
x2=[1,2,4]
plt.plot(x2,y2,label="line2")
plt.xlabel('x-axis')
plt.xlabel('x-axis')
plt.title("2 lines on same graph")
plt.show()

values=[2,5,4,7,3]
names=["A","B","C","D","E"]
plt.bar(names,values,color="green")
plt.show()

https://adornmentevents.com/

import matplotlib.pyplot as plt
x=[1,2,3]
y=[2,4,1]
plt.plot(x,y,color="green",linestyle="dashed",linewidth=3,marker="o",markerfacecolor="blue",markersize=12)
plt.ylim(1,8)
plt.xlim(1,8)
plt.xlabel('x-axis')
plt.xlabel('x-axis')
plt.title("customization")
plt.show()

import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]
y=[2,4,5,6,7,8,9,11,12,12]
plt.scatter(x,y,color="green",label="stars",marker="*",s=3)
plt.xlabel('x-axis')
plt.xlabel('x-axis')
plt.title("my scatter plot")
plt.show()

import matplotlib.pyplot as plt
import numpy as np
plt.subplot(2,1,1)
x1 = [10, 20, 30]
y1 = [20, 40, 10]
plt.plot(x1,y1,label="line1-width-3",linewidth=3,color="blue")
x2 = [10, 20, 30]
y2 = [40, 10, 30]
plt.plot(x2,y2,label="line2-width-5",color="red",linewidth=5)
plt.legend()
plt.show()
# scatter
plt.subplot(2,3,4)
weight1 = [67, 57.2, 59.6, 59.64, 55.8, 61.2, 60.45, 61, 56.23, 56]
height1 = [101.7, 197.6, 98.3, 125.1, 113.7, 157.7, 136, 148.9, 125.3, 114.9]
weight2 = [61.9, 64, 62.1, 64.2, 62.3, 65.4, 62.4, 61.4, 62.5, 63.6]
height2 = [152.8, 155.3, 135.1, 125.2, 151.3, 135, 182.2, 195.9, 165.1, 125.1]
weight3 = [68.2, 67.2, 68.4, 68.7, 71, 71.3, 70.8, 70, 71.1, 71.7]
height3 = [165.8, 170.9, 192.8, 135.4, 161.4, 136.1, 167.1, 235.1, 181.1, 177.3]
# plt.scatter(weight1,height1,color="green",label="stars",marker="*",s=3)
# plt.scatter(weight2,height2,color="green",label="stars",marker="*",s=3)
# plt.scatter(weight3,height3,color="green",label="stars",marker="*",s=3)
weight=np.concatenate((weight1,weight2,weight3))
height=np.concatenate((height1,height2,height3))
plt.scatter(weight,height,color="green",label="stars",marker="*",s=3)

plt.xlabel('weight')
plt.ylabel('height')
# bar
plt.subplot(2,3,5)
x = ['A', 'B', 'C', 'D', 'E', 'F']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.bar(x,popularity,color=["r","black","green","blue",'yellow',"cyan"])
# pie
plt.subplot(2,3,6)
languages = 'L', 'M', 'N', 'O', 'P', 'Q'
popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors=["red","yellow","green","blue","pink","cyan"]
plt.pie(popuratity,labels=languages,colors=colors,shadow=True,startangle=90,explode=(0.1,0,0,0,0,0),radius=1.2,autopct='%1.1ff%%')
plt.show()

