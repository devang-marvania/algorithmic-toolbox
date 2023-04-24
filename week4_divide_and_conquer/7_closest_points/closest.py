from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared

def minimum_distance_optimized(points,points_length):
    '''
    Takes in sorted by X array of points and points array size as input. The output is min distance between 2 points from given array. Utliizes binary 
    search along with a custom function named "seach_in_strip" to ensure that solution compares all points needed. Reference: https://www.geeksforgeeks.org/closest-pair-of-points-using-divide-and-conquer-algorithm/#

    '''

    #No point of doing binary search if need to search within only 3 points
    if points_length<=3:
        min_distance_squared=minimum_distance_squared_naive(points)
        return sqrt(min_distance_squared)

    #Find the mid Point's index and actual midpoint
    midPointIdx=int(points_length/2)
    midPoint=points[midPointIdx]

    #Recursively divide array in 2 parts and find out min distance from each part
    min_distance_squared_left=minimum_distance_optimized(points[0:midPointIdx],midPointIdx)
    min_distance_squared_right=minimum_distance_optimized(points[midPointIdx:],points_length-midPointIdx)

    #Find the min of min_distance from left and right sections
    min_distance=min(min_distance_squared_left,min_distance_squared_right)
    

    strip=[]
    
    #shortlist all points which are "min_distance" away in positive and negative x direction from midPoint and save them in a strip variable
    for point in points:
        if abs(point.x-midPoint.x)<min_distance:
            strip.append(point)

    #find out if there is an edge case where a point from left section and a point from right section are even closer than min_distance calculated above
    min_distance_from_strip=search_in_strip(strip,len(strip),min_distance)   

    #return the min_distance from left/right sections and strip
    return min(min_distance,min_distance_from_strip)     

def search_in_strip(strip,strip_size,min_distance):
    '''
    A custom function to see if there is an edge case where a point from left section and a point from right section are even closer than min_distance calculated from
    individual left and right sections
    '''
    #Sort the strip in ascending order of y co-ordinates
    strip=sorted(strip,key=lambda point:[point.y])

    #Figure out min_distance by comparing 2 points 
    for i in range(strip_size):
        for j in range(i+1,strip_size):
            #If y distance is more than min_distance than actual distance will be for sure more than current and next points, so break the array
            if abs(strip[j].y-strip[i].y)>min_distance:
                break
            #save new value of min_distance if its less than previously recorded min_distance value
            if sqrt(distance_squared(strip[i],strip[j]))<min_distance:
                min_distance=sqrt(distance_squared(strip[i],strip[j]))

    
    return min_distance            
    


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    input_points=sorted(input_points, key=lambda input_point:[input_point.x,input_point.y])
    #print("input points are",input_points)    

    #print("Using optimized algorithm:{0:.9f}".format(minimum_distance_optimized(input_points,len(input_points))))
    #print("Using naive algorithm:{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))

    print("{0:.9f}".format(minimum_distance_optimized(input_points,len(input_points))))
