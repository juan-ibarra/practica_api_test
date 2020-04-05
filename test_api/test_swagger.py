import requests


base_url = "https://petstore.swagger.io/v2/"
seccion = "pet/"

peticion = requests.request('GET','{}{}2'.format(base_url, seccion))
print(peticion.text)
print(peticion.status_code)