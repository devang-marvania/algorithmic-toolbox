from sys import stdin
from random import randint




def points_cover_optimized(starts,ends,points):

    point_list=[]

    #Create a common list of all numbers: start points, end points and points. Attach the label "s" or "e" or "p" to denote whether point is start, end or point.
    #These labels will be used later to run a counter. For the point, save point_idx as well to appropriately maintain score
    point_list =[(start_point,"s") for start_point in starts]+[(end_point,"e") for end_point in ends]+[(point,"p",point_idx) for point_idx,point in enumerate(points)]

    #Sort the combined point list in ascending order. If two points are same then put the start first, then point and then end point.
    point_list_sorted=sorted(point_list,key=lambda x:(x[0],-ord(x[1])))

    #A running score variable
    segment_score=0

    #Zero array to keep score of each point
    counter_array=[0]*len(points)

    for i,tup in enumerate(point_list_sorted):
        if tup[1]=="s":
            #Increase score when segment starts
            segment_score=segment_score+1
        if tup[1]=="e":
            #Decrease score when segment ends
            segment_score=segment_score-1
        if tup[1]=="p":
            #When point is encountered, save the score in counter array
            counter_array[tup[2]]=segment_score

    return counter_array                












if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover_optimized(input_starts, input_ends, input_points)
    

    print(*output_count)
