from pydantic import BaseModel
from datetime import datetime


class BookingMade(BaseModel):
    username:str
    time:str
    date:str
    bookingType:str
    reason:str


class Booking(BookingMade):
    consultant:str = "Mr jeff"
    cost: float    
