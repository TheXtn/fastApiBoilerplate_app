from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .dependencies import get_db
from .models import {{cookiecutter.resource_name.capitalize()}}DTO
from .services import {{cookiecutter.resource_name.capitalize()}}Service

router = APIRouter()

@router.get("/{{cookiecutter.resource_name}}s/{id}", response_model={{cookiecutter.resource_name.capitalize()}}DTO)
def read_{{cookiecutter.resource_name}}(id: int, db: Session = Depends(get_db)):
    service = {{cookiecutter.resource_name.capitalize()}}Service(db)
    {{cookiecutter.resource_name}} = service.get_{{cookiecutter.resource_name}}(id)
    if {{cookiecutter.resource_name}} is None:
        raise HTTPException(status_code=404, detail="{{cookiecutter.resource_name.capitalize()}} not found")
    return {{cookiecutter.resource_name}}

@router.post("/{{cookiecutter.resource_name}}s/", response_model={{cookiecutter.resource_name.capitalize()}}DTO)
def create_{{cookiecutter.resource_name}}({{cookiecutter.resource_name}}_dto: {{cookiecutter.resource_name.capitalize()}}DTO, db: Session = Depends(get_db)):
    service = {{cookiecutter.resource_name.capitalize()}}Service(db)
    return service.create_{{cookiecutter.resource_name}}({{cookiecutter.resource_name}}_dto)
