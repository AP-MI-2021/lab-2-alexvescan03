#from datetime import datetime  # putem lucra cu variabile de tip date
import datetime

def printMenu():
    print("1.problema 5")
    print("2.problema 1")
    print("3.problema 2")
    print("4.exit program")

# problema 2
def get_age_in_days(day):
    """
    :param day:data nasterii acelei persoane
    :return:cate zile a trait
    """

    day = datetime.datetime.strptime(day , '%d/%m/%Y')

    number_of_days_since_day = (datetime.datetime.utcnow() - day).days  # diferenta dintre data actuala si data introdusa in zile

    return number_of_days_since_day  # numarul de zile


# problema 5
def is_palindrome(n):
    '''
    :param n: citeste un numar de la tastatura
    :return: returneaza daca este palindrom sau nu
    '''

    cn = n
    inv = 0

    while cn > 0:
        inv = inv * 10 + cn % 10
        cn = cn // 10

    ok = False

    if inv == n:
        ok = True

    return ok

# problema 1

def isPrime(x):
    '''
    :param x: un numar
    :return: returneaza True daca numarul este prim si false in caz contrar
    '''

    if (x <= 1):
        return False
    if (x == 2):
        return True
    if (x % 2 == 0):
        return False
    i = 3
    while (i * i <= x):
        if (x % i == 0):
            return False
        i += 2

    return True


def get_largest_prime_below(x):
    for i in range(x - 1, 1, -1):  # for(i = x-1 ; i > 1 ; i -=1)
        if (isPrime(i)):
            return i

    return 2


def test_is_palindrome():

    assert is_palindrome(5) == True

    assert is_palindrome(151) == True

    assert is_palindrome(253) == False

    assert is_palindrome(1002) == False

def test_get_largest_prime_below():

    assert get_largest_prime_below(15) == 13
    assert get_largest_prime_below(30) == 29
    assert get_largest_prime_below(32) == 31
    assert get_largest_prime_below(13) == 11

if(__name__ == "__main__"):

    test_get_largest_prime_below()
    test_is_palindrome()

    while (True):

        printMenu()

        optiune = input("Dati optiunea: ")

        if (optiune == "4"):
            break

        if optiune == "1":

            n = int(input("n = "))

            isPalindrome = is_palindrome(n)

            if (isPalindrome):
                print("{} este palindrom".format(n))
            else:
                print("{} nu este palindrom".format(n))

        elif optiune == "2":

            n = int(input("n = "))

            largestPrimeBelowN = get_largest_prime_below(n)

            print("Cel mai mic numar palindrom decat {} este {}".format(n, largestPrimeBelowN));

        elif optiune == "3":

            date = input("Data nasterii = ")

            #d = datetime.datetime.strptime(datestring , '%d/%m/%Y')

            days= get_age_in_days(date)

            print("Ai trait {} zile".format(days))