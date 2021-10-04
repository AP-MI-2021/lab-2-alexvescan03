def get_largest_prime_below(x):
    if(x<=1):
        return False
    if(x==2):
        return True
    if(x%2==0):
        return False

    i=3
    while(i*i<=x):
        if(x%i==0):
            return False
        i+=2
    return True

n=int(input("n="))

for i in range(n-1,1,-1):
    if(get_largest_prime_below(i)):
        print("numarul {} este prim".format(i))
        break