from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    max_product = 0
     
    #sort both sequences in descending order 
    first_sequence.sort(reverse=True)
    second_sequence.sort(reverse=True)

    #multiply elements from both list pairwise and add to max_product
    for i in range(len(second_sequence)):
        max_product = max_product + first_sequence[i]*second_sequence[i]

    return max_product


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
