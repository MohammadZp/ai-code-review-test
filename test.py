def calculate_area(radius):
    # This function calculates the area of a circle
    pi = 3.14159  # Approximation of pi
    area = pi * radius ** 2
    return area

def calculate_perimeter(radius):
    # This function calculates the perimeter (circumference) of a circle
    pi = 3.14159  # Approximation of pi
    perimeter = 2 * pi * radius
    return perimeter

def main():
    radius = 5
    area = calculate_area(radius)
    perimeter = calculate_perimeter(radius)
    
    print(f"The area of the circle with radius {radius} is: {area}")
    print(f"The perimeter of the circle with radius {radius} is: {perimeter}")

if __name__ == "__main__":
    main()
