from sqlalchemy import MetaData,JSON,Column,Table,Integer,String,TIMESTAMP,ForeignKey
from datetime import datetime
metadata = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String,nullable=False),
    Column("permissions",JSON),

)

users = Table(
    "users",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("email",String,primary_key=True),
    Column("username",String,nullable=False),
    Column("password",String,nullable=False),
    Column("registered_at",TIMESTAMP,default=datetime.utcnow),
    Column("role_id", Integer,ForeignKey(roles.c.id)),
)


