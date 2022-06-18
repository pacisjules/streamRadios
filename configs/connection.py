import databases
import sqlalchemy
from functools import lru_cache
from configs import dbinfo
from db.table import metadata

@lru_cache()
def db_config():
    return dbinfo.Setting()

def DATABASE_URL(
    connection: str = "postgresql",
    username: str   = "qlmasrswywqndr",
    password: str   ="a015291058aed5a7c55bd51a62b291a6bc8e746969c101d8aff32ad723f680df",
    host: str       = "ec2-52-73-184-24.compute-1.amazonaws.com",
    port: str       = "5432",
    database: str   = "ec2-52-73-184-24.compute-1.amazonaws.com"
):
    return str(connection+"://qlmasrswywqndr:a015291058aed5a7c55bd51a62b291a6bc8e746969c101d8aff32ad723f680df@ec2-52-73-184-24.compute-1.amazonaws.com:5432/dcv839v8dctfto")

database = databases.Database(DATABASE_URL())

engine = sqlalchemy.create_engine(
    DATABASE_URL()
)

metadata.create_all(engine)