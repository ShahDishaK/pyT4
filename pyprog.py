import numpy as np
a1=np.array([0,1,2,3])
a2=np.array([[0,1,2,3],[4,5,6,7]])
# output
# 0:0
# 1:1
#2:2
#3:3
#0:4
#1:5
# 2:6
# 3:7
# for i,j in zip(np.nditer(a2),np.nditer(a1)):
#     print(i,":",j)
for i,j in np.nditer([a1,a2]):
    print(i,":",j)    

a3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
sum=0
mul=1
for i in np.nditer(a3):
    sum+=i
    mul*=i
print(sum)
print(mul)

np.add(a3,2)

a3=np.array([[0, 1, 2 ,3], [4 ,5, 6, 7 ],[8, 9, 10 ,11] ,[12,13, 14, 15]])
# for item,index in np.ndenumerate(a3):
#     if index%2==0:
print(a3[1::2,1::2])
        
    

a4=np.arange(12).reshape(3,4)

print(a4)

a4[:,[0,1]]=a4[:,[1,0]]
print(a4)

a=np.array([[20,20,20],[30,30,30],[40,40,40]])
b=np.array([20,30,40])
result=a//b[:,None]
print(result)

# There is an array of scores of 5 Batsmen in 4 T20 Matches. Which is given below.
# Scores= [[31, 12, 19, 53],
#                [67, 48, 95, 83],
#                [59, 67, 13, 59],
#                [62, 29, 99, 88],
#                [87, 91, 69, 76]]
# 9	Hard					
# 1
# 1. Find the maximum score in T_20-3 and print it (use only the numpy module)
# 2. Find the minimum score of YUVRAJ and print it (use only the numpy module)
# 3. Add an extra column with the sum of all 4 T20 Matches’ scores of each batsman in the array created and print it. (use only the numpy module)   
Scores= np.array([[31, 12, 19, 53],
            [67, 48, 95, 83],
              [59, 67, 13, 59],
              [62, 29, 99, 88],
              [87, 91, 69, 76]])
max203=np.max(Scores[None,-2])
print(max203)
minUv=np.min(Scores[2,None])
print(minUv)
# add extra column