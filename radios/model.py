from pydantic import BaseModel, Field

class RadioCreate(BaseModel):

    user_id:str =  Field(..., example="user id")
    radio_name:str =  Field(..., example="Names of radio")
    stream_link:str =  Field(..., example="stream_link")
    logo_link: str = Field(..., example="logo_link")
    back_imgLink: str = Field(..., example="back_imgLink")
    channel: str = Field(..., example="channel")
    country: str = Field(..., example="country")
    gerne: str = Field(..., example="gerne")


class RadioList(BaseModel):

    radio_id: str
    user_id:str
    radio_name:str
    stream_link:str
    logo_link: str
    back_imgLink: str
    channel: str
    country: str
    gerne: str
    
    status: str
    created_at:str
    last_update_at:str

class RadioUpdate(BaseModel):
    
    radio_id: str
    user_id:str
    radio_name:str
    stream_link:str
    logo_link: str
    back_imgLink: str
    channel: str
    country: str
    gerne: str
    
    status: str
    created_at:str
    last_update_at:str
