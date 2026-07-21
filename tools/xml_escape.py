# tool: xml_escape
# description: escapes XML special characters in a string
# author: @Solaris-star
# example: xml_escape "<tag>" -> "&lt;tag&gt;"

import xml.sax.saxutils as saxutils


def run(*args) -> str:
    if not args:
        return "Error: expected a string argument"
    return saxutils.escape(args[0], entities={'"': "&quot;", "'": "&apos;"})

