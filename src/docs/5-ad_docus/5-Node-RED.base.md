<!-- multilingual suffix: en, es -->

<!-- [en] -->

# Programming of communication flows: Node-RED

<!-- [es] -->

# Programación de flujos de comunicación: Node-RED 

<!-- [en] -->

The information provided below is intended to be complementary to the project script and is not required reading.
## Motivation

Node-RED is an open source visual programming tool that allows you to generate communication flows in a very intuitive way. Node-RED is built on top of Node.js, a runtime environment for JavaScript, which allows you to work on it directly in the browser.

Throughout the development of the project you will see how communications with other applications are created and configured in Node-RED, and this experience can be very useful in the future since Node-RED can be installed on a multitude of operating systems and hardware. Some of the possibilities are

- Low cost devices like *Arduino, Raspberry Pi* or *Beagelbone Black*.
- Run locally on local computers and servers (*on-premise*). This allows a distribution of data and event processing capacity across a company's network of devices.
- Execution in the cloud using platforms such as Azure, developed by Microsoft, which will be the one you will use in the course project. This option allows Node-RED to be integrated with the wide spectrum of managed services offered by cloud service providers: *databases, Big-Data, Machine Learning*, etc.

In the following link you can find the official page of Node-RED:

<https://nodered.org/>

## Communication flows or *flows*

In Node-RED, a communication flow or *flow* is a .*JSON* file where one or more data flows have been programmed. These flows are created by dragging the desired nodes from the side palette (highlighted in red in the following screenshot) to the workspace, where they can be connected to each other and configured with parameters and attributes specific to each node.

![](img/5_0.png){: .center}


The possibility of configuring and connecting the nodes is particularly suitable for *Internet-of-Things* (IoT) solutions, where the flexibility of data flows and their scalability are fundamental factors for their adaptation to the constant evolution of technology. .

The simplest method of organizing Node-RED streams is to separate them into multiple tabs within the editor, as there is an option to compile and run all tabs simultaneously.

## *Nodes*

There are many types of nodes, but all of them can be included in one of the following three categories depending on their situation in a data flow:

1. Flow initiator nodes that initiate or trigger process flow execution (e.g. an *Inject* node).
1. Intermediate nodes that perform actions with the information they receive in the data flow and pass the resulting data to the following nodes (e.g. a *function* node).
1. Flow terminal nodes that trigger specific actions when the data flow reaches them (e.g. an *Influx Batch* node).

The basic node palette that Node-RED offers when installed in its lighter version can be extended by installing new packages in the form of community-developed *plugins*.

In addition, it is possible to create new nodes according to the needs of each application. This process is as simple as creating an HTML file with a configuration form available on the official Node-RED page, and a JS (Java Script) file with the node logic written in NodeJS.

You can find all the information regarding the creation of new nodes in the official documentation:

<https://nodered.org/docs/creating-nodes/>

## Compatibility with communication protocols

Node-RED is currently capable of managing data flows through widely used protocols such as:

- Modbus
- TCP/IP
- UDP/IP
- MQTT
- HTTP
- Application APIs such as Twitter, Facebook, etc..

Therefore, any application that uses these protocols is likely to be implemented on Node-RED.

<!-- [es] -->

La información que se aporta a continuación pretende ser complementaria al guion del proyecto y no es de lectura obligatoria.

## Motivación

Node-RED es una herramienta de programación visual de código libre que permite generar flujos de comunicaciones de forma muy intuitiva. Node-RED está desarrollado sobre Node.js, un entorno de ejecución para JavaScript, lo que permite que se pueda trabajar sobre él directamente en el navegador.

A lo largo del desarrollo del proyecto veréis como se crean y configuran en Node-RED las comunicaciones con otras aplicaciones, y esa experiencia os puede resultar muy útil en el futuro ya que Node-RED puede instalarse en multitud de sistemas operativos y hardware. Algunas de las posibilidades son:

- Dispositivos de bajo coste como *Arduino*, *Raspberry Pi* o *Beagelbone Black*.
- Ejecutarse localmente en ordenadores y servidores locales (*on-premise)*. Esto permite una distribución de la capacidad de tratamiento de datos y eventos a través de la red de dispositivos de una empresa.
- Ejecución en la nube (*cloud*) utilizando plataformas como Azure, desarrollada por Microsoft, que será la que usaréis en el proyecto de la asignatura. Esta opción permite integrar Node-RED con el amplio espectro de servicios gestionados que ofrecen los proveedores de servicios *cloud*: bases de datos, *Big-Data*, *Machine Learning*, etc. 

En el siguiente enlace podéis encontrar la página oficial de Node-RED:

<https://nodered.org/>

## Flujos de comunicación o *flows*

En Node-RED, un flujo de comunicaciones o *flow* es un archivo *.JSON* donde se ha programado uno o varios flujos de datos. Estos flujos se crean a partir de arrastrar los nodos que se deseen desde la paleta lateral (destacada en rojo en la siguiente captura) al espacio de trabajo, donde pueden ser conectados entre si y configurados con parámetros y atributos específicos de cada nodo.

![](img/5_0.png){: .center}

La posibilidad de configurar y conectar los nodos es especialmente adecuada para soluciones de *Internet-of-Things* (IoT), donde la flexibilidad de los flujos de datos y la escalabilidad de los mismos son factores fundamentales para su adaptación a la constante evolución de la técnica.

El método más simple para organizar los flujos de Node-RED es separarlos en varias pestañas dentro del editor, ya que existe la opción de compilar y ejecutar todas las pestañas de forma simultánea.

## Nodos o *nodes*

Existen muchos tipos de nodos, pero todos ellos pueden ser incluidos en una de las siguientes tres categorías según su situación en un flujo de datos:

1. Nodos iniciadores de flujo que inician o disparan la ejecución de flujo de proceso (e.g. un nodo *Inject*).
1. Nodos intermedios que realizan acciones con la información que reciben en el flujo de datos y traspasan los datos resultantes a los nodos siguientes (e.g. un nodo *function*).
1. Nodos terminales de flujo que disparan acciones específicas cuando el flujo de datos los alcanza (e.g. un nodo *Influx Batch*).

La paleta de nodos básica que ofrece Node-RED cuando se instala en su versión más ligera puede ser extendida mediante la instalación de nuevos paquetes en forma de *plugins* desarrollados por la comunidad.

Además, es posible crear nuevos nodos según las necesidades de cada aplicación. Este proceso es tan sencillo como crear un fichero HTML con un formulario de configuración disponible en la página oficial de Node-RED, y un fichero JS (Java Script) con la lógica del nodo escrita en NodeJS.

Podéis encontrar toda la información referente a la creación de nuevos nodos en la documentación oficial:

<https://nodered.org/docs/creating-nodes/>

## Compatibilidad con protocolos de comunicaciones

Actualmente Node-RED es capaz de gestionar flujos de datos a través de protocolos tan utilizados como:

- Modbus
- TCP/IP
- UDP/IP
- MQTT
- HTTP
- APIs de aplicaciones como Twitter, Facebook, etc.

Por tanto, cualquier aplicación que utilice dichos protocolos es susceptible a ser implementada sobre Node-RED.