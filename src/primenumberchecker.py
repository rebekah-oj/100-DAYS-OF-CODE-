n = int(input("Check this number: "))


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
        if is_prime:
            print("It is a prime number.")
            break
        else:
            print("It's not a prime number.")


prime_checker(number=n)

"""
def prime_checker(number):
    if n > 1:
        for i in range(2, n // 2):
            if (n % i) == 0:
                print("It is not prime number")
                break
    else:
        print("It is a prime number")
           else:
    print()"""
