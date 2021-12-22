from add,sub,mul,div import*
print("Welcome to calculator")
print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exit")
while True:
  choice = input("Enter choice(1-5) : ")
  if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))

  if choice == '1':
    print("Added value = ", add(num1, num2))

  elif choice == '2':
    print("Subtracted value = ",  subtract(num1, num2))

  elif choice == '3':
    print("Multiplied value = ", multiply(num1, num2))

  elif choice == '4':
    print("Divided value = ", divide(num1, num2))
        
  elif choice == '5':
    break
  else:
    print("Invalid Input")