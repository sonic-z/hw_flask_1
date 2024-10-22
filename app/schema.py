import datetime
from typing import Literal

from pydantic import BaseModel


class BaseItemId(BaseModel):
    id: int


class BaseSearchResult(BaseModel):
    result: list[BaseItemId]


class BaseStatus(BaseModel):
    status: Literal["success"]


class SearchAdvResponse(BaseSearchResult):
    pass


class GetAdvResponse(BaseModel):
    id: int
    title: str
    description: str
    price: int
    author: str
    created_at: datetime.datetime
    edited_time: datetime.datetime | None


class CreateAdvRequest(BaseModel):
    title: str
    description: str
    price: int
    author: str


class CreateAdvResponse(BaseItemId):
    pass


class UpdateAdvRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    price: int | None = None


class UpdateAdvResponse(BaseItemId):
    pass


class DeleteAdvResponse(BaseStatus):
    pass
