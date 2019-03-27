"""
	GEOLOCALIZACION DE UN CONJUNTO DE DIRECCIONES IP PROCEDENTES DE UN FICH DE TEXTO
	Departamento de Informatica. GTT
	Script creado con Pyhton3.6 que obtiene la geolocalizacion de dir. IPs alojadas en el fichero malicious_ip
	Marzo 2019
"""
import sys
import folium
import pandas as pd
from ip2geotools.databases.noncommercial import DbIpCity

#Generamos listas para su posterior impresion en el mapa
ip_list=[]
longitude=[]
latitude=[]
region=[]
city=[]
num=[]

class Map(object):
	
	"""Constructor de la clase Mapa"""
	def __init__(self, fileInput):
		self._fileInput=fileInput
	
	"""Devuelve el nombre del fichero"""
	def getNameFile(self):
		return self._fileInput
	
	""" Golocalizacion (latitud y longitu), asi como la region o la ciudad de la IP """
	def obtainGeolocation(self):
		print("Obteniendo localizacion de las IPs del fichero " + self.getNameFile() + "...")
		try:
			with open(self.getNameFile()) as ips:
				for ip in ips:
					ip_list.append(str(ip.rstrip()))
					response = DbIpCity.get(ip.rstrip(), api_key='free')
					if str(response.latitude) != "None":
						latitude.append(float(response.latitude))
						if str(response.longitude) != "None":
							longitude.append(float(response.longitude))
						if str(response.region) != "None":
							region.append(str(response.region))
						if str(response.city) != "None":
							city.append(str(response.city))
						num.append(int(5))
						
			# Imprime resultados por pantalla
			print(latitude)
			print(longitude)
			print(region)
			print(city)
			
		except Exception:
			print("Error: Fichero " + self.getNameFile() + " no encontrado.")
			sys.exit()

	""" Implementamos un dataFrame con los puntos para mostrarlos en el mapa: """
	def loadData(self):
		data = pd.DataFrame({
		   'lat':latitude,
		   'lon':longitude,
		   'dir_ip':ip_list,
		   'name':region,
		   'value':num
		})
		data
		return data

	"""" Generamos e incluimos los puntos en el mapa """
	def createMap(self):
		# Cargamos lo datos del DataFrame
		data = self.loadData()
		
		# Creamos un mapa vacio
		m = folium.Map(location=[0, 0], tiles="Mapbox Bright", zoom_start=2)

		for i in range(0,len(data)):
		   folium.Circle(
			  location=[float(data.iloc[i]['lat']), float(data.iloc[i]['lon'])],
			  popup=data.iloc[i]['dir_ip'],
			  radius=int(data.iloc[i]['value']*10000),
			  color='crimson',
			  fill=True,
			  fill_color='crimson'
		   ).add_to(m)

		print("Guardando mapa.html")
		m.save('mapa.html')  
		print("Hecho!")
		
""" Creamos un objeto 's' del fichero leido y que obtenga la geolocalizacion y genere el mapa en html"""
s = Map("malicious_ip.txt")
s.obtainGeolocation()
s.createMap()
