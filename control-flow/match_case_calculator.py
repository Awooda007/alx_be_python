num1 = input("Enter the first number:")
num2 = input("Enter the second number:")
operation = input("Choose the operation (+, -, *, /):")

match operation:
	case "+":
		print(f"The result is {num1+num2}")
	case "-":
		print(f"The result is {num1-num2}")	
	case "*":
		print(f"The result is {num1*num2}")
	case "/":
		if num2 == 0:
			print("cannot divide by zero")
		else:
			print(f"The result is {num1/num2}")
	case _:
		print("invalid operation")