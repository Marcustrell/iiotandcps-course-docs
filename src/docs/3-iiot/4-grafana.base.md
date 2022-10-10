<!-- multilingual suffix: en, es -->

<!-- [en] -->

# Data visualization in Grafana

<!-- [es] -->

# Visualización de datos en Grafana

<!-- [en] -->

With the containers raised, you can access the container containing Grafana through your browser using the following URL:

[*http://”public\_IP\_of\_yourVM”:3000*]()

To log in you will use the following credentials that are indicated in the “docker-compose.yml” file, which are the following:

**User: admin**

**Password: supersecretpassword**

Now you must configure the database from which you want Grafana to read data. To do this, you must access the configuration menu and access the Data Sources section.

![](./img/1.45.png){: .center}

Click Add Data Source and select InfluxDB as the database type.

![](./img/1.46.png){: .center}

You must give a name to this Data Source (it does not have to be the same as the InfluxDB database) and indicate the URL address of the InfluxDB container.

![](./img/1.47.png){: .center}

In the *Database* field you must enter the name of your database. Make sure that the *HTTP Method* and *Min time* Interval fields remain as in the screenshot.

![](./img/1.48.png){: .center}

You can validate that Grafana has detected the database by clicking the *Save & Test* button. A successful result should return the following message:

![](./img/1.49.png){: .center}

To view the data written in the InfluxDB database, you must create a Grafana *Dashboard*:

![](./img/1.50.png){: .center}

Click on *Add new panel* and a panel will open that will be updated with the information you add in the *Query* tab. Now you must modify the highlighted fields in the screenshot with the name of the InfluxDB measurement series where you have written the data and the variable that contains the numerical values of the measurements.

![](./img/1.51.png){: .center}

Once you have done it, in the graphic panel at the top you will be able to visualize the synthetic data that you have generated in Node-RED. You can select a period of time on which to zoom in to better see the data. **With this you will have fulfilled the objective set for this first part of the project, good job!**

Click Apply in the top right corner of the screen to save the panel changes you've generated. Once done, at the top of the *dashboard* you also have an option to save the changes to the *dashboard*.


![](./img/1.52.png){: .center}

> **You must provide a screenshot of the Grafana dashboard where you can clearly see the data that is written in the InfluxDB database.** Configure the dashboard so that you can clearly see the behavior of the data.

<!-- [es] -->


Con los contenedores levantados, podréis acceder mediante vuestro navegador al contenedor que contiene Grafana utilizando la siguiente URL:

[*http://”IPpublicaDeVuestraVM”:3000*]()

Para iniciar sesión utilizaréis las siguientes credenciales que se indican en el archivo “docker-compose.yml”, que son las siguientes:

**User: admin**

**Password: supersecretpassword**

Ahora deberéis configurar la base de datos que de la que queréis que Grafana haga la lectura de datos. Para ello, deberéis acceder al menú de configuración y acceder al apartado de *Data Sources*.

![](./img/1.45.png){: .center}

Haced clic en *Add Data Source* y seleccionad como tipo de base de datos *InfluxDB*.

![](./img/1.46.png){: .center}

Deberéis dar un nombre a esta Fuente de datos (no tiene porque ser el mismo que el de la base de datos de InfluxDB) e indicar la dirección URL del container de InfluxDB.

![](./img/1.47.png){: .center}

En el campo *Database* deberéis introducir el nombre de vuestra base de datos. Aseguraos que los campos *HTTP Method* y *Min time Interval* quedan como en la captura.

![](./img/1.48.png){: .center}

Podéis validar que Grafana ha detectado la base de datos haciendo clic en el botón *Save & Test*. Un resultado satisfactorio debería devolver el siguiente mensaje:

![](./img/1.49.png){: .center}

Para visualizar los datos escritos en la base de datos de InfluxDB, deberéis crear un *Dashboard* de Grafana:

![](./img/1.50.png){: .center}

Haced clic en *Add new panel* y se os abrirá un panel que se va a ir actualizando con la información que añadáis en la pestaña *Query*. Ahora deberéis modificar los campos destacados en la captura con el nombre de la serie de medidas de InfluxDB donde habéis escrito los datos y la variable que contiene los valores numéricos de las medidas.

![](./img/1.51.png){: .center}

Una vez lo hayáis hecho, en el panel gráfico de la parte superior podréis visualizar los datos sintéticos que habéis generado en Node-RED. Podéis seleccionar un período de tiempo sobre el que hacer *zoom* para ver mejor los datos. **Con esto habréis cumplido el objetivo fijado para esta primera parte del proyecto, ¡buen trabajo!**

Haced clic en *Apply* en la esquina superior derecha de la pantalla para guardar los cambios en el panel que habéis generado. Una vez hecho, en la parte superior del *dashboard* tenéis también una opción para guardar los cambios en el *dashboard*.

> **Debéis aportar una captura del dashboard de Grafana donde se puedan ver claramente los datos que están escritos en la base de datos de InfluxDB.** Configurad el dashboard de forma que se pueda apreciar claramente el comportamiento de los datos.
