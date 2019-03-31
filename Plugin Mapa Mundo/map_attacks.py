import folium
import pandas as pd
from urllib.request import urlopen
from ip2geotools.databases.noncommercial import DbIpCity

#Generamos listas para la longitud y la latitud:
longitude=[]
latitude=[]
region=[]
city=[]
num=[]

# Generamos el mapa y se guarda como página html mymap.htm
m = folium.Map(location=[0, 0], tiles="Mapbox Bright", zoom_start=2)

#Obtenemos las direcciones IP provenientes de un repositorio de cyber threat intelligence
textpage = str(urlopen("http://www.malwaredomainlist.com/hostslist/ip.txt").read(), 'utf-8')
textpage = textpage.replace("\r","")

#Guardamos las IPs en nuestro fichero local
file = open("malicious_ip.txt", "w")
file.write(textpage)

#Eliminamos los saltos en blanco
ips = textpage.split("\n")

cont = 0;
num_max=500
print("Loading map with the first " + num_max + " ips")
for ip in ips:
    #print(ips)
    if (cont <=num_max):
        #print(ip)
        response = DbIpCity.get(ip, api_key='free')
        #print("Latitud: " + str(response.latitude))
        if str(response.latitude) != "None":
            latitude.append(float(response.latitude))
            #print("Longitud: " + str(response.longitude))
            if str(response.longitude) != "None":
                longitude.append(float(response.longitude))
            #print(response.country)
            if str(response.region) != "None":
                region.append(str(response.region))
            if str(response.city) != "None":
                city.append(str(response.city))
            num.append(int(5))
            cont = cont + 1;

#print(latitude)
#print(longitude)
#print(region)
#print(city)
#print(cont)

# Implementamos el dataFrame con los puntos para mostrarlos en el mapa:
data = pd.DataFrame({
   'lat':latitude,
   'lon':longitude,
   'name':region,
   'value':num
})
data

for i in range(0,len(data)):
   folium.Circle(
      location=[float(data.iloc[i]['lat']), float(data.iloc[i]['lon'])],
      popup=data.iloc[i]['name'],
      radius=int(data.iloc[i]['value']*10000),
      color='crimson',
      fill=True,
      fill_color='crimson'
   ).add_to(m)

print("Saving map...")
m.save('mymap.html')  
print("Done" ")
