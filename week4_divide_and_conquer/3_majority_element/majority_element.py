
#Similar to naive algorithm but we use more efficient data structures like dictionary
def majority_element(elements):

    #create dictionary named counts, using the elements. Dictionary data structure will ensure that if an element is repeated, key is not repeated
    counts=dict.fromkeys(elements,0)

    #create a variable for half number of elements which will be compared against
    half_num = len(elements)/2

    #increment the count as number appears in array
    for e in elements:
        counts[e] += 1

        #Break the loop and return 1 as soon as count of a number goes higher than half number
        if counts[e] > half_num:
            return 1
            break

    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))


#Naive algorithm supplied with the code
def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0