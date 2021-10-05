#problema 1
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

#problema 5
def is_palindrome(n):
    cn=n
    inv=0
    while cn>0:
        inv=inv*10 + cn%10
        cn=cn//10
    ok=False
    if inv==n:
        ok=True
    if ok==True:
        print("da")
    else:
        print("nu")

def main():
    n=int(input("n="))
    m=is_palindrome(n)
    print(m)
main()

#problema 2
def get_age_in_days(day):
  from datetime import datetime
  number_of_days_since_day = (datetime.utcnow() - day).days
  return number_of_days_since_day