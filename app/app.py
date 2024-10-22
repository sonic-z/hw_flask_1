import datetime

from fastapi import FastAPI
from sqlalchemy import select

import crud
import models
import schema
from constants import STATUS_SUCCESS
from dependencies import SessionDependency
from lifespan import lifespan
from models import Session
from sqlalchemy.sql.operators import ilike_op

app = FastAPI(
    title="Test Application",
    version="0.0.1",
    description="this project is about ...",
    lifespan=lifespan,
)


@app.get("/advertisement/", response_model=schema.SearchAdvResponse)
async def search_adv(query_string: str, session: SessionDependency):
    print(query_string)
    adv_query = select(models.Advertisement).filter(ilike_op(models.Advertisement.title, f"%{query_string}%"))
    ads = await session.scalars(adv_query)
    return {"result": [adv.id_dict for adv in ads]}


@app.get("/advertisement/{advertisement_id}")
async def get_adv(advertisement_id: int, session: SessionDependency):
    adv_item = await crud.get_item(session, models.Advertisement, advertisement_id)
    return adv_item.dict


@app.post("/advertisement/", response_model=schema.CreateAdvResponse)
async def add_adv(adv_json: schema.CreateAdvRequest, session: SessionDependency):
    adv_item = models.Advertisement(**adv_json.dict())
    adv_item = await crud.add_item(session, adv_item)
    return adv_item.id_dict


@app.delete("/advertisement/{advertisement_id}", response_model=schema.DeleteAdvResponse)
async def delete_adv(advertisement_id: int, session: SessionDependency):
    await crud.delete_item(session, models.Advertisement, advertisement_id)
    return STATUS_SUCCESS


@app.patch("/advertisement/{advertisement_id}", response_model=schema.UpdateAdvResponse)
async def update_adv(
    adv_json: schema.UpdateAdvRequest, advertisement_id: int, session: SessionDependency
):
    adv_dict = adv_json.dict(exclude_unset=True)
    adv = await crud.get_item(session, models.Advertisement, advertisement_id)
    for field, value in adv_dict.items():
        setattr(adv, field, value)
    adv.edited_time = datetime.datetime.utcnow()
    adv = await crud.add_item(session, adv)
    return adv.id_dict
