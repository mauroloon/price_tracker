from typing import Annotated

from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Query
from sqlmodel import Field
from sqlmodel import Session
from sqlmodel import SQLModel
from sqlmodel import create_engine
from sqlmodel import select

class Item(SQLModel, table=True):
    id: int = Field(defauilt=None, primary_key=True)
    name: str
    description: str = None