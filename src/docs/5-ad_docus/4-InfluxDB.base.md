<!-- multilingual suffix: en, es -->

<!-- [en] -->

# Temporary database: InfluxDB

<!-- [es] -->

# Base de datos temporal: InfluxDB

<!-- [en] -->

The information provided below is intended to be complementary to the project script and is not required reading.

## Motivation

Data management and storage has become a vitally important aspect in any IIoT&CPS architecture. In the case of your project, the use of a temporary type database is required, which means that it is capable of storing, in addition to the data, at what moment of time each specific data has been written in the database, that can interface with Node-RED, Grafana and Matlab. The selected product is InfluxDB in its version 1.8.

Throughout the entire document we provide you with links to specific directories of the official documentation of InfluxDB in its version 1.8, which is the following:

<https://docs.influxdata.com/influxdb/v1.8/>

## Data structure

Different series of data or *measurements* can be stored in the same InfluxDB database. Taking an example of an Excel file (referred to as a workbook) that represents an InfluxDB database, each sheet in the Excel file would be a data string. Therefore, if you want to store data about an industrial process, you can define a series of data for each physical magnitude you want to record: temperature, pressure, level, etc. Therefore, the data can be organized in different databases (*databases*) and within the same database, in different data series (measurements).

When an InfluxDB database receives a new measurement, it associates said data with a measurement hour (a moment in time), which is called a *timestamp*. By default, the time assigned to the data is the time at which it entered the database, but it is also possible to manually define the *timestamp* we want to store.

The following screenshot is provided to emphasize that when we speak of a new measure or new data we refer to a new entry, which may contain numerical values, words, etc. In it you can also observe the *timestamps* (*time* column) associated with each data entry.

![](img/4_0.png){: .center}

## *Fields* and *tags*

The data that is stored in a particular InfluxDB data string is always made up of one or more *fields*, and optionally one or more *tags*.

The *fields* are the information that you want to store. In the screenshot example above, the *fields* are the number of butterflies (*butterflies*) and bees (*honeybees*) that two scientists have observed.

On the other hand, the tags, which in the previous capture are the location (*location*) and the responsible scientist (*scientist*), provide additional information that allows optimizing the filtering of information in the case of wanting to identify only specific data entries.

You can find specific technical information at the following link:

<https://docs.influxdata.com/influxdb/v1.8/concepts/key_concepts/>

## Data format and syntax

You must be aware of the data types that each element supports (*measurement, timestamp, field, tag*) as well as their syntax.

You can find information at the following link:

<https://docs.influxdata.com/influxdb/v1.8/write_protocols/line_protocol_reference/>

## InfluxDB interaction 

InfluxDB offers a command line interface (CLI) that allows you to browse the data stored in your data series. To do this, it is necessary to communicate with the database in InfluxDB's own *query* language: InfluxQL or *Influx Query Language*.

You have a small demonstration in video format with the procedures related to the development of the project.

You can find more specific technical information that mentions all the commands and functionalities in the following link:

<https://docs.influxdata.com/influxdb/v1.8/query_language/>

## Communication via HTTP

The InfluxDB API (or Application Programming Interface) allows you to communicate with InfluxDB databases using HTTP requests (by default on port 8086). Databases have the ability to issue responses in JSON format.

As an example, in the project guide document you are provided with an HTTP *query* in the form of a URL (at the point that refers to the configuration of the ports of the virtual machine).

You can find technical information on the HTTP requests they support and their format at the following link:

<https://docs.influxdata.com/influxdb/v1.8/tools/api/#query-http-endpoint>

## InfluxDB compatibility

As mentioned above, compatibility between applications is essential to guarantee the proper functioning of the technological solution that is intended to be designed. This section provides the relationship of InfluxDB with the other software used in the development of the project.

### With Node-RED

Within the Node-RED palette you can find several libraries that allow you to work with InfluxDB databases. The library used in the project that you will develop is the following:

<https://flows.nodered.org/node/node-red-contrib-influxdb>

### With Grafana

In the official InfluxDB documentation you can find the procedure to configure an InfluxDB database in Grafana:

<https://docs.influxdata.com/influxdb/v1.8/tools/grafana/>

On the other hand, the official Grafana documentation provides specific information about the plugin that Grafana uses to be compatible with InfluxDB databases:

<https://grafana.com/docs/grafana/latest/datasources/influxdb/>

### With MATLAB

The following library will be used to work with InfluxDB from MATLAB:

<https://github.com/EnricSala/influxdb-matlab>

<!-- [es] -->

La información que se aporta a continuación pretende ser complementaria al guion del proyecto y no es de lectura obligatoria.

## Motivación

La gestión y almacenamiento de los datos se ha convertido en un aspecto de vital importancia en cualquier arquitectura IIoT&CPS. Para el caso de vuestro proyecto se requiere el uso de una base de datos de tipo temporal, que quiere decir que es capaz de almacenar, además de los datos, en que instante de tiempo se ha escrito en la base de datos cada dato concreto, que pueda interactuar con Node-RED, Grafana y Matlab. El producto seleccionado es InfluxDB en su versión 1.8.

