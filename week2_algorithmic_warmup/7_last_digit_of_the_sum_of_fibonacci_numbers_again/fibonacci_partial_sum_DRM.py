# Uses python3
#import sys

def fibonacci_partial_sum_naive(m,n):
    

    previous = 0
    current  = 1

    #Research about Pisano period

    period = [0,1]

    #append values to period defined above and detect when the last 2 values match first 2 values. When it does, then period can be obtained by removing last 2 values
    for _ in range(n - 1):
        previous, current = (current % 10), (previous  + current) % 10
        period.append(current)

        if period[-2:]==period[:2]:
            period=period[:-2]
            break


    #find the reduced index in period for first number
    reduced_index_m=m%len(period)

    #find the reduced index in period for second number
    reduced_index_n=n%len(period)

    if reduced_index_n>=reduced_index_m:
        partial_sum = sum(period[reduced_index_m:reduced_index_n+1])%10
    else:
        partial_sum = (sum(period[reduced_index_m:])+sum(period[:reduced_index_n+1]))%10


    #print("period is ",len(period))
    #print("sum of period is", sum(period))

    #Important: For module 10, period is 60 and sum of all elements in a period is 280. 
    #Hence, we do not need to sum elements in complete period but only those which are not in period and then do module 10.

    return partial_sum


if __name__ == '__main__':
    #input = sys.stdin.read();
    m, n = map(int, input().split())
    print(fibonacci_partial_sum_naive(m, n))
