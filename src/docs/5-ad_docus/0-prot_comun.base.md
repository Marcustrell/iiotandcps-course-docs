<!-- multilingual suffix: en, es -->

<!-- [en] -->

# Communications protocols

The information provided below is intended to be complementary to the project script and is not required reading.

## Motivation

A communications protocol consists of rules to which the sender of a message and its receiver must comply in order to communicate. In practice, in each layer of the OSI model level, specific rules are established (which may refer to aspects such as information packaging, the format of the data frame, its length or how error control is managed) and A protocol is defined for each layer.

The following figure shows a communications scheme between two devices (Host A and Host B) and the correspondence of protocols for each layer. The notations to the right (APDU, PPDU, SPDU, etc.) indicate what name the communication units in each layer receive.

![](img/0_1.png){: .center}

In any application in which a communication flow between equipment and applications is necessary, one or more communication protocols are used. It is necessary to know the most important characteristics of these protocols to identify the parameters that must be provided to them (IP addresses, memory map addresses, read/write codes).

In the second part of the project, which consists of implementing the CPS architecture, you will work directly with the Modbus protocol when reading data from a PLC. On the other hand, you will notice that some of the software that is going to be used accepts encrypted requests according to the HTTP protocol.

Next, we present some communication protocols of the application layer that are used in the field of industrial automation:

- Modbus.
- *Hypertext Trasnfer Protocol* o HTTP.
- *Message Queuing Telemetry Transport* o MQTT.

As an example, in an application over the protocols TCP for the transport layer, IP for the network layer, and Ethernet for the network interface layer, the layers are distributed as follows:

![](img/0_2.png){: .center}

## Modbus

Modbus is an industrial communications protocol, created by MODICON in 1979 and open, developed to make possible the transmission of information between its PLCs. Modbus is an application protocol, which means that it can be implemented on different physical layers (with their respective protocols). There are versions of the protocol for serial port and Ethernet (Modbus TCP/IP), and other protocols that are derived from TCP/IP. In industrial automation, the use of the Modbus TCP/IP model is very common.

Modbus networks use a master-slave (or client-server) architecture. The master initiates communications (e.g. a SCADA) through a function code that requests data from a slave (e.g. a PLC), which returns a response based on the code it has received. The port reserved for the Modbus protocol is port 502.

### Modbus data model

Modbus originally supports two data types: a Boolean value and a 16-bit unsigned integer. In many cases sensors and other devices generate data in different types (e.g. floating point values). It is common for slave devices to convert these larger data types to registers. As an example, a pressure sensor can divide a 32-bit floating point value between two 16-bit registers.

In SCADA systems, it is common for embedded devices to have certain values defined as inputs (e.g. gains or PID parameters), while other values are outputs (e.g. the position of a valve). Modbus data values are divided into four ranges:

|**Memory block**|**Type of data**|**Teacher acces**|**Slave acces**|
| :-: | :-: | :-: | :-: |
|**Coils**|Boolean|Reading/Writing|Reading/Writing|
|**Discrete inputs**|Boolean|Only reading|Reading/Writing|
|**Holding register**|16-bits unsigned word|Reading/Writing|Reading/Writing|
|**Input register**|16-bits unsigned word|Only reading|Reading/Writing|

### Modbus function codes

Function codes determine how the master accesses and modifies data. When a slave is asked to perform a function code, it uses the function parameters it has received from the master to perform specific actions.

The most common function codes are named after the range of data they modify or access. Here are some examples:

|**Code**|**Function**|
| :-: | :-: |
|Decimal|Hexadecimal||
|02|0x02|Reading Holding Registers|
|06|0x06|Write to a specific register|
|16|0x10|Write to multiple registers|

The following link leads to the official website of the developers of the Modbus protocol:

<https://modbus.org/>

In the following link you can find the technical specifications of the Modbus protocol, which offer detailed information about:

- The data format recognized by Modbus.
- The addresses used by Modbus.
- The function code categories.
- The descriptions of each function code.
- The exceptions generated by Modbus.

<https://www.modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf>

Node-RED Compatibility

Within the Node-RED palette you can find several libraries that allow you to send and receive communications in Modbus format. The library used in the project that you will develop is the following:

<https://flows.nodered.org/node/node-red-contrib-modbus>

## HTTP

