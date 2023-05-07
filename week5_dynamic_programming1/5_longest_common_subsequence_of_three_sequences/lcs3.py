def lcs3(first_sequence, second_sequence, third_sequence):
    """This functions takes the two strings at a time and find the longest possible common 
    subsquence(using lcs2 and lcs2_updated).
    Then it takes these common sequence and compares with third string 
    and finally comes up with final answer
    """
    
    #For first 2 strings, we take the shorter 2.
    seqeuence_list=[first_sequence,second_sequence,third_sequence]

    sorted_sequence_list= sorted(seqeuence_list,key=len)

    first_string=sorted_sequence_list[0]
    second_string=sorted_sequence_list[1]
    third_string=sorted_sequence_list[2]

    #we figure our longest common subsequence(match_list_1 and match_list_2)
    #  using lcs2 and lcs2_updated.
    matches,match_list_1=lcs2(first_string, second_string)

    matches,match_list_2=lcs2_updated(first_string, second_string)

    '''
    if len(match_list_2)>len(match_list_1):
        match_list=match_list_2
    else:
        match_list=match_list_1
    '''

    #Next we take longest common subsequences derived using lcs2 and lcs2_updated and apply 
    # a third string and find the longest common subsequences using 
    # all three strings(match_list_3 and match_list_4)
    matches,match_list_3=lcs2_updated(third_string,match_list_1)
    matches,match_list_4=lcs2_updated(third_string,match_list_2)

    #find the longest common subsequence from 3 strings and count its length
    if len(match_list_3)>len(match_list_4):
        num_matches=len(match_list_3)
    else:
        num_matches=len(match_list_4)
    
    
    
    return num_matches


def edit_distance(first_string, second_string):

    #Modified algorithm to find edit distance matrix using only: deletion, insertion or match.
    
    #create the delta matrix. Make sure to add a column and add a row
    num_rows=len(first_string)+1
    
    num_cols=len(second_string)+1
    row=[0]*num_cols
    matrix = [list(row) for _ in range(num_rows)]

    


    #setting up the first column
    for i in range(num_rows):
        matrix[i][0]=i

    #setting up the first row
    for j in range(num_cols):
        matrix[0][j]=j

    #Loop thorugh first column, then second and so on...Use only insertion, deletion or match to calculate edit distance
    for j in range(1,num_cols):
        for i in range(1,num_rows):
            
            #calcualte edit distance for each case
            insertion=matrix[i][j-1]+1
            deletion=matrix[i-1][j]+1
            match=matrix[i-1][j-1]
            
            #edit distance when there is a match
            if first_string[i-1]==second_string[j-1]:               
              matrix[i][j]=min(insertion,deletion,match)
            #edit distance when there is no match
            else:                
              matrix[i][j]=min(insertion,deletion) 

    #return the resulting matrix with edit distances
    return matrix

def lcs2(first_string,second_string):
    #Takes the 2 strings and outputs the number of elements and longest common seubsequence
    #and actual Longest common subseuqnece is calculated as number of matches"

    #get the delta matrix between 2 strings
    matrix=edit_distance(first_string, second_string)

    
    #figure out the starting point of backtracking
    num_rows=len(matrix)
    num_cols=len(matrix[0])
    sequence=[]
    match_list=[]
    i=num_rows-1
    j=num_cols-1

    #Figure our current cell is deletion, insertion or match based on its relation with neighbor cells.
    #In case of tie between deletion and insertion, deletion is preferred
    while i!=0 or j!=0:
        if i>0 and matrix[i][j]==(matrix[i-1][j]+1):
            i=i-1
            j=j
            sequence.append("deletion")
        elif j>0 and matrix[i][j]==(matrix[i][j-1]+1):
            i=i
            j=j-1
            sequence.append("insertion")
        else:
            match_list.append(first_string[i-1])
            i=i-1
            j=j-1
            sequence.append("match")
        
    #The output sequence starts from end, so we reverse it
    sequence.reverse()
    match_list.reverse()
   

    #count the number of matches in a sequence
    counter=0
    for instance in sequence:
        if instance=="match":
            counter=counter+1

       
         

    return counter,match_list 


def lcs2_updated(first_string,second_string):
    #Takes the 2 strings and outputs the number of elements and longest common seubsequence
    #and actual Longest common subseuqnece is calculated as number of matches"

    #get the delta matrix between 2 strings
    matrix=edit_distance(first_string, second_string)

    
    #figure out the starting point of backtracking
    num_rows=len(matrix)
    num_cols=len(matrix[0])
    sequence=[]
    match_list=[]
    i=num_rows-1
    j=num_cols-1

    #Figure our current cell is deletion, insertion or match based on its relation with neighbor cells.
    #In case of tie between deletion and insertion, insertion is preferred
    while i!=0 or j!=0:
        if j>0 and matrix[i][j]==(matrix[i][j-1]+1):
            i=i
            j=j-1
            sequence.append("insertion")
        elif i>0 and matrix[i][j]==(matrix[i-1][j]+1):
            i=i-1
            j=j
            sequence.append("deletion")
        else:
            match_list.append(first_string[i-1])
            i=i-1
            j=j-1
            sequence.append("match")
        
    #The output sequence starts from end, so we reverse it
    sequence.reverse()
    match_list.reverse()
   

    #count the number of matches in a sequence
    counter=0
    for instance in sequence:
        if instance=="match":
            counter=counter+1

         
         

    return counter,match_list       

if __name__ == '__main__':
   
    
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
    
    """
    a=[1,2,3]
    b=[1,3,2]

    print("lcs2 of ",a,"and",b,"is",lcs2_updated(a,b))
    """