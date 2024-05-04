import requests

from config import RT_BOOKING_FOR_DATE_MS_API_URL

base_url = RT_BOOKING_FOR_DATE_MS_API_URL

# Create Task
def search_booking(data):

    url = base_url

    response = requests.post(url, json=data)

    return response