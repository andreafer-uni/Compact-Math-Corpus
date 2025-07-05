import re

def check_long_tokens(conll_file, max_length=20):
    with open(conll_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    long_tokens = [
        parts[1] for line in lines
        if not line.startswith("#") and (parts := line.strip().split("\t")) and len(parts[1]) > max_length and not re.match(r"^[\W\d]+$", parts[1])
    ]
    print(f"{len(long_tokens)} anomalous tokens found.")
    return long_tokens[:20]
