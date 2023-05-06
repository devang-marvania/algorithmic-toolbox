

def edit_distance(first_string, second_string):
    
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

    #Loop thorugh first column, then second and so on...
    for j in range(1,num_cols):
        for i in range(1,num_rows):
            insertion=matrix[i][j-1]+1
            deletion=matrix[i-1][j]+1
            match=matrix[i-1][j-1]
            mismatch=matrix[i-1][j-1]+1

            if first_string[i-1]==second_string[j-1]:
                
              
                matrix[i][j]=min(insertion,deletion,match)
            else:
                
                matrix[i][j]=min(insertion,deletion,mismatch)

 

    #return the editing distance for last element in matrix
    return matrix[num_rows-1][num_cols-1]                        



    
    


if __name__ == "__main__":
    print(edit_distance(input(), input()))
