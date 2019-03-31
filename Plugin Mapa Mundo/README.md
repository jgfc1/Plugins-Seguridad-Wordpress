# Geolocalización de IPs maliciosas obtenidas de "Malware Domain List":
![alt text](https://lh5.googleusercontent.com/KG_-un2df4PZqysWg64xA7zUZHz9QmLtxAbWOoD42aDZzRW5h16F2GdGiuFtRE7mBzts-7DyNezg9KEScBaG3N-RdrOew6nug8fMMyaiEQWXTnseg73uE3iYq7umqmum1ZrlUkDW)

## Explicación del plugin:
Esta funcionalidad adicional de Wordpress permite visualizar la distribución geográfica de determinadas direcciones IP que poseen mala reputación, utilizando para ello un repositorio externo denominado “Malware Domain List” y que es accesible a través del siguiente enlace: http://www.malwaredomainlist.com/hostslist/ip.txt.

### Componentes:
Se creará un script en Python (por su versatilidad), que se encargará de obtener las direcciones IP del repositorio externo mencionado anteriormente, para que, junto con el empleo de unas bibliotecas (libraries) específicas del propio lenguaje de programación, obtengamos la latitud, longitud y región para que se pueda representar en un mapamundi, y de esta manera, obtengamos una forma más visual y representativa de los datos. En este sentido, analizaremos las primeras 500 direcciones IPs de este fichero por motivos de rendimiento. Además, el programa guardará las direcciones IP leídas en un fichero de texto para futuros estudios; o bien, su lectura para otros posibles scripts sin dependencias de bibliotecas adicionales:

![alt text](https://lh3.googleusercontent.com/blb3NOQbZvoHcYWxaVmhaIi9mjmfGRi-MvA7HGf3E_-taHL9LqpkjNyNzTbpaOGwq4-ImePQIO2cx-CaNj9oVPvwQrGeHAbBtHcXH5HcpS16g0tf72L8wnnRxwMw9aO1Z_yjbBjs)

##### Compilación (Instalación de Python y dependencias):
> apt install python3

> apt install python3-pip

> pip3 install folium

> pip3 install urlib

> pip3 install pandas

> pip3 install ipgeo2tools


##### Ejecución:
> python3 map_attacks.py

##### Output:
> mymap.html

> malicious_ip.txt

### Creación plugin en Wordpress:
A continuación, procederemos a la creación del plugin codificando el script plugin.php. Por último, crearemos el fichero loadMap.php que invocará a  mapa.html generado con el script map_attacks.py. Seguidamente, comprobaremos el funcionamiento del plugin. Para ello, los ficheros han de estar en una carpeta dentro del directorio [nombre_sitio_WordPress]/wp-content/plugins. 

A continuación, en la interfaz de administración de nuestro sitio web WordPress haremos click la opción Plugins → Plugins instalados. Observaremos que el nombre que habíamos asignado al plugin en el fichero plugin.php aparece en la vista (desactivado, por defecto):
![alt text](https://lh6.googleusercontent.com/x34kM7XHeV1rZ4-R2AvMud-H40pdcixAteMz3BzS7qAK2yflDdtYBN2lk6PVZQMMq61kMvAeQscLItD3tVLYijw1WwiQE-HrMju30gQeLNpkXXPXxRug9Lwp0UqoHUekxs8lq3SX)

Si se activa, podremos observar que se ha añadido una funcionalidad extra a nuestro sitio web de administración de WordPress:
![alt text](https://lh6.googleusercontent.com/9D9UW0ZzBcp3IpLKoc4ABQLGayuK67X-hjZEZnyBm2B57ZaAUPnGNqoV3JK8oqTBoEt6wVLfatmAWvvl7KLP037o7c-qJsi0JORTXL8sZJSDt0TRgsBrlETu4qTFgbrFN7p1fflU)

### Verificación del funcionamiento del plugin:
![alt text](https://lh5.googleusercontent.com/KG_-un2df4PZqysWg64xA7zUZHz9QmLtxAbWOoD42aDZzRW5h16F2GdGiuFtRE7mBzts-7DyNezg9KEScBaG3N-RdrOew6nug8fMMyaiEQWXTnseg73uE3iYq7umqmum1ZrlUkDW)
