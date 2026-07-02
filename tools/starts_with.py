# tool: starts_with
# description: checks if a string starts with a given prefix
# author: @navaneethsankar07
# example: starts_with("hello world", "hello") returns True


def run(*args) -> bool:
    string = args[0]
    prefix = args[1]
    return string.startswith(prefix)