# tool: rotate_list
# description: rotates a comma-separated list by n positions
# author: @Solaris-star
# example: rotate_list "a,b,c,d" "1" -> "b,c,d,a"


def run(*args) -> str:
    if len(args) != 2:
        return "Error: expected list and rotation count"
    items = [x.strip() for x in args[0].split(",")] if args[0] != "" else []
    try:
        n = int(args[1])
    except ValueError:
        return "Error: rotation count must be an integer"
    if not items:
        return ""
    n %= len(items)
    return ",".join(items[n:] + items[:n])
