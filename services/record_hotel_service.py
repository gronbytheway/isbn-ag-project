from consumers.hotel_consumer import *

class RecordHotelService:  
    
    # CREATE HOTEL
    @staticmethod
    def create_hotel_record_service(data):

        driver_data = {
            "nit": data['nit'],
            "razonSocial": data['razonSocial'],
            "direccion": data['direccion'],
            "telefono": data['telefono']
            }

        user = create_hotel(driver_data)

        return True
    
    @staticmethod
    def get_hotels_record_service():     
        hotels = get_hotels()
        return hotels
    
    @staticmethod
    def get_hotel_record_service(id):     
        hotel = get_hotel(id)
        return hotel
    
    @staticmethod
    def update_hotel_record_service(id, data):
        driver_data = {
            "nit": data['nit'],
            "razonSocial": data['razonSocial'],
            "direccion": data['direccion'],
            "telefono": data['telefono']
            }
        drivers = update_hotel(id, driver_data)

        return drivers
    
    @staticmethod
    def delete_hotel_record_service(id):     
        hotel = delete_hotel(id)
        return hotel