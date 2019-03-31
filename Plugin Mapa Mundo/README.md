# Geolocalización de IPs maliciosas obtenidas de "Malware Domain List":
![alt text](https://lh5.googleusercontent.com/KG_-un2df4PZqysWg64xA7zUZHz9QmLtxAbWOoD42aDZzRW5h16F2GdGiuFtRE7mBzts-7DyNezg9KEScBaG3N-RdrOew6nug8fMMyaiEQWXTnseg73uE3iYq7umqmum1ZrlUkDW)

#### Explicación del plugin
Esta funcionalidad adicional de Wordpress permite visualizar la distribución geográfica de determinadas direcciones IP que poseen mala reputación, utilizando para ello un repositorio externo denominado “Malware Domain List” y que es accesible a través del siguiente enlace: http://www.malwaredomainlist.com/hostslist/ip.txt. La siguiente imagen representa un extracto de dicha web:

103.14.120.121
103.19.89.55
103.224.212.222
103.24.13.91
103.31.186.207
103.31.186.29
103.4.16.91
103.4.218.22
103.6.196.156
103.8.127.189
103.8.127.205

En primer lugar, se creará un script en Python (por su versatilidad), que se encargará de obtener las direcciones IP del repositorio externo mencionado anteriormente, para que, junto con el empleo de unas bibliotecas (libraries) específicas del propio lenguaje de programación, obtengamos la latitud, longitud y región para que se pueda representar en un mapamundi, y de esta manera, obtengamos una forma más visual y representativa de los datos. En este sentido, analizaremos las primeras 500 direcciones IPs de este fichero por motivos de rendimiento. Además, el programa guardará las direcciones IP leídas en un fichero de texto para futuros estudios; o bien, su lectura para otros posibles scripts sin dependencias de bibliotecas adicionales. La siguiente imagen representa las entradas y las salidas de dicho script:
![alt text](https://lh3.googleusercontent.com/blb3NOQbZvoHcYWxaVmhaIi9mjmfGRi-MvA7HGf3E_-taHL9LqpkjNyNzTbpaOGwq4-ImePQIO2cx-CaNj9oVPvwQrGeHAbBtHcXH5HcpS16g0tf72L8wnnRxwMw9aO1Z_yjbBjs)

Map_attacks.py
Obtenemos y guardamos las direcciones IPs que se encuentran en el repositorio externo. Para ello, eliminamos los saltos de línea y los posibles espacios en blanco que puedan existir:

Obtención de la longitud, latitud y la región de las IPs. Los datos se guardarán en unas listas que se han declarado al inicio del script (latitude, longitude, region y city) 

Creación del mapa e inclusión de puntos (círulos) que representan la geolocalización de los datos obtenidos:

Llegados a este punto, ejecutaremos el programa mediante la secuencia de comandos python3 map_attacks.py. Seguidamente, como resultado del programa se obtendrá un fichero de texto con las IPs que se han leído (malicious_ip.txt) y el mapa con los puntos correspondientes (mymap.html):

A continuación, procederemos a la creación del plugin. Del mismo modo que en el apartado anterior, codificaremos dos ficheros, en este caso, en formato PHP que presentarán el siguiente contenido: 

Por último, la implementación del fichero loadMap.php invocará al mapamundi html generado con el programa anterior:

Se obtendría, de esta manera, los siguientes ficheros en la carpeta htdocs/wp/wp-content/plugins/map:

Seguidamente, comprobaremos el funcionamiento del plugin. Para ello, en la interfaz de administración de nuestro sitio web WordPress haremos click la opción Plugins → Plugins instalados. Observaremos que el nombre que habíamos asignado al plugin en el fichero plugin.php aparece en la vista (desactivado, por defecto):
![alt text](https://lh6.googleusercontent.com/x34kM7XHeV1rZ4-R2AvMud-H40pdcixAteMz3BzS7qAK2yflDdtYBN2lk6PVZQMMq61kMvAeQscLItD3tVLYijw1WwiQE-HrMju30gQeLNpkXXPXxRug9Lwp0UqoHUekxs8lq3SX)

Si se activa, podremos observar que se ha añadido una funcionalidad extra a nuestro sitio web de administración de WordPress:


Finalmente, podremos observar el correcto funcionamiento del plugin:

