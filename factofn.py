num= int(input("Enter a number to get their factors:"))
for i in range(1,num+1):
    if(num%i ==0):
        print(i)