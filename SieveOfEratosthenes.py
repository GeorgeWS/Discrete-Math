import sys
import math

def main():
    if len(sys.argv) != 2:
        print("Usage: Eratosthenes.py n\n"
        "Prints all primes less than or equal to n "
        "found by the Sieve of Eratosthenes.")
    else:
        n = int(sys.argv[1])
        print primesBySieveOfEratosthenes(n)

def primesBySieveOfEratosthenes(n):
    """Returns the set of all primes less than or equal to n found by the Sieve
    of Eratosthenes"""
    sieve = set([i for i in range(2, n + 1)]) # Start with [2, n]
    # For everything in the sieve up to the square root of n...
    for i in range(2, int(math.sqrt(n)) + 1):
        if i in sieve:
            # Remove all multiples of i (only considering those less than n,
            # i.e. those that were in the sieve to begin with).
            for j in range(2, int(n / i) + 1):
                if i * j in sieve:
                    sieve.remove(i * j)
    # The primes less than or equal to n are whatever is left in the sieve!
    return sieve

if __name__ == '__main__':
    main()
