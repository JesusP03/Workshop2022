import requests
from resources import env_url, glance_port, neutron_port, nova_port, keystone_port, generate_headers, payload
from flask import request, render_template


#Generating the json for got the token ID
def generate_json():
    response = requests.post(url=f"{env_url}:{keystone_port}/v3/auth/tokens", json=payload)

    headers = generate_headers()
    json = response.json()
    print(json)
    return json


def crear_instancia():

    #From the form we get all the labels that the user choose

    nombre_seleccionado = request.form.get('nombre')
    imagen_seleccionada = request.form.get('imagenes')
    red_seleccionada = request.form.get('redes')
    flavor_seleccionado = request.form.get('flavors')
    llave_seleccionada = request.form.get('llaves')
    grupo_seleccionado = request.form.get('grupos')

    #Those labels are referenced on the JSON of the instance
    server_to_create ={
    "server": {
        "name": nombre_seleccionado,
        "imageRef": imagen_seleccionada,
        "flavorRef": flavor_seleccionado,
        "networks": [
            {
                "uuid": red_seleccionada
            }
        ],
        "key_name": llave_seleccionada,
        "security_groups": [
            {
                "name": grupo_seleccionado
            }
        ]
    }
    }
    #Creating the instance
    server_on_cloud = requests.post(f'{env_url}:{nova_port}/v2.1/servers', json=server_to_create, headers=generate_headers())
    #Printing in console what happend with the instance
    print(server_on_cloud.reason)
    print(server_on_cloud.text)

    return render_template('created.html')