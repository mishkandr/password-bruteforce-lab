import string

def build_alphabet(include_digits, iclude_lowercase, include_uppercase, include_symbols):
    result = ""

    if include_digits:
        result += string.digits

    if iclude_lowercase:
        result += string.ascii_lowercase

    if include_uppercase:
        result += string.ascii_uppercase

    if include_symbols:
        result += string.punctuation

    if not result:
        raise ValueError("Select at least one character group")

    return result