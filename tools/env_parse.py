# tool: env_parse
# description: Parses a .env-style string and returns all key=value pairs as JSON
# author: @shayneww
# example: env_parse "FOO=bar\nBAZ=qux" -> "{\"FOO\": \"bar\", \"BAZ\": \"qux\"}"

import json


def run(env_content: str) -> str:
    # Ensure the input is a string
    if not isinstance(env_content, str):
        raise TypeError(f"env_content must be a string, got {type(env_content).__name__}")

    # Normalize literal "\n" sequences from cli
    env_content = env_content.replace('\\n', '\n')
    divided_lines = env_content.split('\n')

    env_content_dict = {}

    for line in divided_lines:
        line = line.strip()

        # Skip empty lines, comments or lines without key=value
        if not line or line.startswith('#') or '=' not in line:
            continue

        # Split only on the first key=value to allow '=' characters
        key, value = line.split('=', 1)
        key = key.strip()
        value = value.strip()

        # Strip quotes from the value if present (only if user passed an actual pair)
        if len(value) >= 2 and (
            (value.startswith('"') and value.endswith('"')) or
            (value.startswith("'") and value.endswith("'"))
        ):
            value = value[1:-1]

        env_content_dict[key] = value

    return json.dumps(env_content_dict)