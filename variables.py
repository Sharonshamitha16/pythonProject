print("Enter the following details to now whether u have leave")
name = input("Enter your name: ")
days_of_leave = int(input("Enter the no. of leaves: "))
year =int(input("enter the year: "))
print("-"*50)
print("Dear", name+"," , "\nYou have", str(100-days_of_leave)+" days of leave Balance for this" + "\nYear" ,'('+str(year)+')' + ".")
print("-"*50)