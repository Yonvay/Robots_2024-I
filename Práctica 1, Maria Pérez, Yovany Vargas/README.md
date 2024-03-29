# Laboratorio 1, Robótica Industrial - Trayectorias, Entradas y Salidas Digitales <!-- omit from toc -->

Róbotica 2024-I

Universidad Nacional de Colombia

**INTEGRANTES**
- Maria Alejandra Peréz Petro
- Yovany Esneider Vargas Gutierrez

**TABLA DE CONTENIDO**
- [1. Descripción de la solución planteada](#1-descripción-de-la-solución-planteada)
  - [A. Reconocimiento y caracterización del WorkObject](#a-reconocimiento-y-caracterización-del-workobject)
  - [B. Consideraciones en el diseño de herramienta](#b-consideraciones-en-el-diseño-de-herramienta)
- [2. Diagrama de flujo de acciones del robot](#2-diagrama-de-flujo-de-acciones-del-robot)
- [3. Plano de planta de la ubicación de cada uno de los elementos](#3-plano-de-planta-de-la-ubicación-de-cada-uno-de-los-elementos)
- [4. Descripción de las funciones utilizadas.](#4-descripción-de-las-funciones-utilizadas)
- [5. Diseño de herramienta.](#5-diseño-de-herramienta)
- [6. Código en RAPID del módulo utilizado para el desarrollo de la práctica.](#6-código-en-rapid-del-módulo-utilizado-para-el-desarrollo-de-la-práctica)
- [7. Vídeo con la simulación en _RobotStudio_ así como la implementación de la práctica con el robot real](#7-vídeo-con-la-simulación-en-robotstudio-así-como-la-implementación-de-la-práctica-con-el-robot-real)
- [Referencias](#referencias)


## 1. Descripción de la solución planteada

Se escoge la empresa de transporte DiDi, considerándola una empresa que invierte en marketing debido a sus constantes campañas de marketing en redes sociales, televisión y entretenimiento. Se plantea la escritura de su logo, seguido de las iniciales de los integrantes del Grupo M.P. y Y.V. Ver **Figura 1**.

<span><img id="Fig_1" src="Imágenes/Logo.png" width="300"/>
<label for = "Fig_1" ><br><b>Figura 1.</b> Logo e iniciales.</label>

Donde las letras constan de un solo trazo y el logo todo su contorno. Para el desarrollo idóneo de la practica de laboratorio es necesario un análisis previo a ciertos elementos del entorno de trabajo.   

### A. Reconocimiento y caracterización del WorkObject

En el area de trabajo existen una tablero inclinado y varias cajas de madera, partiendo del objetivo de la practica de laboratorio, este tablero es el WorkObject a trabajar, sin embargo, es necesario ubicarlo considerando el alcance del robot ABB IRB 140. Para esto primero se han de caracterizar este par de objetos.

- **Tablero, WorkObject_1**

Las dimensiones del tablero son; 25.2 cm de alto y 25 cm de ancho, su parte trasera que cumple la función de apoyo tiene un largo de 26.8 cm. Partes unidas por sus extremos en un angulo de 90°, entonces el angulo entre la base y al tablero es de 46.76° ver **Figura 2**.

<span><img id="Fig_2" src="Imágenes/Board.png" width="400"/>
<label for = "Fig_2" ><br><b>Figura 2.</b> Dimensiones de tablero inclinado.</label></span>

Ahora, se usa el ancho de la caja como soporte externo para el tablero, de medida 43 cm, ubicado desde el suelo. La distancia desde el cero de la base del robot ABB IRB 140 a la parte superior de la caja, es de 19 cm.

Con estos datos, la ubicación seleccionada para el *WorkObject_1* tomando como punto de referencia el punto inferior interno de la base del tablero ver **Figura 3** y respecto a la base del robot es; 1200 mm en X, -125 mm en Y y 190 mm en Z ver **Figura 4**.

<span><img id="Fig_3" src="Imágenes/WorkObject_1.png" width="300"/>
<label for = "Fig_3" ><br><b>Figura 3.</b> WorkObject_1 en RobotStudio.</label></span>

<span><img id="Fig_4" src="Imágenes/Ubicación.png" width="300"/>
<label for = "Fig_4" ><br><b>Figura 4.</b> Ubicación WorkObject_1 en RobotStudio.</label></span>

Así el objecto de trabajo está en condiciones optimas para el trazo de las trayectorias.

### B. Consideraciones en el diseño de herramienta

Debido a la alta exactitud del robot ABB IRB 140 se precisa la misma exactitud en la ubicación del WorkObject, sin embargo, no se poseen las herramientas necesarias para esta tarea, por tanto es necesario un método que permita tener un rango de tolerancia. Dicho método está ubicado en la herramienta, ya que el robot no admite modificaciones. Se plantea un resorte bloqueado por un pasador, con un desplazamiento de 3 cm, permitiendo el desplazamiento del marcador aun si el WorkObject no esta en la posición correcta.

Bajo estás consideraciones, la metodología a desarrollar es la siguiente:

- **Creación de modelos CAD**

La creación del WorkObject y la herramienta se llevo a cabo con el software Autodesk Inventor, donde el logo e iniciales están descritos solo por lineas y curvas **Figura 5**. Cabe aclarar que existen 2 versiones de la herramienta, una para su representación completa en RobotStudio, que cuenta con una punta pronunciada y la segunda version para la impresión 3D ver **Figura 6**.

<span><img id="Fig_5" src="Imágenes/Iniciales.png" width="300"/>
<label for = "Fig_5" ><br><b>Figura 5.</b> Logo e iniciales Autodesk Inventor.</label></span>

<span><img id="Fig_6" src="Imágenes/Herramienta.png" width="300"/>
<label for = "Fig_6" ><br><b>Figura 6.</b> Modelado de herramienta para RobotStudio e impresión 3D, Autodesk Inventor.</label></span>

- **Montaje de herramienta y WorkObject**

Desde Autodesk Inventor se exportan los modelados en formato .SAT, seguidamente se importan los modelados a RobotStudio. Desde la pestaña Modelado, sección Mecanismo, se crea la herramienta, donde una vez asignado el TCP en el modelado, la herramienta se incorpora al robot ver **Figura 7**.

<span><img id="Fig_7" src="Imágenes/Montaje.png" width="300"/>
<label for = "Fig_7" ><br><b>Figura 7.</b> Montaje de herramienta RobotStudio.</label></span>

Una vez importado el modelado del tablero con el logo e iniciales en su superficie, se crea el WorkObject_1. Donde el punto asignado será la esquina superior interna del tablero ver **Figura 8**.

<span><img id="Fig_8" src="Imágenes/WorkObject_1RS.png" width="300"/>
<label for = "Fig_8" ><br><b>Figura 8.</b> Creación WorkObject_1 RobotStudio.</label></span>

- **Definición y programación de las trayectorias**

Para un optimo proceso, se decide separar la trayectoria general en sub-trayectorias, asignadas al logo y las iniciales, para un total de 9 sub-trayectorias. Junto a 2 trayectorias generales extras donde se establece el Home y la posición de Mantenimiento ver **FIGURA 9**.

<span><img id="Fig_9" src="Imágenes/Trayectorias.png" width="300"/>
<label for = "Fig_9" ><br><b>Figura 9.</b> Trayectorias RobotStudio.</label></span>

Con la ayuda de las herramientas para la selección de puntos en las aristas y curvas se establecen los movimientos, para los desplazamientos a los puntos iniciales del logo e iniciales, se utiliza la instrucción MoveJ y para los trazos MoveL, en casos de circunferencias MoveC. La descripción detallada de estas funciones se encuentra en la **Sección 4**.

- **Definición y programación de las entradas y salidas**

Aunque en los planteamientos de la practica de laboratorio se exige un total de 2 entras y salidas, se opta por
una distribución de 3, para tener un mayor control sobre el robot, donde la DI_01 ejecuta la rutina de escritura a la vez que activa la salida DO_01, DI_02 ejecuta la rutina que lleva el robot a posición de mantenimiento conmutando DO_02, y DI_03 ejecuta la acción de Homing ver **Figura 10**.

<span><img id="Fig_10" src="Imágenes/IO's.png" width="300"/>
<label for = "Fig_10" ><br><b>Figura 10.</b> I/O digitales RobotStudio.</label></span>

Se entra en detalle en su programación en la **Sección 6**.

- **Simulación**

Una vez programadas las rutinas, entradas y salidas es posible emplear una simulación en RobotStudio, al mismo tiempo que se simulan las entradas y salidas, con el fin de comprobar el correcto funcionamiento de la programación antes designada, esto se explora en detalle en la **Sección 7**.

- **Ejecución en vivo**

Una vez comprobado el correcto funcionamiento de las rutinas, entradas y salidas. Se lleva a cabo el montaje aproximado del WorkObject_1, se instala la herramienta en el robot y se carga la programación con USB mediante el FlexPendant, para su posterior ejecución en vivo, la evidencia en video se encuentra en la **Sección 7**.

## 2. Diagrama de flujo de acciones del robot 

La figura 11 muestra el flujo de acciones del robot. Cuando el robot arranca, ingresa a un bucle "WHILE TRUE DO". Dentro del bucle, se verifica el estado de las entradas digitales (DI). Si DI_01 está activo, se ejecuta el procedimiento "GoEscritura" que ejecuta una serie de instrucciones específicas para la tarea de escribir el logo de DIDI y las iniciales como se muestra en la **Figura 1**. Si DI_02 está activo, se ejecuta la función "GoMantenimeinto" que  mueve el robot a la posición de "Mantenimiento" establecida. Si DI_03 está activo, se ejecuta la función "Homing" que mueve el robot a la posición "Home". Si ninguna de las entradas digitales está activa, el bucle continúa sin realizar ninguna acción, es decir no realiza acciones a menos que reciba entradas.

<span><img id="Fig_11" src=".\Imágenes\DiagramaDeFlujoMain.png" width="400"/>
<label for = "Fig_11" ><br><b>Figura 11.</b> Diagrama de flujo de las acciones del robot.</label></span>


## 3. Plano de planta de la ubicación de cada uno de los elementos

Para visualizar correctamente el plano de planta, acceda a su enlace a continuación.
[Plano de planta, ubicación de cada uno de los elementos.](/Lab_1_Maria%20Pérez_Yovany%20Vargas/Plano%20Planta.pdf)


## 4. Descripción de las funciones utilizadas.

Para las instrucciones de movimiento se utilizaron los comandos RAPID  `MoveL`,`MoveJ`,y `MoveC` según la necesidad.

- `MoveL`: Instrucción que mueve el robot en una línea recta desde su posición actual hasta la posición 
objetivo especificada. **Sintaxis:**  ``MoveL ToPoint, Speed, Zone, Tool; ``

-  `MoveJ`: Se utiliza para mover el robot rápidamente de un punto a otro cuando no es imprescindible que el 
movimiento siga una línea recta. Se utiliza para hacer acercamientos o alejamientos rápidos a una pieza. **Sintaxis:**  ``MoveJ ToPoint, Speed, Zone, Tool; ``

- `MoveC`: Se usa para mover el robot describiendo un arco de círculo, requiere dos puntos objetivo.  **Sintaxis:**  ``MoveC ToPoint_1, ToPoint_2, Speed, Zone, Tool; ``

El ``zonedata`` define el rango de tolerancia al llegar a una posición, es decir, a 
qué distancia de la posición programada deben encontrarse los ejes antes de iniciar un 
movimiento hasta la posición siguiente. En está práctica, se establece el parámetro Finep, fine point como True, con el fin de tener una mayor fidelidad en el trazo, sin embargo, presenta inconvenientes de singularidad en varias ocasiones.

Para la configuración de las salidas digitales se uso el comando:
- ``Set``: Da el valor de 1/0 lógico a la salida digital según se indique.


## 5. Diseño de herramienta.

Para el diseño de la herramienta, se identifican las dimensiones de la base de la herramienta en el datasheet del robot ver **Figura 12**.

<span><img id="Fig_12" src=".\Imágenes\BaseHerramienta.png" width="300"/>
<label for = "Fig_12" ><br><b>Figura 12.</b> Base de la herramienta, ABB IRB 140.</label></span>

Seguidamente junto a las medidas de un marcador `Pelikan 426` y las [consideraciones en el diseño de herramienta](#b-consideraciones-en-el-diseño-de-herramienta), se diseña la herramienta en 2 partes. El Porta-Marcador y un pasador que bloquea la salida del resorte ver **Figura 13**.

<span><img id="Fig_13" src=".\Imágenes\FullTool.png" width="300"/>
<label for = "Fig_13" ><br><b>Figura 13.</b> Herramienta Autodesk Inventor.</label></span>

Con la impresión 3D, el resultado final es el siguiente ver **Figura 14**. Ante posibles inconvenientes en las dimensiones finales se lijan las piezas involucradas, en este caso el pasador.

<span><img id="Fig_14" src=".\Imágenes\RealTool.jpg" width="300"/>
<label for = "Fig_14" ><br><b>Figura 14.</b> Herramienta en físico.</label></span>

Las dimensiones completas de la herramienta se encuentran en su plano asociado, [plano de la herramienta.](/Lab_1_Maria%20Pérez_Yovany%20Vargas/Plano%20Herramienta.pdf)

## 6. Código en RAPID del módulo utilizado para el desarrollo de la práctica.
El código en RAPID del módulo utilizado para el desarrollo de la práctica se encuentra en el archivo [Module1.mod](./RobotStudio/Controller%20Data/Controlador1/RAPID/TASK1/PROGMOD/Module1.mod). 

En primer lugar, el módulo contiene las definiciones de las variables `robtarget` que representan las diferentes posiciones del robot. Cada variable robtarget se define como una lista que contiene los siguientes elementos:
- Posición X, Y, Z: Coordenadas de la posición en milímetros.
- Orientación: Matriz de rotación 4x4 que define la orientación del robot en la posición.
- Ejes de la herramienta: Vector que define los ejes de la herramienta en la posición.
- Límites de singularidad: Vector que define los límites de singularidad del robot en la posición.

Adicionalmente, el módulo contiene cada una de las rutinas del robot, las cuales se describen a continuación.

- **Main:** bloque de procedimiento que contiene la lógica principal del flujo de acciones del robot.
  
```    
PROC Main() 
    WHILE TRUE DO
        IF DI_01 = 1 THEN
            GoEscritura;
        ELSEIF DI_02 = 1 THEN
            GoMantenimeinto;
        ELSEIF DI_03 = 1 THEN
            Homing;
        ENDIF
    ENDWHILE
ENDPROC
```
   
- **GoEscritura:**
bloque de procedimiento que ejecuta la rutina de escritura y enciende una luz de indicación (DO_01). Primero, se ejecutan las rutinas `Logo`, `D1`, `I1`, `D2`, `I2` para escribir el logo DIDI. Luego, se escriben las iniciales de los integrantes con las rutinas `M`, `P`, `Y` y `V`. Por último, el manipulador se apaga la luz de indicación relacionada.

``` 
PROC GoEscritura()
    Homing;
    SetDO DO_03,0;
    SetDO DO_01,1;
    Logo;
    D1;
    I1;
    D2;
    I2;
    M;
    P;
    Y;
    V;
    SetDO DO_01,0;
ENDPROC
```

- **GoMantenimeinto:**  posiciona el manipulador en una pose de mantenimiento donde se puede instalar o desinstalar la herramienta y enciende la luz de indicación (DO_02) mientras está en ejecución.

```
PROC GoMantenimeinto()
    Homing;
    SetDO DO_03,0;
    SetDO DO_02,1;
    MoveJ Mantenimiento,v200,z10,FinalTool\WObj:=wobj0;
    SetDO DO_02,0;
ENDPROC
```

- **Homing:** mueve el robot a la posición de Home y enciende la luz de indicación (D0_03). En la posición HOME todos los ángulos articulares son 0 grados, a excepción de la articulación 6 que queda a 30°.
``` 
PROC Homing()
    SetDO DO_03,1;
    MoveJ Home,v300,z10,FinalTool\WObj:=wobj0;
ENDPROC
```

Finalmente, las rutinas detalladas para cada letra y dibujo del logo (`Logo`, `D1`, `I1`, `D2`, `I2`, `M`, `P`, `Y` y `V`) se pueden encontrar en el modulo RAPID [Module1.mod](./RobotStudio/Controller%20Data/Controlador1/RAPID/TASK1/PROGMOD/Module1.mod). 


## 7. Vídeo con la simulación en _RobotStudio_ así como la implementación de la práctica con el robot real

El video se encuentra alojado en YouTube, acceder mediante este link: [Video, simulación y robot real.](https://youtu.be/UkpNaTU_DuQ)

El resultado final se ve en la **Figura 15**. Se observan pequeños trazos erróneos en la letra Y, debido a la imposibilidad de ubicar de manera precisa el WorkObject_1. Por otra parte, las consideraciones de la herramienta fueron acertados, permitiendo replicar la practica en mas de una ocasión.

<span><img id="Fig_15" src=".\Imágenes\Final.jpg" width="300"/>
<label for = "Fig_15" ><br><b>Figura 15.</b> Resultado final.</label></span>

## Referencias

[1] ABB, Robotics, _Especificaciones del producto, IRB 140_, Skribenta version 5.3.075, ID: 3HAC041346-005. Recuperado de: [Abb library](https://library.e.abb.com/public/84e6cb203eef4658839e7cf66e8eaf71/3HAC041346%20PS%20IRB%20140-es.pdf?x-sign=ImRvOsT2Jz0WrduLX2Ku7h+p8psQ+kwuvQhn/UcW7RoyrJUh8FyguShi/V3lJkkI)
