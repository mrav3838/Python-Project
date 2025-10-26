import math_operator
try : 
    a = int(input("Enter first number: "))

    b = int(input("Enter second number: "))


except ValueError as e:
    print("Enter a valid value of a and b")

print("Menu:")
print("1. Addition(+)")
print("2. Subtraction(-)")
print("3. Multiplication(*)")
print("4. Division(/)")
print("5. Floor Division(//)(discard the decimal part from the result)")
print("6. Modulus(%)(shows only the remainder)")
print("7. Power(**)(powers the value with a^^b)")
print("8. Average")
print("9. Square")
print("10. Absolute value(makes all the values positive)")
print("11. Rounded value(rounded to nearest integer)")
print("12. Maximum value(compares two values and shows the maximum)")
print("13. Minimum value(compares two values and shows the minimum)")
print("Enter the index value from the above menu for the operation")
print("14. To exit the operation")


o =input("Enter operation: ")
match o:
    case "1":
        math_operator.add(a, b)
    case "2":
        math_operator.subtract(a, b)
    case "3":
        math_operator.multiply(a, b)
    case "4":
        math_operator.divide(a,b)        
    case "5":
        math_operator.floor_divide(a, b)
    case "6":
        math_operator.modulus(a, b)
    case "7":
        math_operator.power(a, b)
    case "8":
        math_operator.average(a, b)
    case "9":
        math_operator.square(a, b)
    case "10":
        math_operator.absolute(a, b)
    case "11":
        math_operator.rounded_num(a, b)
    case "12":
        math_operator.maximum(a, b)
    case "13":
        math_operator.minimum(a, b)
    case "14":
        print("Exiting the operation...")
        exit()
    case _:
        print("Invalid Choice from menu")