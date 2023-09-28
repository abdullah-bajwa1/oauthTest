from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str  # You should hash and salt this password
