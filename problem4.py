__author__ = 'HSM Sharique Hasan'


def find_largest_palindrome():
    limit = 999
    minimum = 1
    palindromes = []
    while minimum <= limit:
        iterator = 1
        while iterator <= limit:
            resultant = minimum * iterator
            is_it_palindrome = check_if_number_is_palindrome(resultant)
            if is_it_palindrome:
                palindromes.append(resultant)
            iterator += 1
        minimum += 1
    return max(palindromes)


def check_if_number_is_palindrome(number):
    chars = list(str(number))
    reverse_chars = chars[::-1]
    return reverse_chars == chars


print(find_largest_palindrome())
