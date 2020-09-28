'''Create 2 variables and store 2 numbers the user wants to add together '''

num1 = input("Enter your first number:")
num2 = input("Enter your second number:")
result = int(num1)+int(num2)
'''you have to put int before num1/num2 otherwise instead of 2+3=5, itll do 2+3=23'''
print(result)

'''To be able to add decimal numbers, you use the float function instead of int '''