def edit_distance(first_string, second_string):

    #Modified algorithm to find edit distance matrix using only: deletion, insertion or match.
    
    #create the delta matrix. Make sure to add a column and add a row
    num_rows=len(first_string)+1
    
    num_cols=len(second_string)+1
    row=[0]*num_cols
    matrix = [list(row) for _ in range(num_rows)]

    #print("blank matrix")
    #print(matrix)


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
    "Takes the matrix and outputs the match,,insertion, or deletion sequence. Longest common subseuqnece is calculated as number of matches"

    matrix=edit_distance(first_string, second_string)

    
    
    num_rows=len(matrix)
    num_cols=len(matrix[0])

    sequence=[]

    i=num_rows-1
    j=num_cols-1

    #Figure our current cell is deletion, insertion or match based on its relation with neighbor cells
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
            i=i-1
            j=j-1
            sequence.append("match")
        
    #The output sequence starts from end, so we reverse it
    sequence.reverse()
   

    #count the number of matches in a sequence
    counter=0
    for instance in sequence:
        if instance=="match":
            counter=counter+1
         

    return counter           

if __name__ == '__main__':
    
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    
    print(lcs2(a,b))
    