A lo largo de todo el documento os proporcionamos enlaces de directorios concretos de la documentación oficial de InfluxDB en su versión 1.8, que es la siguiente:

<https://docs.influxdata.com/influxdb/v1.8/>

## Estructura de datos

En una misma base de datos de InfluxDB se pueden almacenar distintas series de datos o *measurements*. Si se toma como ejemplo un archivo Excel (que recibe el nombre de libro) que representa una base de datos de InfluxDB, cada hoja del archivo de Excel sería una serie de datos. Por tanto, si se desea almacenar datos acerca de un proceso industrial, es posible definir una serie de datos para cada magnitud física que se quiera registrar: temperatura, presión, nivel, etc. Por tanto, los datos se pueden organizar en distintas bases de datos (*databases*) y dentro de una misma base de datos, en diferentes series de datos (*measurements*).

Cuando una base de datos de InfluxDB recibe una nueva medida asocia dichos datos a una hora de medida (un momento en el tiempo), que recibe el nombre de *timestamp*. Por defecto, la hora que se le asigna al dato es la hora a la que este ha entrado en la base de datos, pero también es posible definir manualmente que *timestamp* queremos que se almacene.

Se aporta la siguiente captura para enfatizar que cuando hablamos de una nueva medida o de un nuevo dato nos referimos a una nueva entrada, pudiendo estar contener valores numéricos, palabras, etc. En ella también podéis observar observar los *timestamps* (columna *time*) asociados a cada entrada de datos

![](img/4_0.png){: .center}

## *Fields* y *tags*

Los datos que se almacenan en una serie de datos de InfluxDB concreta se componen siempre de uno o varios *fields*¸ y opcionalmente de uno o varios *tags*.

Los *fields* son la información que se quiere almacenar. En el ejemplo de la captura anterior, los *fields* son el número de mariposas (*butterflies*) y abejas (*honeybees*) que dos científicos han observado.

Por otro lado, los *tags*, que en la captura anterior son la localización (*location*) y el científico responsable (*scientist*), aportan información adicional que permite optimizar el filtrado de información en el caso de querer identificar solo unas entradas de datos concretas.

Podéis encontrar información técnica específica en el siguiente enlace:

<https://docs.influxdata.com/influxdb/v1.8/concepts/key_concepts/>

## Formato de datos y sintaxis

Debéis ser conscientes de los tipos de datos que admite cada elemento (*measurement*, *timestamp*, *field*, *tag*) así como de su sintaxis.

Podéis encontrar información en el siguiente enlace:

<https://docs.influxdata.com/influxdb/v1.8/write_protocols/line_protocol_reference/>

## Interacción con InfluxDB

InfluxDB ofrece una interfaz de línea de comandos (CLI) que permite navegar por los datos almacenados en sus series de datos. Para ello es necesario comunicarse con la base de datos en un lenguaje de peticiones (*querys*) propio de InfluxDB: InfluxQL o *Influx Query Language*. 

Disponéis de una pequeña demostración en formato vídeo con los procedimientos relacionados con el desarrollo del proyecto.

Podéis encontrar información técnica más específica que menciona todos los comandos y funcionalidades en el siguiente enlace:

<https://docs.influxdata.com/influxdb/v1.8/query_language/>

## Comunicación mediante HTTP

La API (o interfaz de programación de aplicaciones) de InfluxDB permite comunicarse con las bases de datos de InfluxDB mediante peticiones HTTP (por defecto en el puerto 8086). Las bases de datos tienen la capacidad de emitir respuestas en formato JSON.

Como ejemplo, en el documento guía del proyecto se os proporciona una *query* HTTP en forma de URL (en el punto que hace referencia a la configuración de los puertos de la máquina virtual).

Podéis encontrar información técnica de las peticiones HTTP que admiten y su formato en el siguiente enlace:

<https://docs.influxdata.com/influxdb/v1.8/tools/api/#query-http-endpoint>

## Compatibilidad de InfluxDB

Como se ha mencionado anteriormente, la compatibilidad entre aplicaciones es fundamental para garantizar el buen funcionamiento de la solución tecnológica que se pretende diseñar. Este apartado aporta la relación de InfluxDB con los otros softwares que se utilizan en el desarrollo del proyecto.

### Con Node-RED

Dentro de la paleta de Node-RED se pueden encontrar varias librerías que permiten trabajar con bases de datos de InfluxDB. La librería utilizada en el proyecto que desarrollaréis es la siguiente:

<https://flows.nodered.org/node/node-red-contrib-influxdb>

##3 Con Grafana

En la documentación oficial de InfluxDB podéis encontrar el procedimiento para configurar, en Grafana, una base de datos de InfluxDB:

<https://docs.influxdata.com/influxdb/v1.8/tools/grafana/>

Por otro lado, en la documentación oficial de Grafana se ofrece información específica del plugin que Grafana emplea para ser compatible con bases de datos de InfluxDB:

<https://grafana.com/docs/grafana/latest/datasources/influxdb/>

### Con MATLAB

Se utilizará la siguiente librería para trabajar con InfluxDB desde MATLAB:

<https://github.com/EnricSala/influxdb-matlab>
