__author__ = 'HSM Sharique Hasan'
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143
'''


def prime_factors(number):
    factors = []
    prime_number = 2
    while number > 1:
        while number % prime_number == 0:
            factors.append(prime_number)
            number /= prime_number
        prime_number += 1

    return factors

print(max(prime_factors(600851475143)))
