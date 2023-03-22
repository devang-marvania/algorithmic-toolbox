def fibonacci_number(n):
    
    #hardcode the zeroth and first element in fobonacci sequence
    fibonacci_numbers=[0,1]
    
    #run a loop for higher entries
    if n>1:
        for i in range(2,n+1): 
            new_number=fibonacci_numbers[i-1]+fibonacci_numbers[i-2]
            fibonacci_numbers.append(new_number)
    
  
    #return the answer depending on input
    if n==0:
        return fibonacci_numbers[n]
    elif n==1:
        return fibonacci_numbers[n]
    else: 
        return fibonacci_numbers[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
