from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.utils.jwt_handler import create_access_token
from app.utils.password_hash import verify_password


def authenticate_user(db: Session, email: str, password: str) -> str:
	user = db.query(User).filter(User.email == email).first()

	if not user or not verify_password(password, user.hashed_password):
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="Invalid email or password",
			headers={"WWW-Authenticate": "Bearer"},
		)

	if not user.is_active:
		raise HTTPException(
			status_code=status.HTTP_403_FORBIDDEN,
			detail="User account is inactive",
		)

	role_value = user.role.value if hasattr(user.role, "value") else str(user.role)
	return create_access_token(user_id=user.id, role=role_value)
