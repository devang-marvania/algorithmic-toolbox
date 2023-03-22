def fibonacci_last_digit(n):
    
    #hardcode the zeroth and first element of Fibonacci sequence
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):

        #add only last digits. Last digits are obtained by doing a modulo operation
        previous, current = (current % 10), (previous % 10) + (current % 10)

    #provide only last digit. Done by doing a modulo operation
    return current % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
