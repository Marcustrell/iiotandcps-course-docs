<!-- multilingual suffix: en, es -->

<!-- [en] -->

# Virtual machines (VMs) and Azure

<!-- [es] -->

# Máquinas virtuales (VM) y Azure

<!-- [en] -->

The information provided below is intended to be complementary to the project script and is not required reading.

## Motivation

The subject project consists of implementing an architecture that combines IIoT and CPS technologies. This technological solution is mounted on a virtual machine, which consists of a virtual computer system (with its own CPU, memory, network interface, storage, etc.) but which is created on a physical hardware system (it can be a computer complete, but can also be part of one if only part of its resources are used.

This technology allows:

- Efficient management of physical resources. It is possible to adjust the costs more than in the case of having to permanently have large equipment and pay for its maintenance.
- Offer portability and flexibility, since the services contracted to the provider can be modified in real time.
- Guarantee a high degree of robustness, considering data redundancies so that information is not lost even in the event of technical problems.

However, it is possible to create virtual machines on a commonly used computer using various software such as VirtualBox or VMWare, which allow you to limit the resources available to the virtual machine.

## Virtualization

Virtualization allows one physical system (hardware) to be shared with many virtual environments, which may be simultaneously running several different operating systems. Each operating system works the same way it would on a regular computer, so the emulated end-user experience inside the virtual machine is nearly identical to the experience of working on a running operating system. on a physical machine.

This technology makes sense because most application and operating system implementations only use a small amount of available physical resources. If you virtualize your servers, you can put many virtual servers on each physical server to improve system hardware usage.

A virtual machine provides an environment that is isolated from the rest of the system, so that anything running inside a virtual machine will not interfere with anything else running on the *host* hardware, which is the physical computer that hosts it.

## Azure

The Azure platform, created by Microsoft, is made up of more than 200 cloud products and services. Azure Virtual Machines are one of several types of scalable, on-demand computing resources offered by Azure.

You can find all the documentation that Azure offers about its virtual machine service at the following link:

<https://docs.microsoft.com/es-es/azure/virtual-machines/>

Specifically, the following link refers to virtual machines with Linux operating system:

<https://docs.microsoft.com/es-es/azure/virtual-machines/linux/overview>

<!-- [es] -->

La información que se aporta a continuación pretende ser complementaria al guion del proyecto y no es de lectura obligatoria.

## Motivación

El proyecto de la asignatura consiste en implementar una arquitectura que combine tecnologías IIoT y CPS. Esta solución tecnológica se monta sobre una máquina virtual, que consiste en un sistema informático virtual (con su propia CPU, memoria, interfaz de red, almacenamiento, etc.) pero el cual se crea en un sistema de hardware físico (puede ser un ordenador completo, pero también puede ser parte de uno si se utilizan solo parte de sus recursos.

Esta tecnología permite:

- Una gestión eficiente de recursos físicos. Es posible ajustar más los costes que en el caso de tener que disponer de forma permanente de grandes equipos y costear su mantenimiento.
- Ofrecer portabilidad y flexibilidad, ya que se puede modificar a tiempo real las prestaciones contratadas al proveedor.
- Garantizar un alto grado de robustez, considerando redundancias de datos para que no se pierda la información incluso en caso de que haya problemas técnicos.

No obstante, es posible generar máquinas virtuales en un ordenador de uso común mediante varios softwares como VirtualBox o VMWare, que permiten limitar los recursos disponibles para la máquina virtual.

## Virtualización

La virtualización permite compartir un sistema físico (hardware) con muchos entornos virtuales, que pueden estar ejecutando simultáneamente varios sistemas operativos diferentes. Cada sistema operativo funciona de la misma manera que lo haría en un ordenador de uso común, de manera que la experiencia del usuario final emulada dentro de la máquina virtual es casi idéntica a la experiencia que se tiene trabajando sobre un sistema operativo que se está ejecutando en una máquina física.

Esta tecnología tiene sentido porque la mayoría de las implementaciones de aplicaciones y sistemas operativos solo utilizan una pequeña cantidad de los recursos físicos disponibles. Si se virtualiza los servidores, es posible colocar muchos servidores virtuales en cada servidor físico para mejorar el uso del sistema de hardware.

Una máquina virtual proporciona un entorno aislado del resto del sistema, de manera que todo lo que se ejecute dentro de una máquina virtual no interferirá con lo demás que se ejecuta en el hardware *host*, que es el equipo físico que lo aloja.

## Azure

La plataforma Azure, creada por Microsoft, está compuesta por más de 200 productos y servicios en la nube. Azure Virtual Machines es uno de los diversos tipos de recursos informáticos a petición y escalables que ofrece Azure.

Podéis encontrar toda la documentación que ofrece Azure acerca de su servicio de máquinas virtuales en el siguiente enlace:

<https://docs.microsoft.com/es-es/azure/virtual-machines/>

Específicamente, el siguiente enlace se refiere a las máquinas virtuales con sistema operativo Linux:

<https://docs.microsoft.com/es-es/azure/virtual-machines/linux/overview>
