"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
def calculator():

     while True:
        user_input = input("enter your equation > ")

        tokens_from_user_input = user_input.split(' ') 

        if tokens_from_user_input[0] == "q":
            return False 

        if tokens_from_user_input[0] == "+":

            num1 = int(tokens_from_user_input[1])
            num2 = int(tokens_from_user_input[2])

            print(add(num1, num2))

        if tokens_from_user_input[0] == "-":

            num1 = int(tokens_from_user_input[1])
            num2 = int(tokens_from_user_input[2])

            print(subtract(num1, num2))
        
        if tokens_from_user_input[0] == "*":

            num1 = int(tokens_from_user_input[1])
            num2 = int(tokens_from_user_input[2])

            print(multiply(num1, num2))

        if tokens_from_user_input[0] == "/":

            num1 = int(tokens_from_user_input[1])
            num2 = int(tokens_from_user_input[2])

            print(divide(num1, num2))   

        if tokens_from_user_input[0] == "square":

            num1 = int(tokens_from_user_input[1])
           
            print(square(num1)) 

        if tokens_from_user_input[0] == "cube":

            num1 = int(tokens_from_user_input[1])
            
            print(cube(num1))

        if tokens_from_user_input[0] == "pow":

            num1 = int(tokens_from_user_input[1])
            num2 = int(tokens_from_user_input[2])

            print(power(num1, num2))

        if tokens_from_user_input[0] == "mod":

            num1 = int(tokens_from_user_input[1])
            num2 = int(tokens_from_user_input[2])

            print(mod(num1, num2))

           

calculator()
       # if tokens_from_user_input[0] == "-":




# Replace this with your code
