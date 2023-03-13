from pydantic import BaseModel,datetime_parse
from datetime import datetime


class OperationCreate(BaseModel):
    id: int
    quantity: str
    figi: str
    date:datetime
    instrument_type: str
    type: str
    class Config:
        orm_mode=True