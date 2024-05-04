from flask import Blueprint, request, jsonify
from services.record_driver_service import RecordDriverService
from services.record_hotel_service import RecordHotelService
from services.record_service import RecordService

record_api = Blueprint('record_api', __name__)

# Create Driver
@record_api.route('/api/record/driver', methods=['POST'])
def create_record_controller():
    data = request.get_json()
    response = RecordDriverService.create_driver_record_service(data)
    if response == True:
        return jsonify("Driver Record has been successfully created."), 201
    return jsonify("Error"), 400

# Get Drivers
@record_api.route('/api/record/driver', methods=['GET'])
def get_record_drivers_controller():
    response = RecordDriverService.get_drivers_record_service()
    return jsonify(response), 200

# Get Driver
@record_api.route('/api/record/driver/<id>', methods=['GET'])
def get_record_driver_controller(id):
    response = RecordDriverService.get_driver_record_service(id)
    return jsonify(response), 200

# Update Driver
@record_api.route('/api/record/driver/<id>', methods=['PUT'])
def update_record_driver_controller(id):
    data = request.get_json()
    response = RecordDriverService.update_driver_record_service(id, data)
    return jsonify(response), 200

# Delete Driver
@record_api.route('/api/record/driver/<id>', methods=['DELETE'])
def delete_record_driver_controller(id):
    response = RecordDriverService.delete_driver_record_service(id)
    return jsonify(response), 200

########################################################################################
########################################################################################
# Create Hotel
@record_api.route('/api/record/hotel', methods=['POST'])
def create_record_hotel_controller():
    data = request.get_json()
    response = RecordHotelService.create_hotel_record_service(data)
    if response == True:
        return jsonify("Hotel Record has been successfully created."), 201
    return jsonify("Error"), 400

# Get Hotels
@record_api.route('/api/record/hotel', methods=['GET'])
def get_record_hotels_controller():
    response = RecordHotelService.get_hotels_record_service()
    return jsonify(response), 200

# Get Hotel
@record_api.route('/api/record/hotel/<id>', methods=['GET'])
def get_record_hotel_controller(id):
    response = RecordHotelService.get_hotel_record_service(id)
    return jsonify(response), 200

# Update Hotel
@record_api.route('/api/record/hotel/<id>', methods=['PUT'])
def update_record_hotel_controller(id):
    data = request.get_json()
    response = RecordHotelService.update_hotel_record_service(id, data)
    return jsonify(response), 200

# Delete Hotel
@record_api.route('/api/record/hotel/<id>', methods=['DELETE'])
def delete_record_hotel_controller(id):
    response = RecordHotelService.delete_hotel_record_service(id)
    return jsonify(response), 200

#####################################################################
#####################################################################

@record_api.route('/api/record/booking', methods=['POST'])
def create_booking_controller():

    data = request.get_json()

    response = RecordService.create_booking_service(data)

    if response == True:
        return jsonify("Reserva creada con exito."), 201

    return jsonify("Error al crear la reserva"), 400

@record_api.route('/api/record/bookingfordate', methods=['POST'])
def create_booking_for_date_controller():

    data = request.get_json()

    response = RecordService.create_booking_for_date_service(data)

    response2 = response.json()

    if response == False:
        return jsonify("Error al buscar las reservas"), 400

    return response2