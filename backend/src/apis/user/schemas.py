from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    first_name: str
    second_name: str
    middle_name: str
    email: EmailStr
    username: str

class UserCreateSchema(UserSchema):
    password: str = Field(..., min_length=8, max_length=128)


class UserUpdateSchema(UserCreateSchema):
    pass
