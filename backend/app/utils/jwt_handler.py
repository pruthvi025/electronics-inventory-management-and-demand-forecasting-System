import os
from datetime import datetime, timedelta
from typing import Any, Dict

from jose import jwt


SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

if not SECRET_KEY:
	raise RuntimeError("JWT_SECRET_KEY environment variable is required")


def _build_payload(user_id: int, role: str) -> Dict[str, Any]:
	expire_at = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
	return {"user_id": user_id, "role": role, "exp": expire_at}


def create_access_token(*, user_id: int, role: str) -> str:
	payload = _build_payload(user_id, role)
	return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
