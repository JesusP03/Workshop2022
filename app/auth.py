import requests
from resources import env_url, glance_port, neutron_port, nova_port, generate_headers
#from flask import render_template

#Requesting all the attributes for create de instance
def networks():
    return requests.get(url=f"{env_url}:{neutron_port}/v2.0/networks", headers=generate_headers()).json().get('networks')

def flavors():
    return requests.get(url=f"{env_url}:{nova_port}/v2.1/flavors", headers=generate_headers()).json().get('flavors')

def keys():
    keypairs = requests.get(url=f"{env_url}:{nova_port}/v2.1/os-keypairs", headers=generate_headers()).json().get('keypairs')
    keypairs = [k.get('keypair') for k in keypairs]
    return keypairs

def images():
    return requests.get(url=f"{env_url}:{glance_port}/v2/images", headers=generate_headers()).json().get('images')

def security():
    sec = requests.get(url=f"{env_url}:{nova_port}/v2.1/os-security-groups", headers=generate_headers()).json().get('security_groups')
    return sec


