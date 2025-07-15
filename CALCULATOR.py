while True:
  print("Select operation:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. exit") 

  choice = input("Enter choice (1/2/3/4/5): ")
  if choice == '5':
     print("appo sheri bye")
     break

  num1 = float(input("Bro please enter first number: "))
  num2 = float(input("also the second number: "))

  if choice == '1':
    print("Result:", num1 + num2)
  elif choice == '2':
    print("Result:", num1 - num2)
  elif choice == '3':
    print("Result:", num1 * num2)
  elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Sorry bro,Cannot divide by zero!")  
  else:
    print("Invalid input")