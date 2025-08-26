#Import necessary libraries omg bisa autocomplete dari sini langsung, ga espek seriusan
from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

#start of the FastAPI application boleh boleh
app = FastAPI()


# Define a Pydantic model for the item (Mendifinisikan model Pydantic untuk item)
# This model will be used to validate the request body for item  (Ini model akan digunakan untuk memvalidasi body request untuk item)
class Item(BaseModel):
    nama: str
    deskripsi: Optional[str] = None
    harga: float

#uhh kita simpan datanya sementara di sini, nanti bisa diganti pakai database
fake_db = []


# Define a route to create an item (Mendefinisikan rute untuk membuat item)


#nah yang kita buat pertama adalah route untuk membuat item, ini akan menerima data dari request body
@app.post("/items/" , response_model=Item)
def create_item(item: Item):
    # Simpan item ke dalam fake_db (Simpan item ke dalam fake_db)
    fake_db.append(item)
    return item


# Define a route to read all items (Mendefinisikan rute untuk membaca semua item)
@app.get("/items/", response_model=List[Item])
def get_items():
    return fake_db
    
# Define a route to read a specific item by its index (Mendefinisikan rute untuk membaca item tertentu berdasarkan indeksnya)
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id < 0 or item_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[item_id]

#Define a route to update an item by its index (Mendefinisikan rute untuk memperbarui item berdasarkan indeksnya)
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id < 0 or item_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="Item not found")
    fake_db[item_id] = item
    return update_item

# Define a route to delete an item by its index (Mendefinisikan rute untuk menghapus item berdasarkan indeksnya)
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = fake_db.pop(item_id)
    return {"detail": "Item deleted", "item": deleted_item}