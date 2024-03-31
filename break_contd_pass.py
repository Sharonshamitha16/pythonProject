list=[]
while True:
    num=input("enter the number of elements and z to exit ")

    if int(num)%20==0 or num =='z':
        list.append(int(num))
        break

print (list)