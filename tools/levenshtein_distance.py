# tool: levenshtein_distance
# description: Computes the Levenshtein edit distance between two strings
# author: @Solaris-star
# example: levenshtein_distance "kitten" "sitting" -> "3"

def run(*args) -> str:
    if len(args) != 2:
        return "Error: Expected exactly 2 arguments."
    a, b = args[0], args[1]
    if a == b:
        return "0"
    if not a:
        return str(len(b))
    if not b:
        return str(len(a))
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            ins = cur[j - 1] + 1
            delete = prev[j] + 1
            sub = prev[j - 1] + (ca != cb)
            cur.append(min(ins, delete, sub))
        prev = cur
    return str(prev[-1])
