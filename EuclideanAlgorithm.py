import sys
import math

def main():
    if len(sys.argv) != 3:
        print("Usage: Euclidean.py a b\n"
            "Prints greatest common divisor of a and b "
            "found by Euclidean Algorithm.")
    else:
        a, b = int(sys.argv[1]), int(sys.argv[2])
        gcd = gcdByEuclideanAlgorithm(a, b)
        print "gcd({}, {}) = {}".format(a, b, gcd)

def gcdByEuclideanAlgorithm(a, b):
    if b > a: # Ensure a > b.
        a, b = b, a
    quotient = float(a) / float(b) # Calculate decimal quotient.
    q = math.floor(quotient) # From decimal quotient, derive integer quotient...
    r = int((quotient - q) * b) # ...and remainder.
    if r == 0: # If remainder is 0...
        return b # ...return previous remainder.
    else: # Otherwise repeat procedure using b as the new a and r as the new b.
        return gcdByEuclideanAlgorithm(b, r)

if __name__ == '__main__':
    main()
