import re

def count_long_tokens(conll_file, length_threshold=20):
    long_token_count = 0
    long_tokens = []

    with open(conll_file, "r", encoding="utf-8") as infile:
        for line in infile:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) >= 3:
                token = parts[1]
                if len(token) > length_threshold and not re.match(r"^[\W\d]+$", token):
                    long_token_count += 1
                    long_tokens.append(token)

    return long_token_count, long_tokens
