# Laboratorio 3, Intro a ROS <!-- omit from toc -->

Robótica 2024-I

Universidad Nacional de Colombia

**INTEGRANTES**
- Maria Alejandra Peréz Petro
- Yovany Esneider Vargas Gutierrez

**TABLA DE CONTENIDO**
- [1. Conexión Matlab con ROS](#1-conexión-matlab-con-ros)
- [2. Conexión de ROS con python](#2-conexión-de-ros-con-python)
  - [Objetivo](#objetivo)
  - [Procedimiento](#procedimiento)
  - [Explicación de myTeleopKey.py](#explicación-de-myteleopkeypy)
  - [Resultados](#resultados)
  - [Análisis](#análisis)
- [Conclusiones](#conclusiones)

# 1. Conexión Matlab con ROS

Se inician 2 instancias de terminal, en la primera se llama al nodo maestro con el comando `roscore`.

<span><img id="Fig_1" src="Imágenes/Comando 1.png" width="400"/>
<label for = "Fig_1" ><br><b>Figura 1.</b>  Llamada de nodo maestro.</label></span>

En la segunda el comando `rosrun turtlesim turtlesim node`, este inicializa el programa de la tortuga.

<span><img id="Fig_2" src="Imágenes/Comando 2.png" width="600"/>
<label for = "Fig_2" ><br><b>Figura 2.</b>  Ejecución tortuga.</label></span>

Script en MatLab, este se conecta con ROS y permite asignar valores a la posición de la tortuga.
```
rosinit;

velPub = rospublisher('/turtle1/cmd_vel','geometry_msgs/Twist');
velMsg = rosmessage(velPub)

velMsg.Linear.X = 2 
velMsg.Linear.Y = 3
send(velPub,velMsg)
pause(1)
```
Donde la primera sección inicia el nodo maestro, seguidamente se inicializan las variables, se modifican sus atributos y se envía para su posterior visualización ver **Figura 3**.

<span><img id="Fig_3" src="Imágenes/Matlab 1.png" width="600"/>
<label for = "Fig_3" ><br><b>Figura 3.</b> Conexión MatLab con ROS.</label></span>

Para la obtención del ultimo mensaje se deja la obtención del mensaje sin punto y coma de manera que imprima en consola y se visualice la información.

```
rosmessage(posPub); % -----> rosmessage(posPub)
```
Se observa para la primera conexión en la **Figura 4** y para la ultima en la **Figura 5**.

<span><img id="Fig_4" src="Imágenes/Matlab 2.png" width="600"/>
<label for = "Fig_4" ><br><b>Figura 4.</b> Obtención del ultimo mensaje, primera conexión.</label></span>

<span><img id="Fig_5" src="Imágenes/Matlab 3.png" width="600"/>
<label for = "Fig_5" ><br><b>Figura 5.</b> Obtención del ultimo mensaje, ultima conexión.</label></span>

Con el paso anterior se obtienen todos los atributos que tiene el objeto tortuga, por tanto el ultimo script que permite enviar todos los valores asociados a la pose de la tortuga, debe tener lineas de código donde se cambie cada uno de estos atributos, y finalmente se envíen para su ejecución.

Los atributos de la tortuga son, posición en **_X_** y **_Y_**, angulo de inclinación en radianes, velocidad linear y angular.
Finalmente se detiene la conexión con el nodo maestro con el comando `rosshutdown`.

<span><img id="Fig_6" src="Imágenes/Matlab 4.png" width="600"/>
<label for = "Fig_6" ><br><b>Figura 6.</b> Desconexión del nodo maestro.</label></span>


# 2. Conexión de ROS con python

## Objetivo
Escribir un script de python que permita operar una tortuga del paquete turtlesim con el teclado, de forma que:
- Se mueva hacia adelante y hacia atrás con las teclas W y S
- Gire en sentido horario y antihorario con las teclas D y A.
- Retorne a su posición y orientación centrales con la tecla R.
- De un giro de 180° con la tecla ESPACIO.

## Procedimiento

1. Se crea un directorio (carpeta) llamado `catkin_ws`, el cual servirá como espacio de trabajo para el proyecto ROS. Luego, se crea la carpeta `src` y se compila todo el código dentro del espacio de trabajo con el comando `catkin build`.

```
cd ~
mkdir catkin_ws
cd catkin_ws
mkdir src
catkin build
```

2. Se clona el repositorio hello_turtle dentro de la carpeta src del espacio de trabajo creado, permitiendo la descarga del paquete turtlesim para su integración en el proyecto.

```
cd catkin_ws/src
git clone https://github.com/felipeg17/hello_turtle.git
```

3. En la carpeta `catkin_ws/src/hello_turtle/scrpits`, se agrega el script de Python creado [myTeleopKey.py](./src/hello_turtle/scripts/myTeleopKey.py).

4. incluir el script en el apartado catkin_install_python del archivo `CMakeLists.txt` que se encuentra en el directorio `catkin_ws/src/hello_turtle/`. Dicho apartado lucirá así cuando el script ya sea añadido:
   
```
catkin_install_python(PROGRAMS
  scripts/turtlePos.py
  scripts/turtleSpawn.py
  scripts/turtleSub.py
  scripts/turtleVel.py
  scripts/myTeleopKey.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

5. Lanzar una terminal, dirigirse al directorio del workspace de catkin y escribir el comando
`catkin build` para hacer build en el paquete modificado.

6. Con Linux operando lanzar 3 terminales.      
   - En la primera terminal, escribir el comando roscore para iniciar el nodo maestro.
   ```
   roscore
   ```

   - En la segunda terminal ejecutar
    ```
    rosrun turtlesim turtlesim_node
    ```

   - En la tercera terminal, dirigirse al directorio que contiene el workspace de catkin y ejecutar los comonados indicados. En este punto, la terminal ya deberı́a estar esperando el ingreso de teclas.
    ```
    cd ~/catkin_ws/
    source devel/setup.bash
    rosrun hello_turtle myTeleopKey.py
    ```

## Explicación de myTeleopKey.py

Primero se importan las librerías a manejar.Entre las más importantes esta rospy para la integración de ROS con python, Twist para el envío de comandos a turtlesim, termios, sys y os para el manejo del teclado y Teleport Absolute para el comando de teletransporte.

```Python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute
import termios, sys, os
from numpy import pi
```

`get_key()`: esta función decteta la techa preeionada por el usuario. Utiliza la biblioteca termios para cambiar la configuración del terminal para que pueda leer un solo carácter sin que el usuario tenga que presionar Enter. Ver [link](http://python4fun.blogspot.com/2008/06/get-key-press-in-python.html.)

```Python
TERMIOS = termios

def get_key():  
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd,TERMIOS.TCSANOW,new)
    c = None
    try:
        key = os.read(fd,1)
    finally:
        termios.tcsetattr(fd,TERMIOS.TCSAFLUSH,old)
    return key
```

`handle_key(key, vel_msg, vel_pub)`: esta función toma como argumentos la pulsación de una tecla, un mensaje de Twist y un editor. Comprueba qué tecla se presionó y modifica el mensaje Twist en consecuencia, luego publica el mensaje.

``` Python
def handle_key(key, vel_msg, vel_pub):
    if key.lower() == KEY_FORWARD:
        vel_msg.linear.x = 1
        vel_msg.angular.z = 0

    elif key.lower() == KEY_LEFT:
        vel_msg.angular.z = pi/4
        vel_msg.linear.x = 0

    elif key.lower() == KEY_RIGHT:
        vel_msg.angular.z = -pi/4
        vel_msg.linear.x = 0

    elif key.lower() == KEY_BACKWARD:     
        vel_msg.linear.x = -1
        vel_msg.angular.z = 0

    elif key.lower() == KEY_TELEPORT:
        turtle_teleport = rospy.ServiceProxy('turtle1/teleport_absolute',TeleportAbsolute)
        turtle_teleport(5.5,5.5,0)

    elif key.lower() == KEY_ROTATE_180:
        vel_msg.linear.x = 0
        vel_msg.angular.z = pi

    vel_pub.publish(vel_msg)
```

`move_turtle()`: Esta es la función principal del programa. Inicializa un nodo ROS, crea un editor y un mensaje Twist, y entra en un bucle donde lee continuamente las pulsaciones de teclas, las maneja y se interrumpe si se pulsa la tecla Salir.

``` Python
def move_turtle():
    # Inicialización de nodo
    rospy.init_node('my_turtle',anonymous=True) 
    # Se instancia el objeto Publisher con el tópico cmd_vel para modificar velocidad
    vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist,queue_size=10)
    # Se crea el objeto tipo Twist para enviar los comandos de velocidad al nodo de la tortuga
    vel_msg = Twist()

    while True:
        key = get_key() # Cada iteración del bucle se lee la entrada de teclado
        key = key.decode('utf-8',errors='replace') # Se convierte la variable hexadecimal a str

        try:    
            handle_key(key, vel_msg, vel_pub)
        
        except Exception as e:
            rospy.logerr(f"Error handling key: {e}")

        if key.lower() == KEY_QUIT:
            break
```

## Resultados
En el siguiente video, se muestra los resultados obtenidos al ejecutar el script de python elaborado.



## Análisis

El tópico /cmd_vel en ROS se utiliza para enviar comandos de movimiento a un robot. Este tópico utiliza el tipo de mensaje geometry_msgs/Twist, que representa la velocidad lineal y angular del robot en el espacio 3D.

**Componentes del mensaje geometry_msgs/Twist:**

El mensaje geometry_msgs/Twist se compone de dos vectores 3x1:

- **Velocidad lineal:** Representa la velocidad del robot en el plano horizontal, con componentes en x, y, y z. El componente x indica la velocidad hacia adelante o hacia atrás, el componente y indica la velocidad lateral (a la izquierda o derecha) y el componente z no se utiliza comúnmente en robots terrestres.

- **Velocidad angular:** Representa la velocidad de rotación del robot sobre sus ejes. Un valor positivo indica una rotación en sentido antihorario, mientras que un valor negativo indica una rotación en sentido horario.

**Control de movimiento del robot:**

  - Cuando la tecla A sea presionada se publicará un tópico Twist() con una velocidad angular en z de +1 para rotación antihoraria.
  - Cuando la tecla D sea presionada se publicará un tópico Twist() con una velocidad angular en z de -1 para rotación horaria.
 -  Cuando la telca W sea presionada se publicará un tópico Twist() con una velocidad lineal en x de +1 para ir hacia adelante.
  - Cuando la telca S sea presionada se publicará un tópico Twist() con una velocidad lineal en x de -1 para ir hacia atras.
 - Cuando la tecla R sea presionada se llamará al servicio TeleportAbsolute() para que lleve a la tortuga a las coordenadas (5.5,5.5) y le de una orientación de 0°respecto a la horizontal de la pantalla.
- Cuando la tecla Espacio sea presionada se llamará al servicio TeleportRelative() con un desplazamiento lineal nulo y un desplazamiento angular de 180°.

# Conclusiones
* El tópico `/cmd_vel` proporciona una forma sencilla y estandarizada de controlar el movimiento de robots en ROS. Al comprender la estructura del mensaje `geometry_msgs/Twist` y las relaciones entre los componentes de velocidad lineal y angular, se puede controlar el movimiento del robot con precisión y eficiencia.


 * MatLab es un software con un amplio desarrollo en diferentes areas de estudio. Siendo así que cuenta con un toolbox para ROS, que permite la conexión directa con el nodo maestro, si bien no fue necesario la llamada de funciones de un nivel de complejidad más alta, este toolbox puede ser muy util en próximas practicas.

<span><img id="Fig_7" src="Imágenes/Toolbox.png" width="450"/>
<label for = "Fig_7" ><br><b>Figura 7.</b> ROS Toolbox.</label></span>

* El proceso de pre-desarrollo tiene un mayor grado de complejidad que la practica en si, ya que se somete al practicante a nuevos entornos de desarrollo, sistemas operativos. Con los cuales no está familiarizado, generando una retroalimentación constante sobre sus errores y aciertos.