from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import sqlite3

# Pydantic Model
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# FastAPI instance
app = FastAPI()

# Database connection
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS items
               (name TEXT, description TEXT, price REAL)''')


@app.post("/items/")
async def create_item(item: Item):
    """
    Create an item and save it to the database
    """
    try:
        cursor.execute('''INSERT INTO items(name, description, price)
                        VALUES(?,?,?)''', (item.name, item.description, item.price))
        conn.commit()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"message": "Item created successfully!"}