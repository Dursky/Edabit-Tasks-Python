import math

def square_areas_difference(radius):
    if(radius > 0):
        circle = math.pi * radius **2
        small_square = radius * radius
        big_square = (radius * 2) * (radius * 2) 
        return (small_square + big_square) - circle

print(square_areas_difference(5))