
# A program to get age of user as input and then check if he/she can enter. He/She can enter only if the age is either 20 or more than that

print("Enter your age in numbers")
age = int(input())
if age >= 20:
    age = True
elif age < 20:
    age = False
else:
    print("Please Enter your age in numbers")

#age = True
activated = True

if age and activated:
    print("Hey! Welcome to the app")
elif age == False and activated == False:
    print("Create your account")
elif age == True and activated == False:
    print("Please activate your account")
elif age == False and activated == True:
    print("You can't use this app")
else:
    print("Thanks for using our app")