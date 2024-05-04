import requests

from config import RT_BOOKING_MS_API_URL

base_url = RT_BOOKING_MS_API_URL

# Create User
def create_booking(data):

    url = base_url + '/api/user'

    response = requests.post(url, json=data)

    return response
