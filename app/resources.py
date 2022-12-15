import requests
env_url = "https://api-uat-001.ormuco.com"

#Ports
keystone_port = '5000'
glance_port = '9292'
neutron_port = '9696'
nova_port = '8774'

#Post Request
payload = {
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": "workshop2022@utb.edu.co",
                    "domain": {
                        "name": "Default"
                    },
                    "password": "ILOVECLOUD2022"
                }
            }
        }
    }
}
def generate_token():
    token = requests.post(url=f"{env_url}:{keystone_port}/v3/auth/tokens", json=payload)
    token_id = token.json().get('token').get('id')
    return token_id

def generate_headers():
    token = requests.post(url=f"{env_url}:{keystone_port}/v3/auth/tokens", json=payload)
    token_id = token.json().get('token').get('id')
    return {'X-Auth-Token':token_id}