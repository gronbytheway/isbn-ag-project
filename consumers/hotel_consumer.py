import requests

from config import ISBN_HOTELS_MS_API_URL

base_url = ISBN_HOTELS_MS_API_URL

# Create Hotel
def create_hotel(data):

    url = base_url + '/api/hotel'

    response = requests.post(url, json=data)

    return response

# Get Hotels
def get_hotels():

    url = base_url + '/api/hotel'

    headers = {'Content-type': 'application/json'}
    response = requests.get(url, headers=headers)

    # Convert json into dictionary 
    #response_dict = response.json() 

    return response.json() 

# Get Hotel
def get_hotel(id):
    url = base_url + '/api/hotel/' + str(id)
    response = requests.get(url)
    return response.json() 


# Update hotel
def update_hotel(id, data):
    url = base_url + '/api/hotel/' + str(id)
    response = requests.put(url, json=data)
    return response.json() 

# Delete hotel
def delete_hotel(id):
    url = base_url + '/api/hotel/' + str(id)
    response = requests.delete(url)
    return response.json() 