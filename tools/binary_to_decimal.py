# tool: binary_to_decimal
# description: converts a binary string to its decimal integer value
# author: @Solaris-star
# example: binary_to_decimal "1010" -> "10"


def run(*args) -> str:
    try:
        return str(int(args[0], 2))
    except (ValueError, IndexError):
        bad = args[0] if args else ""
        return f"Error: '{bad}' is not a valid binary string"

