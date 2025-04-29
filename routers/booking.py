from fastapi import APIRouter
from modules.user import * 
from database import *
from fastapi import HTTPException
from modules.booking import Booking, BookingMade
from datetime import datetime
import random
booking_router = APIRouter()

def map_booking(booking_made: BookingMade) -> Booking:
    return Booking(
        username=booking_made.username,
        time=booking_made.time,
        date=booking_made.date,
        bookingType=booking_made.bookingType,
        reason=booking_made.reason,
        cost=random.randrange(1000, 50000) 
    )

@booking_router.post("/booking")
def make_booking(booking:BookingMade):
    if not check_user(booking.username):
        print("no user found")
        raise HTTPException(status_code=404, detail="user not found")
    
    booking = map_booking(booking)
    user = get_user(booking.username)
    user.booking.append(booking)
    save_user_changes(user)
    return {"message":"booking sucessful"}

@booking_router.get("/getBooking")
def see_bookings(username):
    if not check_user(username):
        raise HTTPException(status_code=404, detail="no user found")
    return get_user(username)

