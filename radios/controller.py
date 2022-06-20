from fastapi import APIRouter, HTTPException, Depends
from db.table import radios
from radios import model
from utils import util
from configs.connection import database
import uuid, datetime

import  qrcode

from fastapi_pagination import Page, paginate
router = APIRouter()


# All Radios
@router.get("/all_Radios", response_model=Page[model.RadioList])
async def find_allRadio():
    query = radios.select().order_by(radios.c.radio_id.desc())
    res = await database.fetch_all(query)
    return paginate(res)


# Find Radios with names
@router.get("/like_Radio/{names}", response_model=Page[model.RadioList])
async def find_like_Radio(names: str):

    query = "select * from radios where radio_name like '%{}%'".format(names)
    res= await database.fetch_all(query=query, values={})
    return paginate(res)


#counting all Radios
@router.get("/count_Radios")
async def count_all_count(currentUser: model.RadioList = Depends(util.get_current_active_user)):
    query = "SELECT COUNT(radio_id) FROM Radio"
    res= await database.fetch_all(query=query, values={})
    return res


#Find one radios by ID
@router.get("/Radio/{Radio_id}", response_model=model.RadioList)
async def find_Radio_by_id(Radio_id: str, currentUser: model.RadioList = Depends(util.get_current_active_user)):
    query = radios.select().where(radios.c.radio_id == Radio_id)
    return await database.fetch_one(query)



# Find Radios by country
@router.get("/all_Radios_by_district/{country}", response_model=Page[model.RadioList])
async def find_Radios_by_country(country: str, currentUser: model.RadioList = Depends(util.get_current_active_user)):
    query = radios.select().where(radios.c.country == country)
    res = await database.fetch_all(query)
    return paginate(res)



# Find Radios by status
@router.get("/Radio_by_status/{status}", response_model=Page[model.RadioList])
async def find_Radio_by_status(status: str, currentUser: model.RadioList = Depends(util.get_current_active_user)):
    query = radios.select().where(radios.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)



# add new Radio
@router.post("/addRadio")
async def register_Radio(Radios: model.RadioCreate):
    
    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    
    #Adding Radio
    query = radios.insert().values(
        
        radio_id = gid,
        
        user_id=Radios.user_id,
        radio_name=Radios.radio_name,
        stream_link= Radios.stream_link,
        logo_link= Radios.logo_link,
        back_imgLink= Radios.back_imgLink,
        channel=Radios.channel,
        
        country= Radios.country,
        gerne= Radios.gerne,

        created_at = gdate,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(query)

    return{
        "Message":"Radio "+Radios.radio_name+" has been registered",
        "Status":"1"
    }


#Update Radio
@router.put("/Radio_update", response_model=model.RadioList)
async def update_Radio(Radios: model.RadioUpdate, currentUser: model.RadioList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = radios.update().where(radios.c.radio_id == Radios.radio_id).values(
        radio_id = gid,
        
        user_id=Radios.user_id,
        radio_name=Radios.radio_name,
        stream_link= Radios.stream_link,
        logo_link= Radios.logo_link,
        back_imgLink= Radios.back_imgLink,
        channel=Radios.channel,
        
        country= Radios.country,
        gerne= Radios.gerne,

        created_at = gdate,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_Radio_by_id(Radios.id)


#Delete Radio
@router.delete("/Delete_Radio/{Radio_id}", response_model=model.RadioList)
async def Delete_by_radio_id(Radio_id: str, currentUser: model.RadioList = Depends(util.get_current_active_user)):
    query = radios.delete().where(radios.c.radio_id == Radio_id)
    return await database.execute(query)




