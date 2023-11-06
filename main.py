from fastapi import FastAPI
import utils
import api_key
app = FastAPI()

from pydantic import BaseModel

class Item(BaseModel):
    file_name: str
    source_type: str
    row_count: int
    search_keys: list[str]
    api_key: str
    

@app.post("/addRow/")
async def add_item(item: Item):
    if api_key.verify_api_key(item.api_key):
        return utils.addRow(item.file_name, item.source_type, item.row_count, search_keys=item.search_keys)
    else:
        return {"msg": "api_key is invalid"}
    