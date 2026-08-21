age=int(input("Enter your age: "))

if(age>18):
    print("you are eligible for voting")  #this spacing is called INDENTATION


elif(age<0):
    print("It's age is invalid")

elif(age==0):
    print("Entering 0 which is not valid age")

    
else:
    print("You are not eligible for voting")


print("End of the voting program")