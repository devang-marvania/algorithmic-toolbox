def gcd(a, b):   
    
    #Use a swap if needed to ensure that a is always greater or equal to b
    if b>a:
        (a,b)=swap(a,b)

    #A recursive function is used to recursively caculate gcd of a%b and b till no remainder is present
    if b==0:
        return a
    else:
        return gcd(a%b,b)


def swap(a,b):

    "Custom swap function to ensure that first value a is always greater or equal to second value b"
    if a>=b:
        return a,b
    else:
        return b,a   


if __name__ == "__main__":
    a, b = map(int, input().split())
    #print(swap(a, b))
    print(gcd(a, b))
