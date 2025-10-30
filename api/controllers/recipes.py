from sqlalchemy.orm import Session
from fastapi import Response, status
from api.models import models, schemas

def create(db: Session, recipe: schemas.RecipeCreate):
    db_obj = models.Recipe(**recipe.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def read_all(db: Session):
    return db.query(models.Recipe).all()

def read_one(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

def update(db: Session, recipe_id: int, recipe: schemas.RecipeUpdate):
    q = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    q.update(recipe.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return q.first()

def delete(db: Session, recipe_id: int):
    q = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    q.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
