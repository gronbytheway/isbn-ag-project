from consumers.booking_consumer import *
from consumers.bookingForDate_consumer import *

class RecordService:
    
    @staticmethod
    def create_booking_service(data):
        booking = create_booking(data)
        if booking.status_code == 201:
            return True
        return False
    
    @staticmethod
    def create_booking_for_date_service(data):
        booking = search_booking(data)
        if booking.status_code == 200:
            return booking
        else: 
            return False