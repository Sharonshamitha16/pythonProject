str="34,5,21,87,9"
str2 =''
num_list=[]
num= True
for i in str:
    if num:
        str2 =''
        num=False
    if i==',':
        num_list.append(int(str2))
        num= True
        continue
    str2 +=i
print(num_list)