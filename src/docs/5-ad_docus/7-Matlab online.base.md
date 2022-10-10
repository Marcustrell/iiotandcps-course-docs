<!-- multilingual suffix: en, es -->

<!-- [en] -->

# MATLAB Online, access and connection with InfluxDB

<!-- [es] -->

# MATLAB Online, acceso y conexión con InfluxDB

<!-- [en] -->

The information provided below is intended to be complementary to the project script and is not required reading.

## Motivation

In the second part of the project, a processing of the data measured by the vibration sensor is carried out using MATLAB Online. There is a specific library so that it is possible to bring the data stored in an InfluxDB database to the MATLAB Online environment, as well as to be able to write new data.

## MATLAB Online access

**You do not need to download MATLAB on your computer in order to access the MATLAB Online tool. However, a Mathworks account is required. You can create it by following the instructions found in the following link. If you want to download MATLAB on your computer through the agreement that the UPC has with Mathworks, you will find how to do it at the same link.**

<https://serveistic.upc.edu/ca/distsoft/el-servei/programari-per-a-estudiantsi-professors#section-4>

If you have downloaded and installed it on your computer, you will already have an account created in Mathworks with your address @estudiantat.upc.edu. In this case, to access MATLAB Online you will only have to access <http://matlab.mathworks.com> and log in with the address and password of your Mathworks account.

![](img/7_0.png){: .center}

## InfluxDB connection

The library that you will use so that MATLAB Online can interact with InfluxDB databases is the following:

<https://github.com/EnricSala/influxdb-matlab>

In the practice script you will find templates where you will be told with what data to complete the calls to the functions that are included in this library.

<!-- [es] -->

La información que se aporta a continuación pretende ser complementaria al guion del proyecto y no es de lectura obligatoria.

## Motivación

En la segunda parte del proyecto se lleva a cabo mediante MATLAB Online un procesado de los datos medidos por el sensor de vibración. Existe una librería específica para que sea posible hacer llegar al entorno de MATLAB Online los datos almacenados en una base de datos de InfluxDB, así como poder escribir nuevos datos.

## Acceso a MATLAB Online

**No es necesario descargar MATLAB en vuestro ordenador para poder acceder a la herramienta MATLAB Online. No obstante, es necesario tener una cuenta de Mathworks.** La podéis crear siguiendo las instrucciones que se encuentran en el siguiente enlace. Si deseáis descargar MATLAB en vuestro ordenador mediante el acuerdo que la UPC tiene Mathworks, encontraréis como hacerlo en el mismo enlace.

<https://serveistic.upc.edu/ca/distsoft/el-servei/programari-per-a-estudiantsi-professors#section-4>

En caso que lo hayáis descargado e instalado en vuestro ordenador ya tendréis una cuenta creada en Mathworks con vuestra dirección @estudiantat.upc.edu. En este caso, para acceder a MATLAB Online solo tendréis que acceder a <http://matlab.mathworks.com> y hacer *log in* con la dirección y contraseña de vuestra cuenta de Mathworks.

![](img/7_0.png){: .center}

# Conexión con InfluxDB

La librería que utilizaréis para que MATLAB Online pueda interactuar con bases de datos de InfluxDB es la siguiente:

<https://github.com/EnricSala/influxdb-matlab>

En el guion de la práctica encontraréis plantillas donde se os indicará con que datos completar las llamadas a las funciones que se incluyen en esta librería.