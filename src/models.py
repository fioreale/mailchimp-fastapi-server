from pydantic import BaseModel

class FormData(BaseModel):
    name: str
    surname: str
    email: str
    number: str = None  # Optional
