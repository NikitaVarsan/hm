first_num = int(input("Please enter first number:"))
second_num = int(input("Please enter second number:"))
action = input("Please enter action:")

if action == '+':
    print("Your result is:", first_num + second_num)
elif action == "-":
    print("Your result is:", first_num - second_num)
elif action == "*":
    print("Your result is:", first_num * second_num)
elif action == "/":
    if first_num == 0:
        print("You can't divide by 0")
    elif second_num == 0:
        print("You can't divide by 0")
    else:
        print("Your result is:", first_num / second_num)















