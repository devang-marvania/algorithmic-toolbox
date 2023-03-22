def lcm(a, b):

    #Important: To find least common multiple of a and b, find the least common divisor(gcd) of a and b and then multiply a/gcd, b/gcd and gcd.
    
    #Calculate greatest common divisor of a and b
    gcd_a_b = gcd(a,b)

    #Calculate quotient after dividing a and b by greatest common divisor
    quotient_a = a/gcd_a_b
    quotient_b= b/gcd_a_b

    lcm = int(quotient_a*quotient_b*gcd_a_b)

    return lcm


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




if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

