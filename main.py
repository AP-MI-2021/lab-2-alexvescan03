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


