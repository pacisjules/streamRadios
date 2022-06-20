import sqlalchemy
from sqlalchemy import ForeignKey
metadata = sqlalchemy.MetaData()

#Start and Configuration


#1 Table App Admins
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("username"  , sqlalchemy.String, unique=True),
    sqlalchemy.Column("password"  , sqlalchemy.String),
    
    sqlalchemy.Column("first_name"  , sqlalchemy.String),
    sqlalchemy.Column("last_name"  , sqlalchemy.String),


    sqlalchemy.Column("email"     , sqlalchemy.String, unique=True),
    sqlalchemy.Column("type"     , sqlalchemy.String),
    sqlalchemy.Column("role"     , sqlalchemy.String),

    sqlalchemy.Column("company"     , sqlalchemy.String),
    sqlalchemy.Column("phone"     , sqlalchemy.String, unique=True),
    sqlalchemy.Column("living"     , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)

#2 Table Radios
radios  = sqlalchemy.Table(
    "radios",
    metadata,
    sqlalchemy.Column("radio_id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("radio_name"  , sqlalchemy.String),
    sqlalchemy.Column("stream_link"  , sqlalchemy.String),

    sqlalchemy.Column("logo_link"    , sqlalchemy.String),
    sqlalchemy.Column("back_imgLink"  , sqlalchemy.String),
    sqlalchemy.Column("channel"  , sqlalchemy.String),
    sqlalchemy.Column("country"    , sqlalchemy.String),
    sqlalchemy.Column("gerne"    , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


#3 Table account recovery Keys
account_keys  = sqlalchemy.Table(
    "account_keys",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),

    sqlalchemy.Column("key"  , sqlalchemy.String, unique=True, nullable=False),
    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
)


