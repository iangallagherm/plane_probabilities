import random
import math

def main():
    a = -1 
    b = 1 
    num_points = 1000000

    split_count = 0
    complex_count = 0

    points = random_sphere_points(num_points)

    for point in points:
        if char_poly_disc(point, a, b) < 0:
            complex_count += 1
        else:
            split_count += 1

    print(complex_count/num_points)
    print(split_count/num_points)
    

def random_sphere_points(num_points):
    points = []
    for i in range(num_points):
        u = random.random()
        v = random.random()

        theta = 2 * math.pi * u
        phi = math.acos(2 * v - 1)

        x = math.cos(theta) * math.sin(phi)
        y = math.sin(theta) * math.sin(phi)
        z = math.cos(phi)

        points.append([x,y,z])
    return points

def euclidean_norm(point):
    return sum([coord ** 2 for coord in point])

def char_poly_disc(point, a, b):
    x = point[0]
    y = point[1]
    z = point[2] 

    return 4 * (a*x*x + b*y*y - a*b*z*z)

if __name__ == "__main__":
    main()
