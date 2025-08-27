from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database


# Buat router untuk item
router = APIRouter()
# Endpoint untuk CRUD operasi pada item
@router.get("/items", response_model=list[schemas.Item])
def read_items(db: Session = Depends(database.get_db)):
    return crud.get_items(db)

# Endpoint untuk mendapatkan item berdasarkan ID
@router.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = crud.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


# Endpoint untuk membuat item baru
@router.post("/items", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    return crud.create_item(db, item)


# Endpoint untuk memperbarui item berdasarkan ID
@router.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    updated = crud.update_item(db, item_id, item)
    if updated is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return 


# Endpoint untuk menghapus item berdasarkan ID
@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
    deleted = crud.delete_item(db, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}
