from pynput.keyboard import Key, Listener
import rospy
#from getkey import getkey, keys
from geometry_msgs.msg import Twist 
from turtlesim.srv import TeleportAbsolute,TeleportRelative
from std_srvs import srv

#movimiento lineal
def pubVel(vel_x, ang_z, t):
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('velPub', anonymous=False)
    vel = Twist()
    vel.linear.x = vel_x
    vel.angular.z = ang_z
    #rospy.loginfo(vel)
    endTime = rospy.Time.now() + rospy.Duration(t)
    while rospy.Time.now() < endTime:
        pub.publish(vel)

#movimiento absoluto (pose x,y,ang)
def teleport(x, y, ang):
    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        teleportA = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        resp1 = teleportA(x, y, ang)
        #print('Teleported to x: {}, y: {}, ang: {}'.format(str(x),str(y),str(ang)))
    except rospy.ServiceException as e:
        print(str(e))

#movimiento relativo (linear, ang)
def move(x, ang):
    rospy.wait_for_service('/turtle1/teleport_relative')
    try:
        moveA = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)
        resp1 = moveA(x, ang)
        #print('Relatively teleported to x: {}, ang: {}'.format(str(x),str(ang)))
    except rospy.ServiceException as e:
        print(str(e))


#teclas de movimiento
def on_press(key):
    #key =getkey()
    print('tecla presionada: {0}'.format(key))
    if key == 'a':
        #rotacion antihoraria,angz+
        pubVel(0,1,0.5)
    elif key == 'd':
        #rotacion horaria ,angz-
        pubVel(0,-1,0.5)
    elif key == 'w':
        #hacia adelante ,velx+
        pubVel(1,0,0.5)
    elif key == 's':
         #hacia atras, velx-
        pubVel(-1,0,0.5)    
    elif key == 'r':
        #R para volver a posición y rotacion inicial
        teleport(5.5,5.5,0)
    elif key == ' ':
        #espacio para rotar 180°
        move(0,mt.pi)

def on_release(key):
    if key == Key.esc:
        return False


if __name__ == '__main__':
    pubVel(0,0,0.1)
    try:
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except rospy.ROSInterruptException:
        pass
   