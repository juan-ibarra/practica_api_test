import requests
import json


base_url = "https://petstore.swagger.io/v2/"
seccion = "pet/"
url = '{}{}'.format(base_url, seccion)
headers = {'Content-Type': 'application/json', 'accept': 'application/json'}
body = """ {
    "id": 99,
    "category": {
        "id": 1,
        "name": "Ovejero"
    },
    "name": "Karacha",
    "photoUrls": [
        ""
    ],
    "tags": [
    {
      "id": 100,
      "name": "perrito"
    }
  ],
  "status": "available"
} """

respuesta = requests.put(url, headers=headers, data=body)

respuesta_json = json.loads(respuesta.text)
print(json.dumps(respuesta_json, indent=3))