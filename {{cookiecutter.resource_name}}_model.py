from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

class {{cookiecutter.resource_name.capitalize()}}(Base):
    __tablename__ = "{{cookiecutter.resource_name.lower()}}s"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class {{cookiecutter.resource_name.capitalize()}}DTO(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
