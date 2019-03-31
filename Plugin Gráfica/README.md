# Plugin que nos indica la actividad de un HoneyPot:
![alt text](https://lh5.googleusercontent.com/zTGvq5ZHcfAVmh4ryTWa7Bz17NCkAOvE0G7RkOIPgc3WIudNS2iqdmQ94EPnsyJTO8D6IJQn-F3HhRv_eycd43VxofaMPlfMiqhscSJMpdF85n7r-67803QI0f3kUkYEsUaA5fdQ)

### Explicación del plugin
Este plugin se basa en la información recopilada por la base de datos [HoneyDB](https://riskdiscovery.com/honeydb/), la cual recopila información sobre las direcciones IP que se conectan a sus honeypots, el número de veces que se conecta cada IP y la fecha de última conexión.

![alt text](https://lh4.googleusercontent.com/MQg8T0OAzXYAd6hzXiRrJ7Y_TVsCFbIE-mJCsw7r546dxvlGk74rJ6ShcnbS4XQ4nF76yZbdPy5m_V1b-DmQlqVaxWsXFWl2kgem8Z5iaU_CYa8Vffzbr6ADRO9Wwn7z-Qnx-psm)

A partir de esta información, vamos a crear un plugin que nos muestre una gráfica con las 10 direcciones IP que más veces se han conectado a una de las honeypots de HoneyDB y con el número de conexiones de cada una.

### Componentes
En primer lugar, creamos la carpeta que contendrá el plugin en la ruta **C:/xampp/htdocs/wordpress/wp-content/plugins.** A continuación, creamos el archivo **plugin.php**, el cual contendrá la declaración del plugin.

![alt_text](https://github.com/jgfc1/Plugins-Seguridad-Wordpress/blob/master/img/1.png)

Este plugin añadirá una entrada en el menú del administrador. La función **add_to_menu** indica el título que aparecerá en la página, el nombre de la entrada en el menú del administrador, las capacidades que tiene que tener el usuario para poder ver la entrada en el menú, el nombre de la URL, el icono que se mostrará en la entrada del menú del administrador y la posición en la que aparecerá la entrada.

A continuación, vamos a crear el archivo **grafica.php**, el cual se encargará de obtener los datos de la API de HoneyDB y de generar la gráfica a partir de estos datos.

Para obtener los datos, lo primero que tenemos que hacer es identificarnos en la web de HoneyDB y pedir una API ID y una API Key. En concreto, las nuestras serán las siguientes:

![alt_text](https://github.com/jgfc1/Plugins-Seguridad-Wordpress/blob/master/img/2.png)

A continuación, empleamos cURL para conectarnos a la API de HoneyDB y obtener los datos en formato JSON.

![alt_text](https://github.com/jgfc1/Plugins-Seguridad-Wordpress/blob/master/img/3.png)

Una vez que hemos obtenido los datos, tomamos los primeros 10 resultados en formato JSON, los cuales serán los más frecuentes. Cada uno de estos resultados tendrá el siguiente formato:

![alt_text](https://github.com/jgfc1/Plugins-Seguridad-Wordpress/blob/master/img/4.png)

Una vez extraídos los datos que nos interesan, procedemos a generar nuestra gráfica. Para ello, emplearemos la librería CanvasJS.

La gráfica con los datos extraídos la generamos de la siguiente manera:

![alt_text](https://github.com/jgfc1/Plugins-Seguridad-Wordpress/blob/master/img/5.png)

Finalmente, accedemos a la opción **Plugins > Plugins instalados** del menú del administrador y activamos el plugin **Gráfica de IPs maliciosas**. 

![alt_text](https://github.com/jgfc1/Plugins-Seguridad-Wordpress/blob/master/img/6.png)

Tras activar el plugin, podremos observar que se ha añadido una nueva funcionalidad a nuestro menú de administrador de WordPress:

![alt_text](https://github.com/jgfc1/Plugins-Seguridad-Wordpress/blob/master/img/7.png)

### Verificación del funcionamiento del plugin:
![alt text](https://lh5.googleusercontent.com/zTGvq5ZHcfAVmh4ryTWa7Bz17NCkAOvE0G7RkOIPgc3WIudNS2iqdmQ94EPnsyJTO8D6IJQn-F3HhRv_eycd43VxofaMPlfMiqhscSJMpdF85n7r-67803QI0f3kUkYEsUaA5fdQ)
