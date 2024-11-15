# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
# is_prime = True
# for a in range(2, len(numbers)+1):
#     b = 0
#     for i in range(2, a // 2 + 1):
#         if (a % i == 0):
#             b = b + 1
#     if (b <= 0):
#         is_prime = False
#         primes.append(a)
#     else:
#         not_primes.append(a)
# print("Primes:", primes)
# print("Not Primes:", not_primes)


# Primes: [2, 3, 5, 7, 11, 13]
# Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]