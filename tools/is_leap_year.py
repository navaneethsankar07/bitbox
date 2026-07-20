# tool: is_leap_year
# description: checks whether a year is a Gregorian leap year
# author: @Solaris-star
# example: is_leap_year "2020" -> "true"

import calendar


def run(*args) -> str:
    if not args:
        return "Error: expected a year"
    try:
        year = int(args[0])
    except ValueError:
        return "Error: year must be an integer"
    return "true" if calendar.isleap(year) else "false"

