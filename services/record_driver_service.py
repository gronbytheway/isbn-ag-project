from consumers.driver_consumer import *

class RecordDriverService:

    # CREATE DRIVER
    @staticmethod
    def create_driver_record_service(data):

        driver_data = {
            "documento": data['documento'],
            "nombre": data['nombre'],
            "email": data['email'],
            "tipoVehiculo": data['tipoVehiculo'],
            "telefono": data['telefono'],
            "Placa": data['Placa']
            }
        user = create_driver(driver_data)
        return True
    
    @staticmethod
    def get_drivers_record_service():     
        drivers = get_drivers()
        return drivers
    
    @staticmethod
    def get_driver_record_service(id):       
        drivers = get_driver(id)
        return drivers

    @staticmethod
    def update_driver_record_service(id, data):
        driver_data = {
            "documento": data['documento'],
            "nombre": data['nombre'],
            "email": data['email'],
            "tipoVehiculo": data['tipoVehiculo'],
            "telefono": data['telefono'],
            "Placa": data['Placa']
            }
        drivers = update_driver(id, driver_data)

        return drivers
    
    @staticmethod
    def delete_driver_record_service(id):     
        driver = delete_driver(id)
        return driver
    