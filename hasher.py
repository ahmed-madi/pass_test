from passlib.context import CryptContext

# Default: bcrypt, argon2, sha256_crypt
pwd_context = CryptContext(
    schemes=["bcrypt", "argon2", "sha256_crypt"],
    deprecated="auto"
)


def hash_password(password: str, method: str) -> str:
    ctx = CryptContext(schemes=[method])
    return ctx.hash(password)


def verify_password(password: str, hashed: str, method: str) -> bool:
    ctx = CryptContext(schemes=[method])
    return ctx.verify(password, hashed)
