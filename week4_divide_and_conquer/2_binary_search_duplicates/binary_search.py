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


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    high_idx=num_keys-1
    low_idx=0

    for q in input_queries:
        print(binary_search_duplicates(input_keys, q,low_idx,high_idx), end=' ')
