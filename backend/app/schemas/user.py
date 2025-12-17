import enum

from pydantic import BaseModel, EmailStr, Field


class UserRole(str, enum.Enum):
	ADMIN = "Admin"
	STAFF = "Staff"
	VIEWER = "Viewer"


class UserLogin(BaseModel):
	email: EmailStr
	password: str = Field(min_length=6)


class UserRead(BaseModel):
	id: int
	name: str
	email: EmailStr
	role: UserRole
	is_active: bool

	class Config:
		orm_mode = True
