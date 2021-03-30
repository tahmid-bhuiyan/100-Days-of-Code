import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'

USERNAME = 'plzdontake'
TOKEN = 'J2K34J23532Kkdfgjd1j4j34'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"

graph_config = {
    'id': 'graph1',
    'name': 'Productivity',
    'unit': 'min',
    'type': 'float',
    'color': 'ichou'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pxl_endpoint = f'{graph_endpoint}/{graph_config["id"]}'

date = datetime(year=2021, month=3, day=28).strftime('%Y%m%d')

pixel_params = {
    'date': date,
    'quantity': '72'
}

# response = requests.post(url=pxl_endpoint, json=pixel_params, headers=headers)
# print(response.text)

update_pxl = f"{pxl_endpoint}/{date}"

update_params = {
    'quantity': '180'
}

# response = requests.put(url=update_pxl, json=update_params, headers=headers)
# print(response.text)

response = requests.delete(url=update_pxl, headers=headers)
print(response.text)
