# tool: fibonacci
# description: returns the n-th Fibonacci number (0-indexed)
# author: @Solaris-star
# example: fibonacci "10" -> "55"


def run(*args) -> str:
    if not args:
        return "Error: expected n"
    try:
        n = int(args[0])
    except ValueError:
        return "Error: n must be an integer"
    if n < 0:
        return "Error: n must be >= 0"
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return str(a)