The characteristic that defines the HTTP protocol is its ability to transmit information in hypertext format, which allows other resources such as videos, graphics, audio, etc. to be included in the encoded information. The links that can form part of a message in hypertext format They are called hyperlinks.

As is the case with Modbus, HTTP is based on a client-server architecture. The client issues HTTP requests and the server returns an HTTP response with a response code, which may be accompanied by additional information if the request requires it. As an example, a web browser can act as a client and an application running on a server that hosts a web page can act as a server.

The format of HTTP requests and responses is very similar and is predefined. Knowing the type of requests that a server expects to receive and the responses it generates allows, from the point of view of a client:

- Generate requests that conform to the request format that the server you want to work with can receive.
- Adapt the client application so that it is capable of receiving the HTTP responses that the server will return.

HTTP requests and responses are encoded as a string in ASCII format, which allows the data to be sent as a frame encoded in hexadecimal format. Next, you can see an example of an HTTP response and its equivalence as a hexadecimal data frame:

![](img/0_3.png){: .center}

At Atenea you can access two videos that we have generated specifically to present the HTTP protocol:

- The video **Video1\_HTTP.mp4** covers the most important features of the HTTP protocol, as well as the formats of HTTP requests and responses.
- The video **Video2\_HTTP.mp4** presents practical examples of communications through the HTTP protocol implemented on the Node-RED tool. In this second video, the concepts presented in the first video are considered known.

## MQTT

MQTT is a protocol that is based on publish-subscribe relationships and, thanks to this, it greatly eases communications between devices, since information is only sent when specific events occur and therefore the necessary resources in terms of bandwidth are much lower. This information is encapsulated in the form of objects called messages. The publish-subsrcribe relationships are defined when a hierarchical tree of topics is defined, in which some devices (referred to as nodes) can subscribe or publish. On the other hand, all communications are managed by a central node (referred to as a broker).

This operating mode allows you to isolate the applications that publish in a topic from those that are subscribed to it. Some implications of this are as follows:

- Applications do not need to share any parameters with each other or be aware of each other's existence.
- The apps do not need to be in sync.
- It is not necessary for the applications to be connected at the same time. It is possible for an application to publish a message, in a specific topic, with a parameter that tells the central node to retain it, so that subscribed applications receive it when they are connected.

All of this greatly facilitates the scalability of the system since the topics hierarchy can be modified at any time and new publisher/subscriber nodes can be declared.

The following link leads to the official website of the developers of the MQTT protocol, where you can find all the technical information:

<https://mqtt.org/>

Specifically, in the following link you can find the technical specifications of the protocol:

<https://mqtt.org/mqtt-specification/>

- At Atenea you can access two videos that we have generated specifically to present the MQTT protocol:
- The video **Video1\_MQTT.mp4** introduces the MQTT protocol and develops a very simple theoretical example with the aim of giving context to the most important theoretical concepts: nodes, topics, etc.
- The video **Video2\_MQTT.mp4** implements the theoretical example presented in the first video on the Node-RED tool.

<!-- [es] -->

# Protocolos de comunicaciones

La información que se aporta a continuación pretende ser complementaria al guion del proyecto y no es de lectura obligatoria.

## Motivación

Un protocolo de comunicaciones consiste en unas reglas a las que deben ajustarse el emisor de un mensaje y su receptor para poder comunicarse. A la práctica, en cada capa del nivel del modelo OSI se establecen unas reglas concretas (que pueden referirse a aspectos como el empaquetado de la información, el formato de la trama de datos, su longitud o como se gestiona el control de errores) y queda definido un protocolo para cada capa.

La figura siguiente muestra un esquema de comunicaciones entre dos equipos (*Host A* y *Host B*) y la correspondencia de protocolos para cada capa. Las anotaciones a la derecha (APDU, PPDU, SPDU, etc.) indican que nombre reciben las unidades de comunicación en cada capa.

![](img/0_1.png){: .center}

En cualquier aplicación en la que sea necesario un flujo de comunicaciones entre equipos y aplicaciones se utilizan uno o varios protocolos de comunicaciones. Es necesario conocer las características más importantes de dichos protocolos para identificar los parámetros que se les debe proporcionar (direcciones IP, direcciones de mapas de memoria, códigos de lectura/escritura).

