from pydantic import BaseModel

class {{cookiecutter.resource_name.capitalize()}}DTO(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
