# tool: json_prettify
# description: pretty-prints a JSON string with indentation
# author: @Solaris-star
# example: json_prettify "{\"a\":1}" -> multi-line indented JSON

import json


def run(*args) -> str:
    if not args:
        return "Error: expected a JSON string"
    try:
        return json.dumps(json.loads(args[0]), indent=2, ensure_ascii=False)
    except json.JSONDecodeError as exc:
        return f"Error: {exc}"

