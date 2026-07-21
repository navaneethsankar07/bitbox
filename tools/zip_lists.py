# tool: zip_lists
# description: zips two comma-separated lists into pairs
# author: @Solaris-star
# example: zip_lists "a,b" "1,2" -> "a:1,b:2"


def run(*args) -> str:
    if len(args) != 2:
        return "Error: expected two comma-separated lists"
    left = [x.strip() for x in args[0].split(",")]
    right = [x.strip() for x in args[1].split(",")]
    pairs = [f"{a}:{b}" for a, b in zip(left, right)]
    return ",".join(pairs)
