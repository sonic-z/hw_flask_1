import datetime

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.ext.asyncio import (AsyncAttrs, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import PG_DSN

engine = create_async_engine(
    PG_DSN,
)

Session = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):

    @property
    def id_dict(self):
        return {"id": self.id}


class Advertisement(Base):

    __tablename__ = "advertisement"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    author: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
    edited_time: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)

    @property
    def dict(self):
        if self.edited_time is not None:
            edited_time = self.edited_time.isoformat()
        else:
            edited_time = None
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "author": self.author,
            "created_at": self.created_at.isoformat(),
            "edited_time": edited_time,
        }


ORM_OBJECT = Advertisement
ORM_CLS = type[Advertisement]
