def fibonacci_sum_squares(n):
    previous = 0
    current  = 1

    #Research about Pisano period

    period = [0,1]
    last_digit_squared_period=[0,1]

    #append values to period defined above and detect when the last 2 values match first 2 values. When it does, then period can be obtained by removing last 2 values
    for _ in range(n - 1):
        previous, current = (current % 10), (previous  + current) % 10
        period.append(current)

        #calculate last digit of fibonacci number sqaured and store in array for future use
        last_digit_squared_period.append((current%10)*(current%10))

        if period[-2:]==period[:2]:
            period=period[:-2]
            last_digit_squared_period=last_digit_squared_period[:-2]
            break

    #Find out how many complete periods are observed before this Fibonacci number comes
    complete_period=int(n/len(period))

    #Find the index of Fibonacci number in period
    reduced_index= n%len(period)
    
    #Calculate sum of fibonacci number squared's last digits
    sum_last_digit_squared = complete_period*sum(last_digit_squared_period) + sum(last_digit_squared_period[:reduced_index+1])
    
    #do a modulo operation to return last digit of the sum
    return sum_last_digit_squared % 10



if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
