from sys import stdin
from collections import namedtuple



def optimal_points(segments):
    points = []
  

    #sort the segments in increasing order of start points. If there is tie with start point then sort in increasing order of end points
    sorted_segments=sorted(segments,key=lambda x:(x.start,x.end))
   
    #list of zeros. As a point crosses the segment we will set the corrosponding index value to 1. Index order to be matched with order of sorted_segments
    touched_segments=[0]*len(sorted_segments)

   #This algotithm essentially takes the left most segment and finds out which segments are affected if a projection is made top to bottom. Whichever, segments are
   #covered,we set their corrosponding index value to 1 in projected_segments list. Now, we find the "point" : First create a list of endpoints consisting of endpoint 
   #of leftmost segment and the segments covered by its projection. Then find the min from this list that is "point". Next append this "point" to points list. Next 
   #is to find out after passing the vertical line through "point", which segments are touched. In next search, reduce the search space by only searing in untouched
   #segments.

    for i in range(len(sorted_segments)):
         if touched_segments[i]==0:
              projected_segments=[0]*len(sorted_segments)
              for j in range(i,len(sorted_segments)):
                   if point_within_segment(sorted_segments[i],sorted_segments[j].start):
                        projected_segments[j]=1
              ends=end_list(projected_segments,sorted_segments)
              point=min(ends)
              points.append(point)
              for j in range(i,len(sorted_segments)):
                   if point_within_segment(sorted_segments[j],point):
                       touched_segments[j]=1                    
    
    
    return points

def end_list(projected_segments,sorted_segments):
    "returns the end points of segment in sorted_segments if their corrosponding index in projected_segments is 1"

    end_list=[]
    for i in range(len(projected_segments)):
        if projected_segments[i]==1:
            end_list.append(sorted_segments[i].end)        

    return end_list    

def point_within_segment(segment,point):
    "Takes the segment and point as input and returns True if point is within segment, otherwise False"

    if segment.start<=point<=segment.end:
        return True
    else: 
        return False    


Segment = namedtuple('Segment', 'start end')


#Use below code to comply with grader and enter segment info

if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)



 # Use this code to interactively enter the segment info

"""
n = int(input("Enter the number of line segments: "))

segments = []
for i in range(n):
    start, end = map(int, input(f"Enter the start and end point of segment {i+1}: ").split())
    segments.append(Segment(start, end))    
points = optimal_points(segments)
print(len(points))
print(*points)
"""





