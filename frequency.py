list=[1,2,2,3,3,1,1]
dict={}
for num in list:
    if num in dict:
        dict[num]+=1
    else:
        dict[num]=1

for key,value in dict.items():
    print(key,"---->",value)
