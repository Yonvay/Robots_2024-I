# Laboratorio 2, Epson <!-- omit from toc -->

Robótica 2024-I

Universidad Nacional de Colombia

**INTEGRANTES**
- Maria Alejandra Peréz Petro
- Yovany Esneider Vargas Gutierrez

**TABLA DE CONTENIDO**
- [1. Especificaciones del robot utilizado](#1-especificaciones-del-robot-utilizado)
- [2. Desarrollo de práctica](#2-desarrollo-de-práctica)
	- [A. Consideraciones](#a-consideraciones)
	- [B. Descripción de las funciones utilizadas](#b-descripción-de-las-funciones-utilizadas)
	- [C. Descripción detalla del código](#c-descripción-detalla-del-código)
- [3. Videos](#3-videos)
	- [A. Simulación](#a-simulación)
	- [B. Ejecución en Robot](#b-ejecución-en-robot)
  
## 1. Especificaciones del robot utilizado

Modelo: EPSON VT6-A901S

Tipo: Seis ejes

Alcance: 920 mm

Carga útil máxima: 6 kg

El robot disponible no cuenta con modulo de entradas y salidas digitales, ni Teach Pendant.

<span><img id="Fig_1" src="Imágenes/EPSON VT6-A901S.jpeg" width="150"/>
<label for = "Fig_1" ><br><b>Figura 1.</b> Robot EPSON VT6-A901S.</label></span>

El robot tiene dos condiciones de parada de emergencia, botón de parada de emergencia y desconexión del puerto USB. 

## 2. Desarrollo de práctica

### A. Consideraciones

Al igual que en otros robots, EPSON cuenta con un software enfocado a la programación de los mismos en este caso **EPSON RC+ 7.0** compatible con tres tipos de robots: Scara, Seis ejes y Módulos EZ (ver **Figura 2**). El lenguaje de programación que utiliza es **SPEL+**.

<span><img id="Fig_2" src="Imágenes/Tipos.png" width="300"/>
<label for = "Fig_2" ><br><b>Figura 2.</b> Tipos de robots, EPSON RC+ 7.0.</label></span>

En primer lugar, se configuran los puntos que se usaran en las trayectorias. Estos se enseñan en el modulo _administrador de robot_  con la herramienta _Mover y Enseñar_ (JOG&TEACH), ver **Figura 3**.

<span><img id="Fig_3" src="Imágenes/Enseñar.png" width="500"/>
<label for = "Fig_3" ><br><b>Figura 3.</b> Modulo administrador de robot.</label></span>

> [!NOTE]
> Es importante no crear directamente los puntos mediante la inserción de coordenadas, porque esto ocasiona un error de interpretación por parte del software. En lugar de eso, enseñar puntos aleatorios y luego editar sus coordenadas, así se evita dicho error.

Se enseñan 3 tres puntos con las coordenadas indicadas. Ver **Figura 4**.

<span><img id="Fig_4" src="Imágenes/Puntos.png" width="600"/>
<label for = "Fig_4" ><br><b>Figura 4.</b> Puntos.</label></span>

Adicionalmente, en el modulo _administrador de robot_ en la pestaña _Configuración HOME_ se establece el punto para **HOME**. Cuando se llama en código **HOME** se genera una trayectoria interna que lleva el robot al **HOME** establecido. Cabe resaltar que el software permite establecer el orden en que cada articulación se mueve para llegar a este punto, ver **Figura 5**.

<span><img id="Fig_5" src="Imágenes/HOME.png" width="400"/>
<label for = "Fig_5" ><br><b>Figura 5.</b> Punto HOME.</label></span>

Para descargar el código creado en el EPSON RC+ 7.0, se cambia la conexión del controlador virtual a USB. Ver **Figura 6**.

<span><img id="Fig_6" src="Imágenes/USB.png" width="200"/>
<label for = "Fig_6" ><br><b>Figura 6.</b> Conexión USB.</label></span>

### B. Descripción de las funciones utilizadas

- **Go:** Se utiliza para mover el robot rápidamente de un punto a otro cuando no es imprescindible que el 
movimiento siga una línea recta. Se utiliza para hacer acercamientos o alejamientos rápidos a una pieza. **Sintaxis:**  ``Go ToPoint``, también admite como entrada un pallet. Adicionalmente, permite la implementación de offsets sin modificar los puntos preestablecidos ``Go ToPoint :Axis(Offset)``.

- **Wait:** Instrucción donde el robot espera una cantidad de tiempo especificado, sus unidades son los segundos, sin embargo acepta decimales, permitiendo así la inserción de milisegundos (0.5, 500 ms). **Sintaxis:**  ``Wait Time``.

- **Move:** Instrucción que mueve el robot en línea recta desde su posición actual hasta la posición objetivo especificada. **Sintaxis:**  ``Move ToPoint``

Para la configuración de las salidas digitales se usaron los comandos **On** y **Off** que llevan la salida a 1 o 0 respectivamente.

### C. Descripción detalla del código
En primer lugar, se crean todas las variable a utilizar, entre ellas se encuentran contadores, pallets, y se definen las salidas digitales.

Un pallet corresponde a un área distribuida en partes iguales. Para la definción de un pallet son necesarios 3 puntos y las dimensiones de la distribución de partes iguales, donde el centro de cada una de ellas son los puntos establecidos. **Sintaxis:**  ``Pallet Index, Point_1, Point_2, Point_3, Rows, Columns``, existe una variación del mismo, que permite adicionar una fila y columna extra en caso de requerirlo; ``Pallet Outside Index, Point_1, Point_2, Point_3, Rows, Columns``. Ver **Figura 7**.

<span><img id="Fig_7" src="Imágenes/Pallet.png" width="150"/>
<label for = "Fig_7" ><br><b>Figura 7.</b> Pallet.</label></span>

En el main se establecen los valores de potencia, velocidad y aceleración a los cuales el robot ha de funcionar. La rutina de **main** consiste en ir a **HOME**, seguidamente llamar la trayectoria ``navegar``, ``paletizado_z``, ``paletizado_s`` y ``paletizado_externo``, volviendo a **HOME** entre trayectorias.

```SPEL+
Global Integer i, j

Function main
	'Se definen los pallets 
	Pallet Outside, 2, Origen, EjeX, EjeY, 3, 3
	Pallet 1, Origen, EjeX, EjeY, 3, 3
	'Se definen las salidas digitales
	#define estado_navegar 10
	#define estado_navegar_2 11
	#define estado_paletizado_z 12
	#define estado_paletizado_s 13
	#define estado_paletizado_ex 14
	
	Motor On 'Motores On
	Power High 'Potencia Alta para simular y Baja para probar en el robot
	Speed 30 'Velocidad de Go, Jump y Pulse
	SpeedS 100 'Velocidad de Move, Arc...
	Accel 30, 30 '...
	AccelS 100 '...	
	
	Do
		'Se apagan todas las salidas para volver a empezar
		Off estado_navegar
		Off estado_navegar_2
		Off estado_paletizado_z
		Off estado_paletizado_s
		Off estado_paletizado_ex
		'Ejecución de rutinas	
		Home
		If Sw(8) Then
			Call navegar
			Home
		ElseIf Sw(9) Then
			Call navegar_2
			Home
		ElseIf Sw(10) Then
			Call paletizado_z
			Home
		ElseIf Sw(11) Then
			Call paletizado_s
			Home
		ElseIf Sw(12) Then
			Call paletizado_externo
		EndIf
	Loop
Fend
```

La trayectoria ``navegar`` corresponde a la función con su mismo nombre, la cual hace el recorrido por los tres puntos creados con anterioridad, como se vio en la sección de [consideraciones](#a-consideraciones). Se hace el recorrido en primer lugar con la función **Go**, y luego **Move**. Esperando 500 ms entre cada movimiento.

```SPEL+
Function navegar
	'Se enciende la salida 10
	'Indicando que está en ejecución
	On estado_navegar
	'Movimientos con Go
	Go Origen
	Wait 0.5 'Espera 500 ms
	Go EjeX
	Wait 0.5
	Go EjeY
	Wait 0.5
	'Movimientos con Move
	Move Origen
	Wait 0.5
	Move EjeX
	Wait 0.5
	Move EjeY
	Wait 0.5
	'Se apaga la salida 10
	'Indicando que esta ha terminado
	Off estado_navegar
Fend
```

La trayectoria ``navegar_2`` es una modificación de la trayectoria anterior con Go, en la cual la altura de Z se modifica en 200mm, antes y después de la ejecución
de cada punto.

```
Function navegar_2
	'Se enciende la salida 11
	'Indicando que está en ejecución
	On estado_navegar_2
	Go Origen :Z(200)
	Go Origen
	Go Origen :Z(200)
	Wait 0.5
	Go EjeX :Z(200)
	Go EjeX
	Go EjeX :Z(200)
	Wait 0.5
	Go EjeY :Z(200)
	Go EjeY
	Go EjeY :Z(200)
	Go Origen :Z(200)
	Wait 0.5
	'Se apaga la salida 11
	'Indicando que la rutina ha terminado
	Off estado_navegar_2
Fend
```

La trayectoria ``paletizado_z``, hace el recorrido con la función **Go** del pallet de dimensiones 3x3 creado en las primeras lineas di código. Este recorrido se logra mediante un ``for`` que permite el recorrido secuencial de cada una de las nueve ubicaciones en el pallet.

```SPEL+
Function paletizado_z
	'Se enciende la salida 12
	'Indicando que está en ejecución
	On estado_paletizado_z
	'Mediante un For recorre todas las posiciones
	For i = 1 To 9
		Go Pallet(1, i) :Z(200)
		Go Pallet(1, i)
		Go Pallet(1, i) :Z(200)
	Next
	'Se apaga la salida 12
	'Indicando que esta ha terminado
	Off estado_paletizado_z
Fend
```

La trayectoria ``paletizado_s``, hace el recorrido con la función **Go** del pallet en S. Este recorrido se logra alternando entre un paso positivo y negativo, ya que la segunda fila debe recorrerse en dirección contraria para el recorrido en S.

```SPEL+
Function paletizado_s
	'Se enciende la salida 13
	'Indicando que está en ejecución
	On estado_paletizado_s
	For i = 1 To 3
		Go Pallet(1, i) :Z(200)
		Go Pallet(1, i)
		Go Pallet(1, i) :Z(200)
	Next
	For i = 6 To 4 Step -1
		Go Pallet(1, i) :Z(200)
		Go Pallet(1, i)
		Go Pallet(1, i) :Z(200)
	Next
	For i = 7 To 9
		Go Pallet(1, i) :Z(200)
		Go Pallet(1, i)
		Go Pallet(1, i) :Z(200)
	Next
	'Se apaga la salida 13
	'Indicando que esta ha terminado
	Off estado_paletizado_s
Fend
```

La trayectoria ``paletizado_externo``, hace el recorrido con la función **Go** del pallet outside. En este caso se recorre mediante dos ciclos ``for``. Este método también es posible en un pallet normal.

```SPEL+
Function paletizado_externo
	'Se enciende la salida 14
	'Indicando que está en ejecución
	On estado_paletizado_ex
	'Mediante dos For recorre todas las posiciones
	For i = 1 To 4
		For j = 1 To 4
			Go Pallet(2, i, j) :Z(200)
			Go Pallet(2, i, j)
			Go Pallet(2, i, j) :Z(200)
		Next
	Next
	'Se apaga la salida 14
	'Indicando que esta ha terminado
	Off estado_paletizado_ex
Fend
```
> [!NOTE]
> Ambos integrantes elaboraron sus propios códigos, los cuales son esencialmente los mismos. Estos son: [Main_Maria.prg](./Main_Maria.prg) y [Main_Yovany.prg](./Main_Yovany.prg)

## 3. Videos
Los videos están almacenados en una carpeta de drive con acceso general [Link](https://drive.google.com/drive/folders/1T4iOJfjbF1U0leWlQVlbVVba-X9EQseo?usp=drive_link). Hay un total de 4 videos.

> [!IMPORTANT]
> Acceda a Google Drive con su cuenta UNAL, ejemplo@unal.edu.co


### A. Simulación
 Para la simulación, la potencia se estableció en alta (``Power High``) y con el _monitor de E/S_ se controló el inicio de cada rutina.

<span><img id="Fig_8" src="Imágenes/monitor_E_S.png" width="300"/>
<label for = "Fig_8" ><br><b>Figura 8.</b> Monitor de entradas y salidas.</label></span>
	
 La simulación se presenta en el siguiente video:
 [1.Simulacion.mp4](https://drive.google.com/file/d/1ruolqe_OU1eA8WTGTtbdTOF6UgHmL4Xo/view?usp=sharing).

 <span><img id="Fig_9" src="Imágenes\resultados_simulacion.png" width="500"/> <label for = "Fig_9" ><br><b>Figura 9.</b> Resultados de simulación.</label></span>

### B. Ejecución en Robot 
Debido a que el robot no cuenta con modulo de entradas y salidas no es posible el control de trayectorias por medio de entradas digitales. Por ello, se comentan las partes del código ``If Sw(Digital_input)`` asociadas con la lectura de entradas. Adicionalmente, por precaución, la ejecución de la rutina en el robot real se ejecuta en potencia baja (``Power Low``), lo que plantea un delimitador en la velocidad y aceleración. 

Durante la práctica ambos miembros probaron sus códigos elaborados en el robot, los videos de dicha ejecución se presentan a continuación.

[2. Ejecución del código del programa de Maria Peréz](https://drive.google.com/file/d/1h_bwgz-KlUIUS3DazlSsES4aIiHJqVMX/view?usp=drive_link)

[3. Ejecución del código del programa de Yovany Vargas](https://drive.google.com/file/d/1kXkxF5EArWzg4wBgNJhnc32K4FhgaQRT/view?usp=drive_link)

Por último, se presenta un video corto en el que se evidencia el seguimiento de los movimientos del robot en EPSON RC+ 7.0, esto se logra mediante la conexión USB, presente al momento de descargar el código en el controlador del robot.

[4. Vista del software EPSON RC+ 7.0 con el robot en ejecución](https://drive.google.com/file/d/1mAecAb9SD7CPf3xmbNIcIN6Cff_7Qffc/view?usp=drive_link)



## Referencias <!-- omit from toc -->

[1] Control De Movimiento, Control De Movimiento, _CAPACITACIÓN BÁSICA EPSON RC+ 7.0 - ROBOTS SCARA SERIE T_. Recuperado de: [micampus.unal.edu.co](https://micampus.unal.edu.co/pluginfile.php/2688481/mod_assign/introattachment/0/Capacitacio%CC%81n%20ba%CC%81sica%20EPSON%20RC%20%2B%207.0%20SCARA%20SERIE%20T%20131023.pdf?forcedownload=1).