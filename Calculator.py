def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x , y):
    if y==0:
        return " error, cant divide by 0! "
    return x / y

print("      SIMPLE CALCULATOR        ")
print("Which Operation Do U Want To Do?")
print("1. Proceed With Addition")
print("2. Proceed With Substraction")
print("3. Proceed With Multiplication")
print("4. Proceed With Division")

while True:
    choice = input(" Enter Choice (1 or 2 or 3 or 4): ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number"))
        except ValueError : 
            print("Invalid Input")
            continue
        
        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {substract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            
        if input("Another Calculation? (yes/no): ").lower() != 'yes': break