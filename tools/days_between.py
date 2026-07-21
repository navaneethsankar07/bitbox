# tool: days_between
# description: number of days between two dates (YYYY-MM-DD)
# author: @Solaris-star
# example: days_between "2020-01-01" "2020-01-11" -> "10"

from datetime import date


def run(*args) -> str:
    if len(args) != 2:
        return "Error: expected two dates YYYY-MM-DD"
    try:
        a = date.fromisoformat(args[0])
        b = date.fromisoformat(args[1])
    except ValueError:
        return "Error: dates must be YYYY-MM-DD"
    return str(abs((b - a).days))

