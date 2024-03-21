from pydantic import BaseModel
from typing import List


class UserCreateInput(BaseModel):
    name: str


class UserFavoriteAddInput(BaseModel):
    user_id: int
    symbol: str


class StardardOutput(BaseModel):
    message: str


class ErrorOutput(BaseModel):
    detail: str


class Favorite(BaseModel):
    id: int
    symbol: str
    user_id: int

    class Config: 
        orm_mode = True


class UserListOutput(BaseModel):
    id: int
    name: str
    favorites: List[Favorite]

    class Config: 
        orm_mode = True


class DaySummaryOutput(BaseModel):
    date: str
    symbol: str
    opening: float
    closing: float
    lowest: float
    highest: float
    quantity: float
    amount: int
    avg_price: float
