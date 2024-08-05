from sqlalchemy.orm import Session
from .models import {{cookiecutter.resource_name.capitalize()}}
from .dtos import {{cookiecutter.resource_name.capitalize()}}DTO

class {{cookiecutter.resource_name.capitalize()}}Service:
    def __init__(self, db: Session):
        self.db = db

    def get_{{cookiecutter.resource_name}}(self, id: int) -> {{cookiecutter.resource_name.capitalize()}}DTO:
        return self.db.query({{cookiecutter.resource_name.capitalize()}}).filter({{cookiecutter.resource_name.capitalize()}}.id == id).first()

    def create_{{cookiecutter.resource_name}}(self, {{cookiecutter.resource_name}}_dto: {{cookiecutter.resource_name.capitalize()}}DTO) -> {{cookiecutter.resource_name.capitalize()}}:
        db_{{cookiecutter.resource_name}} = {{cookiecutter.resource_name.capitalize()}}(**{{cookiecutter.resource_name}}_dto.dict())
        self.db.add(db_{{cookiecutter.resource_name}})
        self.db.commit()
        self.db.refresh(db_{{cookiecutter.resource_name}})
        return db_{{cookiecutter.resource_name}}
    