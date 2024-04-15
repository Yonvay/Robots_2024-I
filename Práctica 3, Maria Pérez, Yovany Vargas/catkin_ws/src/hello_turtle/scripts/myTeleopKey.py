#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute
import termios, sys, os
from numpy import pi

# Definición de las teclas
KEY_FORWARD = 'w' # Movimiento hacia adelante
KEY_BACKWARD = 's' # Movimiento hacia atrás
KEY_LEFT = 'a' # Rotación hacia la izquierda/ anti-horaria
KEY_RIGHT = 'd' # Rotación hacia la derecha/ horaria
KEY_QUIT = 'q' # Salir del programa
KEY_TELEPORT = 'r' # retornar a  posición y orientación centrales
KEY_ROTATE_180 = ' ' # Rotar 180 grados

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

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass

    