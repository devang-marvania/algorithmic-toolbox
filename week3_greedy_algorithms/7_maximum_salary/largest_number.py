from itertools import permutations

""" 
Note: A totally different implementation is possible by comparing strings. Just need to ensure that each number is convered to string and all strings are
repeated by 3 times, this way you can compare the strings and sort in descreasing order. Below is one example taken from Chat GPT
"""

def largest_number_naive(numbers):
    # Convert numbers to strings and sort them in descending order based on their concatenated value
    sorted_numbers = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    # Concatenate the sorted numbers and return the result as an integer
    return int(''.join(sorted_numbers))

"""
# Below implementation by Devang failed the test cases such as [1,128,11,1111,13]
def largest_number_naive(numbers):
    

    numbers=list(map(int,numbers))

    #create a dictionary with key as number and first value is the instances this number has appeared
    counts=count_duplicate(numbers)

    #add a second value to counts dictionary. This second value is the most important digit    
    for key in counts:           
        imp_digit=most_important_digit(key) 

        #Note: You can append a second value to existing key only if first value attached is in list form 
        counts[key].append(imp_digit)
       

    #Sort the dictionary in descreasing order of most_important_digit. If there are two keys with same most important digit then bias towards the smaller original number.
    sorted_counts=dict(sorted(list(counts.items()),key=lambda item:(item[1][1],-item[0]),reverse=True))

    number_string=[]

    #Append the numbers by attaching keys of sorted_dict. If same number has appeared more then attach same number more times.
    for count in sorted_counts:
        appearances = sorted_counts[count][0]
        while appearances>0:
            number_string.append(str(count))
            appearances = appearances-1

    combined_num_str = ''.join(number_string)
    combined_num = int(combined_num_str)      
 

    return combined_num

def most_important_digit(n):
    "This function takes a single or multi digit number and produces the single digit which is at highest decimal place. For example, most_important_digit(119)=1,"
    "most_important_digit(765)=7,most_important_digit(1)=1"

    if n<=9:
        result=n

    else:
        m=1
        while(int(n / (10**m)) != 0):
            m=m+1
        result = int(n / (10 **(m-1)))

    return result     

def count_duplicate(numbers):
    "Counts the duplicate appearances of the number and stores in a dictionary"

    counts={}

    for number in numbers:
        if number in counts:
            counts[number] = [counts[number]+1]
        else:
            counts[number] = [1]


    return counts           
"""



if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    #print("Devang's implementation:",largest_number_naive(input_numbers))
    #print("Chat GPT implementation:",compile_largest_number(input_numbers))
    print(largest_number_naive(input_numbers))

