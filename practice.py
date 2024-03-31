# INPUT FROM USER AND FORMATTING
import l

print('_' * 100)
height = float(input("Enter your height: "))
height_inches = "{:.2f}".format(
    height / 2.54)  # string.format i.e {}is used for string and : for placeholder and.2f is refering the pts
print("your height is:", str(height))
print("you are", height_inches, "inches tall")

print('_' * 100)
# math
import math

a = 3
b = 4.6
print(math.ceil(a))
print(math.floor(b))
print(math.factorial(a))
print('_' * 100)
print(not (a == b))
print(not a == b)
print(a == (not b))

print('_' * 100)
# CONVERT TO DEC TO BIN AND COUNT
n = 50


def solution(n):
    a = bin(n)
    b = len(a) - 2
    print(a)
    print(b)


solution(n)
print('_' * 100)
# ELIMINATE NON ZERO ELEMENTS

l = [2, 3, 4, 5, 6, 7, 8, 9, 0, 1]

a = []
for i in range(0, len(l)):
    if l[i] != 0:
        a.append(l[i])
print(a)
print('_' * 100)

# IF ELSE CONDITION PRINTING 3 DIGIT NUMBER OR NOT

num = int(input("enter a number:"))
if num>=100 and num<=999:
    print("It is and 3 digit number")
    if num % 2 == 0:
        print(str(num) + " It  is an even 3 digit number also")
else:
    print("It is not a 3 digit number ")

print('_' * 100)

# LISIS

list=["chennai", "madurai", "kanyakumari", "salem", "trichy","pondicherry", "coimbatore"]
print(list)
print("inserted",list.insert(1,"thanjavur"))
print(list)
list[5]="cuddalore"
print( "modified",list)
print(list.append("trivandrum"))
print(list)
print(list.insert(2,"thanjavur"))
print(list)
print(list.insert(3,"thanjavur"))
print(list)


del  list[2]
print(list)

deleted =list.pop()
print(deleted)
print(list)
print(list.remove("kanyakumari"))
print(list)
print(sorted(list))
print(list)
print(list.sort())
print(list)
print(list.reverse())
print(list)
print("-"*100)
#
# # while loop ALPHABET OR  NOT
letter =''
while not letter.isalpha():
    letter=input("enter a alphbet: ")

print(letter," is the alphabet have entered  ")
print("-"*100)

num=1
while num<=100:
    print(num)
    num+=1
print("printed till 100 from while loop")
print("-"*100)

#using for loop
for i in range (1,100+1):
     print(i)
print("printed till 100 from for loop")
print("-"*100)

for i in range (100,0,-2):
    print(i)
print("-"*100)

list =[2,3,4,5,6,7,8,9]
for i in list :
    print(i*2)
print("-"*100)

# while loop guess the game
import random
num = random.randint(1,20)
attemps=0
while attemps < 4:
    guess = int(input(" u have only " +str(4-attemps)+ " attempts..  guess the numer btw 1 to 20 : "))
    attemps += 1

    if num==guess:
        print("congrats u won...You have completed in " + str(attemps) + "  attempt(s)")
        break
    elif guess>num:
            print(" ur guess is higher")
            print("Guess again. You are in no." + str(attemps) + " attempt(s)")
    elif guess <num:
            print("ur guess is lower")
            print("Guess again. You are in   " + str(attemps) + " attempt(s) ")

if attemps==4 and num!=guess:
    print("you lost  all the attempts , the corect number is ", num)

#break_contd_pass
list=[]
while True:
    num = input("enter values to add and z to get exit:")
    if num=='z':
        break

    list.append(int(num))
print(list)


string="A,B,V,H,U,J,I,,K,O"
string2= ''
for i in string:
    if i==',':
        continue
    string2 =string2+i
print(string2)

num="23,45,67,89,21,43,65"
splitted =num.split(',')
print(splitted)
joined='-'.join(splitted)
print(joined)

#tuples
tup=(2,3,46,7,4,324,6,2,2,8)
print(tup.count(2))
print(tup)
for i in tup:
    print(i)
print('*'*45)
print(tup[3])