from passlib.context import CryptContext

# bcrypt_sha256 hashes password after SHA256 to avoid bcrypt length limits.
_pwd_context = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto")


def hash_password(password: str) -> str:
	"""Hash a plaintext password using bcrypt."""

	return _pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
	"""Verify a plaintext password against its hash."""

	return _pwd_context.verify(plain_password, hashed_password)
