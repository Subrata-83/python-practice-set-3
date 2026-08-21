age=int(input("Enter your age: "))

if(age%2==0):
    print("age is even")

if(age>=18):
    print("You ar eligible for voting")


elif(age==0):
    print("age 0 is invalid integer")

elif(age<0):
    print("Negative invalid integer")


else:
    print("You are not eligible for voting")

print("end of the voting")
