number = int(input("Enter a 4 digit number: "))

fourth_num = number % 10
third_num = (number % 100) // 10
second_num = (number % 1000) // 100
first_num = number // 1000


print(fourth_num , third_num, second_num, first_num)
