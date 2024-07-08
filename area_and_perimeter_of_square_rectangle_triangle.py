# Area of rectangle,square and triangle
# Perimeter of square and triangle

l = int(input('Enter the length of the rectangle: '))
b = int(input('Enter the breadth of the rectangle: '))
side = int(input('Enter the side number of the square: '))
base = int(input('Enter the base of the triangle: '))
height = int(input('Enter the height of the triangle: '))
a = int(input('Enter the side of the square: '))
length = int(input('Enter the length of the rectangle: '))
breadth = int(input('Enter the breadth of the rectangle: '))
length1 = int(input('Enter the first side of the triangle'))
length2 = int(input('Enter the second side of the triangle'))
length3 = int(input('Enter the third side of the triangle'))


area_of_rectangle = l * b
print('Area of Rectangle is: ',area_of_rectangle)

area_of_square = (side * side)
print('Area of square is: ',area_of_square)

area_of_triagnle = (base * height) / 2
print('Area of triangle is: ',area_of_triagnle)

perimeter_of_square = 4 * a
print('Perimeter of square is: ',perimeter_of_square)

perimeter_of_rectangle = 2 * (length * breadth)
print('Perimeter of rectangle is: ',perimeter_of_rectangle)

perimeter_of_triangle = length1 + length2 + length3
print('Perimeter of the triangle is: ',perimeter_of_triangle)