En la segunda parte del proyecto, la que consiste en implementar la arquitectura CPS, trabajaréis directamente con el protocolo Modbus a la hora de realizar la lectura de datos de un PLC. Por otro lado, observaréis que alguno de los softwares que se va a utilizar admiten peticiones codificadas según el protocolo HTTP.

A continuación, os presentamos algunos protocolos comunicaciones de la capa de aplicación que se utilizan en el ámbito de la automatización industrial:

- Modbus.
- *Hypertext Trasnfer Protocol* o HTTP.
- *Message Queuing Telemetry Transport* o MQTT.

Como ejemplo, en una aplicación sobre los protocolos TCP para la capa de transporte, IP para la capa de red y Ethernet para la capa de interfaz de red, las capas se distribuyen de la siguiente forma:

![](img/0_2.png){: .center}

## Modbus

Modbus es un protocolo de comunicaciones industriales, creado por MODICON en 1979 y abierto, desarrollado para hacer posible la transmisión de información entre sus PLCs. Modbus es un protocolo de aplicación, lo que significa que puede implementarse sobre diferentes capas físicas (con sus respectivos protocolos). Existen versiones del protocolo para puerto serie y Ethernet (Modbus TCP/IP), y otros protocolos que derivan de TCP/IP. En automatización industrial es muy común el uso del modelo Modbus TCP/IP.

Las redes Modbus utilizan una arquitectura maestro-esclavo (o cliente-servidor). El maestro inicia las comunicaciones (e.g. un SCADA) mediante un código de función que solicita datos a un esclavo (e.g. un PLC), que devuelve una respuesta en función del código que ha recibido. El puerto reservado para el protocolo Modbus es el puerto 502.

### Modelo de datos de Modbus

Originalmente, Modbus soporta dos tipos de datos: un valor booleano y un entero sin signo de 16 bits. En muchos casos los sensores y otros dispositivos generan datos en tipos diferentes (e.g. valores con punto flotante). Es común para los dispositivos esclavos convertir estos tipos de datos más grandes a registros. Como ejemplo, un sensor de presión puede dividir un valor de punto flotante de 32 bits entre dos registros de 16 bits.

En los sistemas SCADA, es común para los dispositivos embebidos tener ciertos valores definidos como entradas (e.g. ganancias o parámetros PID), mientras que otros valores son salidas (e.g. la posición de una válvula). Los valores de datos de Modbus son divididos en cuatro rangos:

|**Bloque de memoria**|**Tipo de datos**|**Acceso de maestro**|**Acceso de esclavo**|
| :-: | :-: | :-: | :-: |
|**Bobinas**|Booleano|Lectura/Escritura|Lectura/Escritura|
|**Entradas discretas**|Booleano|Solo lectura|Lectura/Escritura|
|**Registros de retención**|Palabra de 16 bits sin signo|Lectura/Escritura|Lectura/Escritura|
|**Registros de entrada**|Palabra de 16 bits sin signo|Solo lectura|Lectura/Escritura|

### Códigos de función de Modbus

Los códigos de función determinan cómo el maestro tiene acceso y modifica los datos. Cuando a un esclavo se le pide realizar un código de función, utiliza los parámetros de la función que ha recibido del maestro para ejecutar unas acciones concretas.

Los códigos de función más comunes llevan el nombre del rango de datos que modifican o al que tienen acceso. A continuación, se muestran algunos ejemplos:

|**Código**|**Función**|
| :-: | :-: |
|Decimal|Hexadecimal||
|02|0x02|Lectura de registros de retención|
|06|0x06|Escritura en un registro concreto|
|16|0x10|Escritura en múltiplos registros|

El siguiente enlace conduce a la página web oficial de los desarrolladores del protocolo Modbus:

<https://modbus.org/>

En el siguiente enlace podéis encontrar las especificaciones técnicas del protocolo Modbus, que ofrecen información detallada acerca de:

- El formato de datos reconocidos por Modbus.
- Las direcciones empleadas por Modbus.
- Las categorías de códigos de función.
- Las descripciones de cada código de función.
- Las excepciones generadas por Modbus.

<https://www.modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf>

### Compatibilidad con Node-RED

Dentro de la paleta de Node-RED se pueden encontrar varias librerías que permiten emitir y recibir comunicaciones en formato Modbus. La librería utilizada en el proyecto que desarrollaréis es la siguiente:

