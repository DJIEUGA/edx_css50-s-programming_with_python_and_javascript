import math

def is_prime(n):
    
    # We know numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check factors up to sqrt(n)
    for i in range(2,int(math.sqrt(n))):

        # If i is a factor, return false
        if n % i == 0:
            return 
    # If no factors were found, return true
    return True   

 