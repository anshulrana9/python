
total_points = 0
print("Please Enter your name to start")
name = input()

if name:
    total_points=100
else:
    name = input()

list_of_num=[1,2,3,4,5,6,7,8,9,10]
random_num = 5

for each_num in list_of_num:
    print("Your total points are", total_points)
    print("Now, Guess a number between 1 to 10")
    guessed_num = int(input())

    if guessed_num == random_num:
        total_points= total_points + 100
        print("Congrats", name , "You guessed it right")
        print("Your Total Points are" ,total_points)
        break

    elif guessed_num != random_num:
        print("Wrong Number! 10 points deducted. Try Again")
        total_points -= 10
        print(total_points)