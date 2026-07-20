# tool: clamp
# description: clamps a number between min and max
# author: @Solaris-star
# example: clamp "15" "0" "10" -> "10"


def run(*args) -> str:
    if len(args) != 3:
        return "Error: expected value, min, max"
    try:
        value = float(args[0])
        lo = float(args[1])
        hi = float(args[2])
    except ValueError:
        return "Error: arguments must be numbers"
    if lo > hi:
        lo, hi = hi, lo
    clamped = min(max(value, lo), hi)
    if clamped.is_integer():
        return str(int(clamped))
    return str(clamped)
