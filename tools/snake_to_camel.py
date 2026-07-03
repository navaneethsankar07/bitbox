# tool: snake_to_camel
# description: converts a snake_case string to camelCase
# author: @navaneethsankar07
# example: snake_to_camel("hello_world") returns "helloWorld"


def run(*args) -> str:
    text = args[0]
    parts = text.split("_")
    return parts[0] + "".join(word.capitalize() for word in parts[1:])
