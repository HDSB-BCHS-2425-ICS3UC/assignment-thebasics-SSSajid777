# this is an integer as output has no decimals
integer_result=10
print("Integer Example:",integer_result)
#this is a float as it has decimal number
float_result=10.4
print("Float Example:",float_result)
#this is boolean, a true or false statement
logged_in=True 
print("Boolean Example:",logged_in)
#this is char, a single character
charA=('a')
print("Char Example:",charA)
#this is string, a combination of characters
str=("Hello World")
print ("String Example:",str)

#this is input
print ("Please enter your name")
name=input()

#this is multiplication
product=2*3
print ("the product is",product)


#this is division 
quotient=4/2
print ("the quotient is",quotient)

#this is addtion 
sum=2+5
print ("the sum is",sum)

#this is subtraction
difference=10-2
print ("the difference is",difference)

#this is modulus, this shows the remainder when you divide
remainder=(23%4)
print ("the remainder is",remainder)

#this is to the power of. ** is used for exponents
exponent=(2**3)
print ("the exponent is",exponent)


import math
#this is square root, you have to import math to use it)
root=(math.sqrt(9))
print("the root is",root)

#this is discriminant from the quadratic formula

#input from user
a=float(input("Type the value of a, then press Enter "))
b=float(input("Type the value of b, then press Enter "))
c=float(input("Type the value of c, then press Enter "))

#Formula of discriminant
delta = b**2 - 4*a*c
print("The discriminant is",delta)

#3D Volume

#Cube

cube_side=float(input("Enter A(lenght of edge), then press Enter "))
cube_volume= cube_side**3
print("The volume of cube is",cube_volume)

#Sphere

sphere_radius= float(input("Enter r(radius), then press Enter "))
sphere_volume= (4/3) * (math.pi) * (sphere_radius**3)
print("The volume of a sphere is",sphere_volume)


#Cone


cone_radius= float(input("Enter r(radius), then press Enter"))
cone_height= float(input ("Enter h(height), then press Enter"))
cone_volume= (1/3) * (math.pi) * (cone_radius*2) * (cone_height)
print("The volume of a cone is", cone_volume)


#Cylinder 

cylinder_radius= float(input("Enter r(radius), then press Enter"))
cylinder_height= float(input ("Enter h(height), then press Enter"))
cylinder_volume= (math.pi) * (cylinder_radius**2) * (cylinder_height)
print("The volume of a cylinder is", cylinder_volume)