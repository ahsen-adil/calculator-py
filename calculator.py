num1 = int(input("please enter your first number"))
num2 = int(input("please enter your second number"))
opr = input("please write any one operator : (+ - * /)")

if opr == "+":
  print(num1+num2)
elif opr == "-":
  print(num1-num2)
elif opr == "*":
  print(num1*num2)
elif opr == "/":
  print(num1/num2)
else:
  print('please chose the operator from given choies to complete this action')
