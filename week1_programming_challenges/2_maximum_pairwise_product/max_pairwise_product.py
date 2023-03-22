def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    highest = numbers[0]
    highest_idx=0
    #second_highest = numbers[0]
    #second_highest_idx=0
    for i in range(n):
        if numbers[i]>highest:
            highest=numbers[i]
            highest_idx=i
    
    for j in range(n):        
        if numbers[j]<=highest and j != highest_idx:
            second_highest = numbers[j]
            second_highest_idx = j
                
    
    #print("highest number is",highest)
    #print("highest number index is",highest_idx)
    #print("second highest number is",second_highest)
    #print("second highest number index is",second_highest_idx)
    max_product=highest*second_highest
    
    return max_product


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))