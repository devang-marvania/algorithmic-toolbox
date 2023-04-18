from sys import stdin
from random import randint


#Implemented a partition function which returns m1 and m2 indexes. 
#The region from left to m-1: less than pivot, m1 to m2: equal to pivot, m2+1 to right: greater than pivot

'''
def partition3(array, left, right,segment_dict,sort_by_end):

    #Initialize variables
    pivot=segment_dict[array[left]][sort_by_end]
    m1=left
    m2=right
    i=left
    

    #Run the loop till all elements are compared by comparing against m2
    while i<=m2:

        #Adjust to left to m1-1 region
        if segment_dict[array[i]][sort_by_end]<pivot:
            array[i],array[m1]=array[m1],array[i]
            i=i+1
            m1=m1+1

        #Adjust the m2+1 to right region    
        elif segment_dict[array[i]][sort_by_end]>pivot:
            array[i],array[m2]=array[m2],array[i]
            m2=m2-1

        #Adjust the m1 to m2 region    
        else:
            i=i+1

    return m1,m2,array

def randomized_quick_sort(array, left, right,segment_dict,sort_by_end):
    if left >= right:
        return array
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2,array = partition3(array, left, right,segment_dict,sort_by_end)
    randomized_quick_sort(array, left, m1 - 1,segment_dict,sort_by_end)
    randomized_quick_sort(array, m2 + 1, right,segment_dict,sort_by_end)

    return array


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count

'''
def binary_search_duplicates(keys, query,low,high):
    
    #Find out at what index the query lies in sorted input array 
    match=binary_search(keys, query,low,high)

    #if the query exists within input array(meaning index is not -1) then see till 
    # how long you can decrement the index and still get it matched with the query
  #  if match != -1 and match!=0:
  #      while keys[match-1]==query:
  #          match=match-1
  #          if match==0:
  #              break

    #If the query exists within array and not at lowest index(meaning index is not -1 or 0) then create a temporary variable "reduced_match"
    #and see how far this index can be reduced. If at reduced index becomes -1, then use the previous value. To do this, whenever reduced_index is not 0 or 
    #-1, updated match. If at some point, reduced index becomes 0, then update match right away to save value.
    
    if match != -1 and match !=0:
        reduced_match=match
        while(reduced_match != -1 and reduced_match != 0):
            match=reduced_match
            reduced_match=binary_search(keys, query,low,reduced_match-1)
            if reduced_match==0:
                match=reduced_match
                    
        
            

    return match


def binary_search(keys, query,low,high):
    # Binary search function takes sorted array of numbers as input(keys), along with a search item(query) and lower and higher index of keys within which search 
    #needs to be made. If query matches with any items in keys, then return corrosponding index, otherwise -1

    #Check if query is within the input array by checking at bounds
    if query<keys[low] or query>keys[high]:
        return -1
    
    #Recursive Binary search implementation starts below

    #In case lower index gets bigger than higher index(could happen by doing changing lower bound to mid+1)
    if high<low:
        return low-1
    
    #Look at middle of array and depending on query and keys[mid] relation, change the upper and lower bounds
    mid=int(low+(high-low)/2)

    
    if query == keys[mid]:
        return mid
    
    elif query<keys[mid]:
        return binary_search(keys,query,low,mid-1)
    
    elif query>keys[mid]:
        return binary_search(keys,query,mid+1,high)

    else:
        return -1

def segments_limit(sorted_segment_dict,point):
    "gives the segment index of lower and upper segment within which point lie"

    high_idx=len(sorted_segment_dict)-1
    low_idx=0

    if point<sorted_segment_dict[low_idx] or point>sorted_segment_dict[high_idx]:
        return -1
    
    if high_idx<low_idx:
        return 
    
    

    mid_idx=int(low_idx+high_idx)/2

    #point position relative to mid index. Positive value indicates - point is towrard left of mid_idx and upper idx needs to changed in next search, negative value
    #indicates - point is towards right of mid_idx and lower idx needs to be changed in next search, 0 indicates that point is start point of mid idx segment 
    #are same - we want to keep shifting left by one segment at a time to cover any segments with same start point
    
    pos_rel_mid_idx=sorted_segment_dict[mid_idx][0]-point









def points_cover(starts,ends,points):
    assert len(starts)==len(ends)

    #segment_id=[i for i in range(len(starts))]
    segment_dict={i:[starts[i],ends[i]] for i in range(len(starts))}
    sorted_by_start_list=sorted(segment_dict.items(),key=lambda x:x[1][0])
    sorted_by_start_dict={k:v for k,v in sorted_by_start_list}

    sorted_by_end_list=sorted(segment_dict.items(),key=lambda x:x[1][1])
    sorted_by_end_dict={k:v for k,v in sorted_by_end_list}
    

    sorted_starts=[v[0] for k,v in sorted_by]
    sorted_ends=[]

    for i in range(len(sorted_segment_dict)):
        sorted_starts

    print("sorted segment dict:",sorted_segment_dict)


starts=[4,3]
ends=[5,10]
points=[1,2]

points_cover(starts,ends,points)






'''
if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    #output_count = points_cover_naive(input_starts, input_ends, input_points)
    #print(*output_count)

    points_cover_naive(input_starts, input_ends, input_points)

    #print()
'''

