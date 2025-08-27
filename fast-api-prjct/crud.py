from sqlalchemy.orm import Session
from . import models, schemas

# CRUD operations for Item model
def get_items(db: Session):
    return db.query(models.Item).all()
# Get a single item by ID
def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()
# Create a new item
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
# Delete an item by ID
def delete_item(db: Session, item_id: int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item:
        db.delete(item)
        db.commit()
        return True
    return False
# Update an existing item by ID
def update_item(db: Session, item_id: int, item_data: schemas.ItemCreate):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item:
        item.name = item_data.name
        item.description = item_data.description
        db.commit()
        db.refresh(item)
        return item
    return None
