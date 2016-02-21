__author__ = 'HSM Sharique Hasan'


final_number = 1000
number = 1
sum = 0

while number < final_number:
    if number % 3 == 0 or number % 5 == 0:
        sum += number
    number += 1

print(sum)