
from sqlalchemy import Table,Column,Integer,String,TIMESTAMP,MetaData,text

metadata = MetaData()

operation = Table(
    "operation",
    metadata,
    Column("id",Integer, primary_key= True),
    Column("quantity",String),
    Column("figi",String),
    Column("instrument_type",String,nullable=True),
    Column("date",TIMESTAMP(timezone=True),
                        nullable=False,
                        server_default=text('now()')),
    Column("type",String)
)