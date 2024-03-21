from datetime import date, timedelta
from os import getenv

from fastapi import APIRouter
from requests import get
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.models import User

sync_router = APIRouter(prefix='/sync')

engine = create_engine(getenv('DATABASE_URL_SYNC'))
SessionLocal = sessionmaker(bind=engine)


@sync_router.get('/assets/day_summary/{user_id}')
def day_summary(user_id: int):
    today = date.today() - timedelta(days=1)

    with SessionLocal() as session:
        user = session.query(User).filter(User.id==user_id).first()
        symbols = [favorite.symbol for favorite in user.favorites]

    result = []

    for symbol in symbols:
        data = get(f'https://www.mercadobitcoin.net/api/{symbol}/day-summary/{today.year}/{today.month}/{today.day}/').json()
        result.append({
            'date': data['date'],
            'symbol': symbol,
            'opening': data['opening'],
            'closing': data['closing'],
            'lowest': data['lowest'],
            'highest': data['highest'],
            'quantity': data['quantity'],
            'amount': data['amount'],
            'avg_price': data['avg_price']
        })
    return result