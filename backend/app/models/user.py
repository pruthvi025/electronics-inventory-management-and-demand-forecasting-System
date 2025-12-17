import enum

from sqlalchemy import Boolean, Column, DateTime, Enum, Integer, String, func

from app.database.session import Base


class UserRole(str, enum.Enum):
	ADMIN = "Admin"
	STAFF = "Staff"
	VIEWER = "Viewer"


class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String(255), nullable=False)
	email = Column(String(255), unique=True, index=True, nullable=False)
	hashed_password = Column(String(255), nullable=False)
	role = Column(Enum(UserRole), nullable=False, default=UserRole.VIEWER)
	is_active = Column(Boolean, nullable=False, default=True)
	created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
