# tool: is_prime
# description: checks whether an integer is prime
# author: @Solaris-star
# example: is_prime "17" -> "true"


def run(*args) -> str:
    if not args:
        return "Error: expected an integer"
    try:
        n = int(args[0])
    except ValueError:
        return "Error: argument must be an integer"
    if n <= 1:
        return "false"
    if n <= 3:
        return "true"
    if n % 2 == 0 or n % 3 == 0:
        return "false"
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return "false"
        i += 6
    return "true"
