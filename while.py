

##qn1
# while True:
#     user=input('enter your age:')
#     if user=='stop':
#         print('stop')
#         break
#     age=int(user)
#     if age<18:
#         print('you are a minor')
#     elif 18<=age<60:
#         print('you are adult')
#     else:
#         print('you are senior citizen')


    
# qn2
# while (user_input:=input('enter your input:')!='bus'):
#     print('waiting')
# else:
#     print('wait is over')

#qn5

# ratings=['4+','5+','4+','9+','3+']
# content_rating={}
# i=0
# while i < len(ratings):
#     if ratings[i] in content_rating:
#         content_rating[ratings[i]]=content_rating.get(ratings[i],0)+1
#     else:
#         content_rating[ratings[i]]=1
#     i=i+1
# print(content_rating)

#qn3
# while(user:=input('enter your fruit:')!='apple'):
#     print('try again')
# else:
#     print('you got it')
#qn6
# import random
# rn=random.randint(1,100)
# while True:
#     user=int(input('enter a number:'))
#     if rn==user:
#         print('congrulation')
#         break
#     elif user>rn:
#         print('too high')
#     else:
#         print('too low')

#qn7

# username = 'admin'
# password = '1234'
# count = 3
# while True:
#     user_input = input('enter your user name : ')
#     password_input = input('enter your password : ')

#     if count == 0:
#         print('your attempt is over ')
#         break
#     else:
#         if username == user_input and password == password_input:
#             print('login sucessful')
#             break
#         else:
#             count -=1
#             print(f'your password or user name is worng, attemped left {count}')

##qn8
                

# import random

# print("Multiplication Quiz (type 'exit' to stop)")

# while True:
#     num1 = random.randint(1, 30)
#     num2 = random.randint(1, 30)

#     user_input = input(f"What is {num1} × {num2}? ")

#     if user_input == "exit":
#         print("Quiz ended. Goodbye!")
#         break


#     if not user_input.isdigit():
#         print("Please enter a valid number or 'exit'.")
#         continue

#     answer = int(user_input)

#     if answer == num1 * num2:
#         print("Correct!\n")
#     else:
#         print("Incorrect, try again.\n")

##qn9
# while True:
#     user_input = input("Enter a number (or type 'exit' to stop): ")

#     if user_input == "exit":
#         print("Program ended.")
#         break

#     if not user_input.isdigit():
#         print("Please enter a valid positive number.")
#         continue

#     num = int(user_input)

#     if num < 2:
#         print("The number is not prime.")
#         continue

#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print("The number is prime.")
#     else:
#         print("The number is not prime.")

##qn10
# secret_word = "python"

# while True:
#     guess = input("Guess the secret word (or type 'quit' to exit): ")

#     if guess == "quit":
#         print("You exited the game.")
#         break

#     if guess == secret_word:
#         print("Congratulations, you guessed the word!")
#         break
#     else:
#         print("Incorrect, try again.")

##qn11
# count = 0

# while True:
#     name = input("Enter a name: ")

#     if name == "good luck":
#         count += 1

#         if count == 3:
#             print("You typed good luck three times.")
#             break
#         else:
#             print(f"You typed the same word {count} times.")

##qn12
# current_floor = 1
# print("Elevator is starting on floor 1.")

# while True:
#     user_input = input("Enter destination floor (0 to exit): ")


#     if user_input == "0":
#         print("Goodbye! Elevator shutting down.")
#         break


#     if not user_input.lstrip("-").isdigit():
#         print("Invalid input. Please enter a valid floor number.")
#         continue

#     target_floor = int(user_input)

#     if target_floor > current_floor:
#         print("Going up")
#     elif target_floor < current_floor:
#         print("Going down")
#     else:
#         print("You are already on this floor.")


#     current_floor = target_floor
#     print(f"Elevator is now on floor {current_floor}.\n")
