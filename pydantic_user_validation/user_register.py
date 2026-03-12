from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional


# Address Model
class Address(BaseModel):
    city: str = Field(min_length=3)
    pincode: str = Field(pattern="^[0-9]{6}$")


# User Model
class User(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    user_id: int
    name: str
    email: EmailStr
    age: int = Field(ge=18)
    address: Address
    is_premium: Optional[bool] = False


# Test Data
user = User(
    user_id=1,
    name="Kushal",
    email="kushal@gmail.com",
    age=22,
    address={
        "city": "Delhi",
        "pincode": "110001"
    }
)

print(user)



user.age = 25  