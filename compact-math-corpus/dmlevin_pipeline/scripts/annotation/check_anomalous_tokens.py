
import re

def check_anomalous_tokens(conll_file, length_threshold=20):
    """Counts how many anomalous (too long) tokens there are in the CoNLL file."""
    long_token_count = 0
    long_tokens = []

    with open(conll_file, "r", encoding="utf-8") as infile:
        for line in infile:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            parts = line.split("\t")
            if len(parts) >= 3:
                token = parts[1]  # The token is the second column
                if len(token) > length_threshold and not re.match(r"^[\W\d]+$", token):  # Ignores isolated numbers and symbols
                    long_token_count += 1
                    long_tokens.append(token)

    return long_token_count, long_tokens

if __name__ == "__main__":
    conll_path = "dmlevin.conll"
    num_long_tokens, long_tokens_list = check_anomalous_tokens(conll_path)
    print(f"Number of anomalous tokens found: {num_long_tokens}")
    print("Examples of incorrect tokens:")
    print(long_tokens_list[:20])
