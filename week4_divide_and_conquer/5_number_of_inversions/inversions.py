from itertools import combinations


def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions

#We use a merge sort algorithm to sort the input array and during the merging process, count inversions
def MergeSort(A):
    "Takes the unsorted array A and returns its sorted version in ascending order"
    
    #By using global keyword we tell Python to treat total_inversions as the global variable and not local function variable
    global total_inversions

    #Return simply input array and a junk value(777) if input array size is 1 
    if len(A)==1:
        #A junk value of 777 is retuned for single array size. This value of 777 is not used anywhere 
        return A,777
    
    #deciding approx half point of unsorted array
    m = int(len(A)/2)

    #Recursively break the original array in half and keep breaking till array size becomes 1. Then start merging it.
    B,_=MergeSort(A[0:m])
    C,_=MergeSort(A[m:])

    #Merge the sub arrays in ascending order and count inversions
    A_sorted,inversions=Merge(B,C)
    
    #We maintain a global variable named total_inversions and add the new inversions found during merge process to this global variable.
    total_inversions = total_inversions+inversions
    #print("total inversions are",total_inversions)

    return A_sorted,total_inversions

def Merge(B,C):
    "Takes the pre-sorted B and C which are portion of original array A and merges then such that all elements are in ascending order"
     
    #array to store sorted values 
    D=[]
    inversions=0

    #do merging till both arrays are non-empty
    while len(B)!=0 and len(C)!=0:
        #pick the first element of each array
        b=B[0]
        c=C[0]
        
        #if left element is less than or equal to right side element then merge that element to result array and cut the first element from left array
        if b<=c:
            B=B[1:]
            D.append(b)
        else:
            #IMPORTANT: If this "else" block is executed, then it means that current left side element(b) is higher than current right side element(c). Also,
            #all remaining elements of left side will be higher than current right side element(c) as B and C are pre-sorted. So we can count the number of inversions
            # by counting how many elements are in left side array(B).
            inversions = inversions+len(B)

            #Append the right side element to result array and cut from right array
            C=C[1:]
            D.append(c)

    #Either B or C is empty so no point of comparing. Just add them to result array
    D=D+B+C
    
    #return the resulting sorted array along with number of inversions encountered in merging process
    return D,inversions     





if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    #create a global variable to maintain the count of inversions
    total_inversions=0
    #Just print second return value which corrosponds to number of inversions
    print(MergeSort(elements)[1])


 
