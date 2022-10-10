<!-- multilingual suffix: en, es -->

<!-- [en] -->

# Dashboard in real time: Grafana

<!-- [es] -->

# Dashboard en tiempo real: Grafana 

<!-- [en] -->

The information provided below is intended to be complementary to the project script and is not required reading.

## Motivation

The possibility of visualizing the data acquired and/or processed in real time makes it easier to interpret said data and make decisions. In the case of your project, Grafana will be used to visualize in dynamic graphic panels of different types the data that you write in the Influx database, with which it is fully compatible. Also, you will run it in a Docker container.

Grafana is a tool to visualize time series data programmed in open source code written in *Go* and Node.JS LTS language (very similar to Node.JS, the engine on which Node-RED works) also equipped with a complete HTTP API that facilitates its integration.

Grafana has been designed to present the data to be monitored in a pleasant and easy-to-use way, which has allowed it to progressively replace SCADA systems for industrial monitoring.

You can find the complete technical documentation of Grafana at the following link:

<https://grafana.com/>

## Grafana access

Grafana can be accessed through any browser, as it has a web interface that listens on port 3000.

![](img/6_0.png){: .center}

## Kiosko mode

One of the most useful features of Grafana is the ability to display *dashboards* on a large monitor or television. This allows us to display different control panels that we have saved in something similar to a playlist, being able to divide the data into two parts and display both sequentially, automatically and periodically.

An example would be the two configurations shown below:

![](img/6_1.png){: .center}

![](img/6_2.png){: .center}

<!-- [es] -->

La información que se aporta a continuación pretende ser complementaria al guion del proyecto y no es de lectura obligatoria.

## Motivación

La posibilidad de visualizar los datos adquiridos y/procesados en tiempo real hace facilita la interpretación de dichos datos y la toma de decisiones. Para el caso de vuestro proyecto se utilizará Grafana para visualizar en paneles gráficos dinámicos de distintos tipos los datos que vayáis escribiendo en la base de datos de Influx, con la que es totalmente compatible. Además, lo ejecutaréis en un contenedor de Docker.

Grafana es una herramienta para visualizar datos de series temporales programada en código abierto escrito y en lenguaje *Go* y Node.JS LTS (muy semejante a Node.JS, el motor sobre el que funciona Node-RED) dotado además de una HTTP API completa que facilita su integración.

Grafana ha sido diseñado para presentar los datos a monitorizar de una manera agradable y simple de utilizar, hecho que ha permitido que progresivamente vaya sustituyendo los sistemas SCADA para monitorización industrial.

Podéis encontrar la documentación técnica completa de Grafana en el siguiente enlace:

<https://grafana.com/>

## Acceso a Grafana

Es posible acceder a Grafana mediante cualquier navegador, ya que dispone de una interfaz web que escucha en el puerto 3000.

![](img/6_0.png){: .center}


# Modo kiosko
Una de las funcionalidades más útiles de Grafana es la capacidad de mostrar *dasbhoards* en un monitor grande o televisor. Ello permite mostrar diferentes paneles de control que hayamos guardado en algo semejante a una lista de reproducción, pudiendo dividir los datos en dos partes e ir mostrando ambas de manera secuencial, automática y periódica.

Un ejemplo serían las dos configuraciones que se muestran a continuación:

![](img/6_1.png){: .center}

![](img/6_2.png){: .center}
