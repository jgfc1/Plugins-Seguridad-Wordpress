# Plugins de Seguridad para Wordpress
#### Desarollado por Diego Silveira, Javier Renedo y Javier Gombao.
Los plugins son herramientas que extienden la funcionalidad de WordPress y ofrecen funciones y características personalizadas que permiten al usuario diseñar su sitio web según sus necesidades. En este repositorio se encuentra el código necesario para la creación de dos plugins relacionados con la ciberseguridad. Para ello, se ha pensado en la extracción de datos alojados en repositorios externos que están relacionados con el *[Cyber Threat Intelligence](https://github.com/hslatman/awesome-threat-intelligence)*, que se caracteriza por ser un conjunto de servicios que predicen y notifican amenazas en tiempo real. Concretamente, los datos se extraerán de dos fuentes:

- **[HoneyDB](https://riskdiscovery.com/honeydb/)**: proporciona datos de la actividad de un honeypot desplegado en Internet. Un honeypot es herramienta que se encuentra en una red o sistema informático para ser el objetivo de un posible ataque, y así poder detectarlo y obtener información del mismo y del atacante. Se accederá a la información a través de una API y los datos se visualizarán con un gráfico de barras. [Ver Plugin Gráfica](https://github.com/jgfc1/Plugins-Seguridad-Wordpress/tree/master/Plugin%20Gr%C3%A1fica) 



- **[MalwareDomainList](https://www.malwaredomainlist.com/)**: mantiene una [lista de direcciones IP](http://www.malwaredomainlist.com/hostslist/ip.txt) y dominios que se sabe que se utilizan para propagar malware y spyware. Se descargará un fichero de texto en línea que contenga direcciones IPs maliciosas y se procederá a la visualización de los datos mediante un mapamundi con puntos, donde cada punto representará las coordenadas de la dirección IP obtenida. [Ver Plugin Mapa Mundo](https://github.com/jgfc1/Plugins-Seguridad-Wordpress/tree/master/Plugin%20Mapa%20Mundo)



