def printMenu
    print("1.problema 5")
    print("2.problema 1")
    print("3.problema 2")
def main():
    printMenu()
    optiune = input("Dati optiunea:")
    if optiune == "1":
        is_palindrome()
    if optiune == "2":
        get_largest_prime_below()
    if optiune == "3":
        get_age_in_days()
main()
#problema 5

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
    if ok == True:
        print("da")
    else:
        print("nu")


def test_is_palindrome():
    assert is_palindrome(121) is True
    assert is_palindrome(100) is False
    assert is_palindrome(116) is False
    assert is_palindrome(333) is True
    n = int(input("n="))
    m = is_palindrome(n)
    print(m)


test_is_palindrome()

#problema 1
def get_largest_prime_below(x):
    '''

    :param x: citim un numar de la tastatura
    :return: ne returneaza ultimul numar prim mai mic decat acesta
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
    for i in range(n - 1, 1, -1):
        if (get_largest_prime_below(i)):
            print("numarul {} este prim".format(i))
        break


def test_get_largest_prime_below(n):
    n = int(input("n="))
    assert get_largest_prime_below(12) == 11
    assert get_largest_prime_below(10) == 7
    assert get_largest_prime_below(25) == 13
    assert get_largest_prime_below(5) == 3
    m = test_get_largest_prime_below(n)
    print(m)


test_get_largest_prime_below()

#problema 2
def get_age_in_days(day):
    '''

    :param day: data nasterii
    :return: varsta persoanei
    '''
  from datetime import datetime #putem lucra cu variabile de tip date
  number_of_days_since_day = (datetime.utcnow() - day).days #diferenta dintre data actuala si data introdusa in zile
  return number_of_days_since_day #numarul de zile