# tool: sha1_hash
# description: Computes the SHA-1 hex digest of a string
# author: @Solaris-star
# example: sha1_hash "hello" -> "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"

import hashlib


def run(*args) -> str:
    text = " ".join(args)
    return hashlib.sha1(text.encode("utf-8")).hexdigest()