<https://flows.nodered.org/node/node-red-contrib-modbus>

## HTTP

La característica que define el protocolo HTTP es su capacidad de transmitir información con el formato hipertexto, lo que permite que en la información codificada se puedan incluir otros recursos como vídeos, gráficos, audios… Los enlaces que pueden formar parte de un mensaje en formato hipertexto reciben el nombre de hipervínculos.

Como es el caso con Modbus, HTTP se basa en una arquitectura cliente-servidor. El cliente emite peticiones HTTP y el servidor devuelve una respuesta HTTP con un código de respuesta, que puede venir acompañado de información adicional si la petición lo requiere. Como ejemplo, un navegador web puede ejercer como cliente y una aplicación que se ejecuta en un servidor que aloja una página web puede ejercer como servidor.

El formato que tienen las peticiones y las respuestas HTTP es muy similar y está predefinido. Conocer el tipo de peticiones que espera recibir un servidor y las respuestas que genera permite, des del punto de vista de un cliente:

- Generar peticiones que se ajusten al formato de peticiones que puede recibir el servidor con el que se quiere trabajar.
- Adaptar la aplicación cliente para que sea capaz de recibir las respuestas HTTP que devolverá el servidor.

Las peticiones y respuestas HTTP se codifican como una *string* en formato ASCII, lo que permite que los datos se envíen en forma de trama codificada en formato hexadecimal. A continuación, podéis ver un ejemplo de respuesta HTTP y su equivalencia como una trama de datos hexadecimal:

![](img/0_3.png){: .center}

En Atenea podéis acceder a dos vídeos que hemos generado específicamente para presentar el protocolo HTTP:

- El vídeo **Video1\_HTTP.mp4** trata las características más importantes del protocolo HTTP, así como los formatos de las peticiones y respuestas HTTP.
- El vídeo **Video2\_HTTP.mp4** presenta ejemplos prácticos de comunicaciones mediante el protocolo HTTP implementados sobre la herramienta Node-RED. En este segundo vídeo se dan por conocidos los conceptos presentados en el primer vídeo.

## MQTT

MQTT es un protocolo que está basado en relaciones *publish-subscribe* y gracias a ello aligera enormemente las comunicaciones entre dispositivos, ya que solo se envía información cuando suceden eventos concretos y por tanto los recursos necesarios en cuanto a anchos de banda son mucho menores. Esta información se encapsula en forma de objetos que reciben el nombre de *messages*. Las relaciones *publish-subsrcribe* quedan definidas cuando se defina un árbol jerárquico de *topics*, en los que algunos dispositivos (que reciben el nombre de nodos) pueden subscribirse o publicar. Por otro lado, todas las comunicaciones son gestionadas por un nodo central (que recibe el nombre de *broker*).

Este modo de funcionamiento permite aislar las aplicaciones que publican en un *topic* de las que están subscritas al mismo. Algunas implicaciones de ello son las siguientes:

- Las aplicaciones no necesitan compartir ningún parámetro entre ellas ni tener constancia de la existencia de las otras.
- No es necesario que las aplicaciones se encuentren sincronizadas.
- No es necesario que las aplicaciones estén conectadas a la vez. Es posible que una aplicación publique un *message,* en un *topic* concreto, con un parámetro que indica al nodo central que lo retenga, para que lo reciban las aplicaciones subscritas cuando estén conectadas.

Todo ello facilita enormemente la escalabilidad del sistema ya que en cualquier momento se puede modificar la jerarquía de *topics* y declarar nuevos nodos publicadores/subscriptores.

El siguiente enlace conduce a la página web oficial de los desarrolladores del protocolo MQTT, donde podéis encontrar toda la información técnica:

<https://mqtt.org/>

Concretamente, en el siguiente enlace podéis encontrar las especificaciones técnicas del protocolo:

<https://mqtt.org/mqtt-specification/>

En Atenea podéis acceder a dos vídeos que hemos generado específicamente para presentar el protocolo MQTT:

- El vídeo **Video1\_MQTT.mp4** introduce el protocolo MQTT y desarrolla un ejemplo teórico muy simple con el objetivo de dar contexto a los conceptos teóricos más importantes: nodos, *topics*, etc.
- El vídeo **Video2\_MQTT.mp4** implementa sobre la herramienta Node-RED el ejemplo teórico presentado en el primer vídeo. 