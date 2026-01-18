a=float(input("Enter the side:"))
b=float(input("Enter the second side:"))
c=float(input("Enter the third side:"))

s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5

print("The area of the triangle is",round(area,3))


