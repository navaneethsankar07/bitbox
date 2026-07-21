# tool: word_frequency
# description: Counts frequency of each word in a string
# author: @Solaris-star
# example: word_frequency "a a b" -> "a: 2, b: 1"

from collections import Counter
import re

def run(*args) -> str:
    if len(args) != 1:
        return "Error: Expected exactly 1 argument."
    words = re.findall(r"\w+", args[0].lower())
    if not words:
        return ""
    counts = Counter(words)
    return ", ".join(f"{w}: {c}" for w, c in counts.most_common())
