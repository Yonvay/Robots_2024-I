# Laboratorio 4, Cinemática Directa - Phantom X - ROS <!-- omit from toc -->

Robótica 2024-I     

Universidad Nacional de Colombia

**INTEGRANTES**
- Maria Alejandra Peréz Petro
- Yovany Esneider Vargas Gutierrez

**TABLA DE CONTENIDO**
- [1. Configuración del software para el correcto funcionamiento de las herramientas](#1-configuración-del-software-para-el-correcto-funcionamiento-de-las-herramientas)
- [2. Extracción de parámetros de Denavit-Hartenberg Estándar (DHstd)](#2-extracción-de-parámetros-de-denavit-hartenberg-estándar-dhstd)
- [3. Conexión con Python](#3-conexión-con-python)
- [4. Interfaz gráfica](#4-interfaz-gráfica)
- [5. Video de demostración](#5-video-de-demostración)
- [6. Comparación Gráficas Digitales vs Gráficas Reales.](#6-comparación-gráficas-digitales-vs-gráficas-reales)

# 1. Configuración del software para el correcto funcionamiento de las herramientas

Si bien el enfoque de la practica es el uso de herramientas como el toolbox de Peter Corke y ROS, análisis morfológico y control del robot, buena parte del tiempo es invertida en explorar los repositorios de referencia, hasta encontrar la manera en que el sistema reconozca los motores y sea posible su conexión con ROS. Por tanto, a continuación se expone el procedimiento correcto y todos los comandos necesarios.

## Recomendaciones iniciales.

 - No es necesario y llega a ser perjudicial actualizar Python, cabe recordar que ROS es un software de código abierto que no ha tenido soporte por un tiempo. Con la version de Python que trae la version 20.04 LTS de Ubuntu es más que suficiente.

 - No es necesario eliminar los repositorios antes utilizados en la herramienta `Catkin`, no existe evidencia alguna que determine si esto afecta el funcionamiento de la conexión de los motores con ROS.

 - Es totalmente necesario conectar el robot a la fuente de alimentación y el cable de datos a la computadora, en caso contrario ROS y el software de Dynamixel NO detectaran los motores por más comandos de configuración que se ejecuten.

## a. Descarga de Dynamixel

Para ello, con el paquete de instalación ya descargado en Ubuntu <a href= https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_wizard2/>Aquí</a>, se abre una terminal en la carpeta donde se ubica el paquete antes descargado, y se ejecutan en el mismo orden los siguiente comandos.

- Otorgar permisos al paquete en cuestión

```
sudo chmod 775 DynamixelWizard2Setup_x64
```

- Iniciar el programa de instalación y finalizar la instalación

```
./DynamixelWizard2Setup_x64
```

- Dar acceso a los puertos USB

```
sudo usermod -aG dialout UserName
```

*UserName*, corresponde al nombre de cuenta Linux, con la que inicias sesión en Ubuntu

- Reiniciar

```
reboot
```

Una vez terminado el proceso anterior, Ubuntu esta configurado para permitir el paso de información por parte de los motores. Así el software de Dynamixel puede identificar los motores a la hora de ejecutar el Scan encargado de su búsqueda, sin embargo ROS aún no los reconoce.

## b. Instalación y configuración de *dynamixel_one_motor*

Para pasar al desarrollo de esta practica es necesario haber culminado con éxito la practica No. 3, donde se hace uso del paquete turtlesim, por ello, se da por hecho que el usuario tiene a su disposición `ROS` y la herramienta `Catkin`. Entonces, en la carpeta `src` se clona el repositorio *dynamixel_one_motor* para ello, se abre una terminal en la carpeta `src` y se ejecuta el siguiente comando.

```
git clone https://github.com/fegonzalez7/dynamixel_one_motor.git
```

Ahora es necesario otorgar los ID de cada uno de los motores, para ello es necesario editar el archivo `basic.yaml`, ubicado en la carpeta `config`, en la ruta `..\catkin_ws\src\dynamixel_one_motor\config\`. Allí se debe dejar la siguiente configuración, sin olvidar guardar los cambios.

```
joint_1:
  ID: 1
  Return_Delay_Time: 0
  
joint_2:
 ID: 2
 Return_Delay_Time: 1
  
joint_3:
 ID: 3
 Return_Delay_Time: 2
  
joint_4:
 ID: 4
 Return_Delay_Time: 3
  
joint_5:
 ID: 5
 Return_Delay_Time: 4
 ```

 Como se puede observar `Return_Delay_Time`, es la característica encargada del retardo por articulación recomendado en la guía de trabajo. Seguidamente es necesario cargar estos cambios, para ello con una terminal abierta en la carpeta `catkin_ws`, se ejecuta el siguiente comando.

 ```
 catkin build dynamixel_one_motor
 ```

 Con esto la conexión de los motores con ROS está correctamente configurada, para su comprobación se ejecutan 2 comandos, los cuales dan pie a la ejecución y conexión de ROS con los motores. Estos comandos se deben hacer en una terminal en la carpeta `catkin_ws`.

 ```
 source devel/setup.bash
 roslaunch dynamixel_one_motor one_controller.launch
```

Si las recomendaciones y pasos anteriores, fueron correctamente ejecutados el resultado debe ser el siguiente. Ver **Figura 1.**, allí se evidencia como ROS reconoce los 5 motores del robot.

<span><img id="Fig_1" src="Pantallazos/terminal roslaunch running.png" width="600"/>
<label for = "Fig_1" ><br><b>Figura 1.</b> ROS Corriendo correctamente.</label></span>

# 2. Extracción de parámetros de Denavit-Hartenberg Estándar (DHstd)

| $i$ | $\theta_i$ | $d_i$ (cm) | $a_i$ (cm) | $\alpha_i$ (rad)| $offset$ (rad)|
| 1 | $\theta_i$  | 9.7  | 0 | $\pi/2$ | 0 |
| 2 | $\epsilon$| $\zeta$   |

# 3. Conexión con Python

# 4. Interfaz gráfica

# 5. Video de demostración

# 6. Comparación Gráficas Digitales vs Gráficas Reales


# Referencias
[1] Joint controller. https://wiki.ros.org/dynamixel_controllers/Tutorials/CreatingJointPositionController

[2] Paquetes de Dynamixel Workbench. [Repositorio en GitHub]. https://github.com/fegonzalez7/rob_unal_clase3

[3] Paquete del robot Phantom X. [Repositorio en GitHub]. https://github.com/felipeg17/px_robot

[4] Tutorial Phantom X Robot. [Repositorio en GitHub]. https://github.cPhantom X Robotom/fegonzalez7/rob_unal_clase4

Repo de referencia 1
https://github.com/sofiaponteb/Labs-Robotica-2022-2/blob/main/Lab4.md

Repo de referencia 2
https://github.com/aholguinr/Lab4_Robotica_Caipa_Holguin
