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

Function navegar
	'Se enciende la salida 10
	'Indicando que está en ejecución
	On estado_navegar
	
	'Movimientos con Go
	Go Origen
	Wait 0.5
	Go EjeX
	Wait 0.5
	Go EjeY
	Wait 0.5
	Go Origen
	Wait 0.5 'Espera 500 ms
	
	Off estado_navegar
Fend

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
	'Indicando que la rutina ha terminado
	Off estado_paletizado_z
Fend

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
	'Indicando que la rutina ha terminado
	Off estado_paletizado_s
Fend

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
	'Indicando que la rutina ha terminado
	Off estado_paletizado_ex
Fend