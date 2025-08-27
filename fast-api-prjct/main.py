from fastapi import FastAPI
from .import models, database
from .routes import items

# Buat tabel database
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Include router dari routes/items.py
app.include_router(items.router)
