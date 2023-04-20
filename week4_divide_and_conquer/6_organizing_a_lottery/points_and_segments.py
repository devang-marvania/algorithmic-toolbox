from sys import stdin
from random import randint
import bisect











def points_cover(starts,ends,points):
    #assert len(starts)==len(ends)

    #segment_id=[i for i in range(len(starts))]
    segment_list=[(starts[i],ends[i]) for i in range(len(starts))]
    segment_list_sorted=sorted(segment_list,key=lambda x:x[0])

    result=[]

    for point in points:
        score=search_sorted_segment_list(segment_list_sorted,point)
        result.append(score)

     

    return result

def search_sorted_segment_list(segment_list_sorted,point):

    segment_start_sorted=[segment[0] for segment in segment_list_sorted]
    right_segment_idx=bisect.bisect(segment_start_sorted,point)

  

    segment_shortlist_by_start=segment_list_sorted[:right_segment_idx]
    segment_shortlist_by_end=[segment for segment in segment_shortlist_by_start if point<=segment[1]]

    return len(segment_shortlist_by_end)


#input_starts=[0,-3,7]
#input_ends=[5,2,10]
#input_points=[1,6]

#print(points_cover(starts,ends,points))





'''
if __name__ == '__main__':
    #data = list(map(int, stdin.read().split()))
    #n, m = data[0], data[1]
    #input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    #input_points = data[2 * n + 2:]

    #output_count = points_cover_naive(input_starts, input_ends, input_points)
    #print(*output_count)

    #points_cover_naive(input_starts, input_ends, input_points)
    output_count=points_cover(input_starts, input_ends, input_points)
    print(*output_count)

    #print()
'''


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    

    points_cover(*output_count)




