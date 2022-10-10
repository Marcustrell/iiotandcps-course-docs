<!-- multilingual suffix: en, es -->

<!-- [en] -->

# Docker y Docker Compose

<!-- [es] -->

# Docker y Docker Compose

<!-- [en] -->

The information provided below is intended to be complementary to the project script and is not required reading.

## Motivation

Instead of installing the programs directly in the virtual machine that you will create, you will have to deploy them in isolated software containers (*containers*). These containers are units of software that package code so that applications work in isolation without the need to use multiple virtual machines.

## Docker

Docker is an open source project for automating the deployment of applications as self-contained, portable containers that can be run in the cloud or on-premises. Docker is also a company (Docker Inc.) that promotes and promotes this technology.

Docker technology uses the Linux kernel (the common base shared by Ubuntu, Debian, Mint, etc.) to segregate processes so they can run independently in containers, in order to make better use of available hardware. and retain the security that a solution where processes run on separate physical systems would offer.

The container tools offer a deployment model based on images, which are static representations of an application or service and its configuration and dependencies. To run the application or service, an instance of the application image is created to create a container, which in our case will run on the virtual machine. Docker Hub is a public registry where any developer can upload an image containing the software they have built. By default, Docker looks for the image that is indicated in this registry. In the case of a specific application, it is common to find an image for each commercial version of the application. This allows containers to run specific software versions regardless of the hardware being used, and even multiple versions of the same program to run simultaneously without compatibility errors.

The *tags* are labels that allow different instances that have been created from the same image to be differentiated. These images are generated locally using the *build* command from a DockerFile file, which allows you to define a series of instructions that will be executed at the moment of creating an image.

In the screenshot that appears on the next page, which corresponds to the *docker-compose* file that is provided to you to generate the containers that you will need in the project, it is indicated that the image that is going to be used is a Node-RED image that we have identified with the *tag* “1.3.0”.

You can find all the information regarding Docker (terminology and technical aspects) in the following links. The first link leads to the Microsoft Docker documentation while the second link leads to the official Docker documentation.

<https://docs.microsoft.com/es-es/dotnet/architecture/containerized-lifecycle/>

<https://docs.docker.com/>

## Docker Compose

Docker Compose is a tool to define and run multi-container solutions, which uses YAML files to configure the different applications (one for each container) and carries out the process of creating and starting the containers with just one command (*docker-compose up*). The YAML file that is written for each solution is also called docker-compose.

The following figure, which is a cutout of the *docker-compose* file that you will use in the project, shows how a specific service is defined, in this case Node-RED:

- In *image* it is indicated which image will be used from Node-RED. In this case it is not an image taken from the official Node-RED repository; It is an image generated based on the image of version 1.8.4-alpine of Node-RED on which the packages you will need have been installed.
- In *environment*, in this case, only the time zone is indicated.
- In *ports*, the correspondence between ports is indicated (the first being that of the virtual machine and the second being that of the container).
- In *networks*, it is indicated which IP address this container will take in the internal network that will form all the containers generated through this *docker-compose* file.
- In *volumes* it is indicated where the generated data should be stored once the container is turned off. If that was not done, the data would be lost since the containers are generated each time as a new instance of an image.

![](img/3_0.png){: .center}

You can find all the documentation regarding Docker Compose at the following link:

<https://docs.docker.com/compose/>

<!-- [es] -->

La información que se aporta a continuación pretende ser complementaria al guion del proyecto y no es de lectura obligatoria.

## Motivación

En lugar de instalar los programas directamente en la máquina virtual que crearéis, los deberéis implementar en contenedores de software aislados (*containers*). Estos contenedores son unidades de software que empaquetan código para que las aplicaciones funcionen de forma aislada sin la necesidad de emplear múltiples máquinas virtuales.

## Docker

Docker es un proyecto de código abierto para automatizar la implementación de aplicaciones como contenedores portátiles y autosuficientes que se pueden ejecutar en la nube o localmente. Docker es también una empresa (Docker Inc.) que promueve e impulsa esta tecnología.

La tecnología Docker usa el kernel de Linux (la base común que comparten Ubuntu, Debian, Mint, etc.) para segregar los procesos, de modo que puedan ejecutarse de manera independiente en contenedores, con el objetivo de hacer un mejor uso del hardware disponible y conservar la seguridad que ofrecería una solución donde los procesos se ejecutan en sistemas físicos separados.

Las herramientas del contenedor ofrecen un modelo de implementación basado en imágenes, que son representaciones estáticas de una aplicación o servicio y de su configuración y dependencias. Para ejecutar la aplicación o el servicio, se crea una instancia de la imagen de la aplicación para crear un contenedor, que en vuestro caso se ejecutará en la máquina virtual. Docker Hub es un registro público donde cualquier desarrollador puede colgar una imagen que contenga el software que ha generado. Por defecto, Docker busca la imagen que se le indica en este registro. En el caso de una aplicación concreta, es común encontrar una imagen por cada versión comercial de la aplicación. Ello permite que los contenedores ejecuten versiones de software concretas sin importar el hardware que está siendo utilizado, e incluso que varias versiones del mismo programa se ejecuten simultáneamente sin que ocurran errores de compatibilidad.

Los *tags* son etiquetas que permiten diferenciar distintas instancias que se hayan creado a partir de una misma imagen. Estas imágenes se generan localmente mediante el comando *build* a partir de un archivo DockerFile, que permite definir una serie de instrucciones que se ejecutarán en el momento de la creación de una imagen. 

En la captura que se presenta en la página siguiente, que corresponde al archivo *docker-compose* que se os proporciona para generar los containers que necesitaréis en el proyecto, se indica que la imagen que se va a utilizar es una imagen de Node-RED que hemos identificado con el *tag* “1.3.0”.

Podéis encontrar toda la información referente a Docker (terminología y aspectos técnicos) en los siguientes enlaces. El primer enlace conduce a la documentación de Microsoft sobre Docker mientras que el segundo conduce a la documentación oficial de Docker.

<https://docs.microsoft.com/es-es/dotnet/architecture/containerized-lifecycle/>

<https://docs.docker.com/>

## Docker Compose

Docker Compose es una herramienta para definir y ejecutar soluciones multi-contenedor, que utiliza archivos YAML para configurar las distintas aplicaciones (una para cada contenedor) y lleva a cabo el proceso de creación y arranque de los contenedores con solo un comando (*docker-compose up*). El archivo YAML que se escribe para cada solución también recibe el nombre de *docker-compose*.

La siguiente figura, que es un recorte del archivo *docker-compose* que utilizaréis en el proyecto, permite observar cómo se define un servicio concreto, en este caso Node-RED:

- En *image* se indica que imagen se va a utilizar de Node-RED. En este caso no es una imagen tomada del repositorio oficial de Node-RED; se trata de una imagen generada tomando como base la imagen de la versión 1.8.4-alpine de Node-RED sobre la que se han instalado los paquetes que necesitaréis.
- En *environment*, en este caso, se indica solo la zona horaria.
- En *ports* se indica la correspondencia entre puertos (el primero siendo el de la máquina virtual y el segundo siendo el del contenedor).
- En *networks* se indica que dirección IP tomará este contenedor en la red interna que formarán todos los contenedores generados mediante este archivo *docker-compose*.
- En *volumes* se indica donde se deberá almacenar los datos generados una vez el contenedor se apague. Si eso no se hiciera, los datos se perderían ya que los contenedores se generan cada vez como una nueva instancia de una imagen.

![](img/3_0.png){: .center}

Podéis encontrar toda la documentación referente a Docker Compose en el siguiente enlace:

<https://docs.docker.com/compose/>
