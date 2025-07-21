import re


def guess_hash_algorithm(sample_hash: str) -> str:
    if sample_hash.startswith(("$2a$", "$2b$", "$2y$")):
        return "bcrypt"
    elif sample_hash.startswith("$argon2"):
        return "argon2"
    elif sample_hash.startswith("$pbkdf2"):
        return "pbkdf2"
    elif re.fullmatch(r"[a-fA-F0-9]{64}", sample_hash):
        return "sha256_crypt"
    elif re.fullmatch(r"[a-fA-F0-9]{128}", sample_hash):
        return "sha512_crypt"
    elif re.fullmatch(r"[a-fA-F0-9]{32}", sample_hash):
        return "md5_crypt"
    else:
        return "bcrypt"  # Safe default
