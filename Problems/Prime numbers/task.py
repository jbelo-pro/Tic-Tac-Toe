
prime_numbers = [n for n in range(2, 1001) if all([n % r for r in range(2, n)])]


