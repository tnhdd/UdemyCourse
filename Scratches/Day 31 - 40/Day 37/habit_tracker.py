import requests
from datetime import datetime

user_name = "batet"
token = "ngongan1"
pixela_endpoint = "https://pixe.la/v1/users"
graph_id = "graph1"
today = datetime.now()

user_params = {
    "token": token,
    "username": user_name,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
graph_endpoint = f"{pixela_endpoint}/{user_name}/graphs"

graph_config = {
    "id": graph_id,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": token
}

# requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{user_name}/graphs/{graph_id}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5",
}
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
