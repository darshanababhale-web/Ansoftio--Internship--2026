# Function to calculate area
def rectangle_area(length, breadth):
    area = length * breadth
    return area

# User input
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

# Function call
result = rectangle_area(length, breadth)

# Output
print("Area of Rectangle is:", result)
