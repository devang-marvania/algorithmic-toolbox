def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    #Research about Pisano period

    period = [0,1]

    #append values to period defined above and detect when the last 2 values match first 2 values. When it does, then period can be obtained by removing last 2 values
    for _ in range(n - 1):
        previous, current = (current % m), (previous  + current) % m
        period.append(current)

        if period[-2:]==period[:2]:
            period=period[:-2]
            break


    #find the reduced index in period
    reduced_index=n%len(period)
    #print("period is ",len(period))

    return period[reduced_index] 


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
