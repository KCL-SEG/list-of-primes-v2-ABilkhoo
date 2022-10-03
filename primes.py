"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if type(number_of_primes) != int:
        raise TypeError("number_of_primes must be an int")
    if number_of_primes <= 0:
        raise ValueError("number_of_primes must be positive")


    list = []
    
    i = 2
    while len(list) < number_of_primes:
        prime = True;
        for item in list:
            if i % item == 0:
                prime = False;
                break;
        
        if prime == True:
            list.append(i)
        i += 1

    return list
