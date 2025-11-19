import math

def calculate_b(a,c):
    return math.sqrt(c*c-a*a)

def calculate_area(a,b):
    return a*b/2

def main():
    print("Triangle calculator")
    a = float(input("Enter the length of one leg (side): \n"))
    c = float(input("Enter the length of the hypotenuse: \n"))
    while a <= 0 or c <= a:
        a = float(input("Enter the length of one leg (side): \n"))
        c = float(input("Enter the length of the hypotenuse: \n"))
    b = calculate_b(a,c)
    area = calculate_area(a,b)
    print(f"The length of b is {b:.2f} and the area of the triangle is {area:.2f}.")

main()