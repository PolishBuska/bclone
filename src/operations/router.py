import sqlalchemy.exc
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.dialects.postgresql import asyncpg
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from src.operations.schemas import OperationCreate
from src.database import get_async_session
from src.operations.models import operation


router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)

@router.get("/")
async def get_operations(type: str
                         ,session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == type)
    result = await session.execute(query)
    return {'result':result.first()}

@router.post("/")
async def add_operations(new_operation: OperationCreate,session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await  session.execute(stmt)
    await session.commit()
    return {"status":"ТРАХАТЬСЯ ААААААААААААААААААААА"}