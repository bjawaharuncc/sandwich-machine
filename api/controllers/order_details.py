from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from api.models import models
from api.models import schemas





def create(db: Session, order_detail: schemas.OrderDetailCreate):
    db_order_detail = models.OrderDetail(
        order_id=order_detail.order_id,
        sandwich_id=order_detail.sandwich_id,
        amount=order_detail.amount
    )
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail


def read_all(db: Session):
    return db.query(models.OrderDetail).all()


def read_one(db: Session, order_detail_id: int):
    detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if detail is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order detail not found")
    return detail


def update(db: Session, order_detail_id: int, order_detail: schemas.OrderDetailUpdate):
    detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if detail is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order detail not found")
    detail.amount = order_detail.amount or detail.amount
    db.commit()
    db.refresh(detail)
    return detail


def delete(db: Session, order_detail_id: int):
    detail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_detail_id).first()
    if detail is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order detail not found")
    db.delete(detail)
    db.commit()
    return {"message": "Deleted successfully"}
