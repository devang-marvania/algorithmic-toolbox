def optimal_summands(n):
    summands = []
    # write your code here
    number=0
    summation=0


# Max number of prizes are possible when every prize is incrementing by 1 except the last prize. If last prize needs to be increased by more than 1 compared to its predecessor,
#so that total is equal to n then do it. Below logic implements the same thing.
    while summation<n:
        number=number+1
        summation=summation+number
        summands.append(number)
        #print("total is",sum(summands))

    total_sum=sum(summands)
    
    #Adjust last element if total increases
    if total_sum>n:
        summands.remove(summands[-1])
        difference = n - sum(summands)
        new_last_number=summands[-1]+difference
        summands[-1]=new_last_number

    '''
    if total_sum==n:
        print("everything is right")
    else:
        print("something is wrong, sum is higher than n")
    '''        
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
