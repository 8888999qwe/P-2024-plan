def mysort(list1,len1):
    temp = []
    i = 0
    a = 0
    j = 0
    max = 0
    while i<=(len1-1):
        for x in list1:
            if x>max:
                max=x
                a=j
            j+=1
        temp.append(max)
        list[a]=0
        max=0
        j=0
        i+=1
    return temp
list =[1,4,10,8,2,3,6]
len2 = 0
len2 =len(list)
list=mysort(list,len2)
for x in list:
    print(x)