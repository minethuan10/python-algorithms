#look at line 10 so they pass 20 to a and 96 to 8
def gcd(a,b):
    #first check because 20!=0
    while(b!=0):
        t=a #t=20
        a=b #a=8
        b=t%b #b=20%8=4
        print(f'The remainder of b is {b}')  
    return a


print(gcd(20,8))