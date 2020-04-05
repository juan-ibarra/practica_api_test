import requests
import datetime


base_url = "https://api.nasa.gov/planetary/apod?api_key="
api_key = "gOjGGSe4LegmYHFKdk7NMApDlOPG8nyYOaP9N9RM"

formato_fecha = '%Y-%m-%d'
dia_anterior = datetime.date.today() - datetime.timedelta(days=1)

dia = dia_anterior.strftime(formato_fecha)
fecha = str(datetime.date.today().strftime(formato_fecha))
hd = 'False'
url = '{}{}&date={}&hd={}'.format(base_url, api_key, dia, hd)

peticion = requests.request('GET', url)
print(peticion.text)