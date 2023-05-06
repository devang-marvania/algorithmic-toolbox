

def compute_operations(n):
    
    #array to store number of operations required to reach index value. 
    #For example: dp[3]=1 indicates that 1(value stored at dp[3]) operation was required to reach 3(index) 
    dp = [0] * (n+1)

    #array to store the previous number before arriving to index value.
    #For example: prev[3]=1 indicates that before arriving to 3(index), the previous value in sequence was 1(value stored at prev[3])
    prev = [0] * (n+1)
   
   #Loop from 2 till n is reached and store the number of operations and previous values 
    for i in range(2, n+1):

        #If operation is incrementing by 1 to reach i, then its 1 incremental operation compared to operations required to reach i-1
        dp[i] = dp[i-1] + 1
        #If increment by 1 operation was used than previous value must be 1 less than i
        prev[i] = i-1
      

        #If i is divisible by 2 then see if multiplication by 2 results in less total operations
        if i % 2 == 0 and dp[i]> dp[i//2] + 1:

            #If multiplication by 2 is used, then total number of operations needed to reach i is 1 more than operations needed to reach till i//2
            dp[i] = dp[i//2] + 1

            #If multiplication by 2 was used, then previous number before reaching i must by i/2(or i//2)
            prev[i] = i//2
          
        #If i is divisible by 3 then see if multiplication by 3 results in less total operations  
        if i % 3 == 0 and dp[i] > dp[i//3]+1:
            
            #If multiplication by 3 is used, then total number of operations needed to reach i is 1 more than operations needed to reach till i//3
            dp[i] = dp[i//3] + 1
            
            #If multiplication by 3 was used, then previous number before reaching i must by i/3(or i//3)
            prev[i] = i//3
         

    #We start calculating output_sequence from reverse. 
    #Meaning we start with last element n and then append the one element before that and so on, till 1 is reached       
    output_sequence=[n]
  
    #Loop in reverse till 1 is reached
    while output_sequence[-1]!=1:
        #Always append the previous element of last element in output_sequence
        output_sequence.append(prev[output_sequence[-1]])
        
    #Reverse the sequence so that 1 is first and n is last
    output_sequence.reverse()


    return output_sequence



if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
 
