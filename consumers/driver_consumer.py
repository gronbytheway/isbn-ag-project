import requests

from config import ISBN_DRIVERS_MS_API_URL

base_url = ISBN_DRIVERS_MS_API_URL

# Create Driver
def create_driver(data):
    url = base_url + '/api/driver'
    response = requests.post(url, json=data)
    return response

# Get Drivers
def get_drivers():
    url = base_url + '/api/driver'
    headers = {'Content-type': 'application/json'}
    response = requests.get(url, headers=headers)
    # Convert json into dictionary 
    response_dict = response.json() 
    return response.json() 

# Get Driver
def get_driver(id):
    url = base_url + '/api/driver/' + str(id)
    response = requests.get(url)
    return response.json() 

# Update Driver
def update_driver(id, data):
    url = base_url + '/api/driver/' + str(id)
    response = requests.put(url, json=data)
    return response.json() 

# Delete Driver
def delete_driver(id):
    url = base_url + '/api/driver/' + str(id)
    response = requests.delete(url)
    return response.json() 