from random import randint

#Implemented a partition function which returns m1 and m2 indexes. 
#The region from left to m-1: less than pivot, m1 to m2: equal to pivot, m2+1 to right: greater than pivot

def partition3(array, left, right):

    #Initialize variables
    pivot=array[left]
    m1=left
    m2=right
    i=left

    #Run the loop till all elements are compared by comparing against m2
    while i<=m2:

        #Adjust to left to m1-1 region
        if array[i]<pivot:
            array[i],array[m1]=array[m1],array[i]
            i=i+1
            m1=m1+1

        #Adjust the m2+1 to right region    
        elif array[i]>pivot:
            array[i],array[m2]=array[m2],array[i]
            m2=m2-1

        #Adjust the m1 to m2 region    
        else:
            i=i+1

    return m1,m2

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
