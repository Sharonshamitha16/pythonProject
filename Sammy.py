'''def isEmpty(stk):
    if stk ==[]:
        return True
    else:
        return False
def Push(stk,item):
    stk.append(item)
    top=len(stk)-1
def Pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        item=stk.pop()
def Peek(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        if stk==[]:
            top=None
        else:
            top=len(stk)-1
            print(stk[top], "<- top")
def Display(stk):
    if isEmpty(stk):
        return "Empty"
    else:
        top=len(stk)-1
        print(stk[top] , "<- top")
        for i in range(top-1,-1,-1):
            print(stk[i])

print("=" * 60)
print("Stack Operations")
print("="*60)
Stack=[]
while True:
    ch=int(input("Enter your choice:"))
    if ch not in [1,2,3,4,5]:
        print("Wrong Choice! Aborting")
    elif ch==1:
        Item=input("Enter the Item:")
        Push(Stack,Item)
    elif ch==2:
        if isEmpty(Stack):
            print("Underflow")
        else:
            Pop(Stack)
    elif ch==3:
        if isEmpty(Stack):
            print("Empty")
        else:
            Peek(Stack)
    elif ch==4:
        if isEmpty(Stack):
            print("EMPTY")
        else:
            Display(Stack)
    elif ch==5:
        print("Exiting!!!")
        break'''

import pickle
def writing():
    f=open("idk.dat","ab+")
    r=pickle.dump("Sam is here",f)
    f.close()
def reading():
    try:
        f = open("idk.dat", "ab+")
        re=pickle.load(f)
        p=f.tell()
        f.seek(0,0)
        print(p)
        print(re)
    except EOFError:
        f.close()
reading()