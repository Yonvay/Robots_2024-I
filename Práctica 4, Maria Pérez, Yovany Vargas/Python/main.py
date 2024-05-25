# -- coding: utf-8 --
import rospy
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def Deg2Rad(pose_deg):
    pose_rad = [value*np.pi/180 for value in pose_deg]
    return pose_rad

def callback(data):
    data = [value*180/np.pi for value in data.position]
    print (f"Joint1: {data[0]:.2f}°, Joint2: {data[1]:.2f}°, Joint3: {data[2]:.2f}°, Joint4: {data[3]:.2f}°, Joint5: {data[4]:.2f}°")

# Función que permite suscribirse al tópico de articulaciones
def listener():
    rospy.Subscriber("/dynamixel_workbench/joint_states", JointState, callback)

# Función que permite publicar en cada tópico de controlador de articulación
def joint_publisher(postura: list, pub: rospy.Publisher):
    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5"]
    point = JointTrajectoryPoint()
    point.positions = postura  
    point.time_from_start = rospy.Duration(1)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(1)

def main():
    # Poses en radianes
    home = Deg2Rad([0, 0, 0, 0, 0])
    pose2 = Deg2Rad([25, 25, 20, -20, 0])
    pose3 = Deg2Rad([-35, 35, -30, 30, 0])
    pose4 = Deg2Rad([85, -20, 55, 25, 0])
    pose5 = Deg2Rad([0, -10, 90, -90, 0])
    posturas=[home,pose2,pose3,pose4,pose5] # array de poses
    postura_seleccionada = None # postura seleccionada

    # Publicador de tópico de controlador de articulación
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    
    while not rospy.is_shutdown():
        #control de mov. con teclas.
        print("\n1=home, \n2=[25, 25, 20, -20, 0], \n3=[-35, 35, -30, 30, 0], \n4=[85, -20, 55, 25, 0], \n5=[80, -35, 55, -45, 0]")
        key=input("Ingrese la tecla de la postura deseada: " )
        
        if key == '1':
            postura_seleccionada = home
            key = ' '
        elif key == '2':
            postura_seleccionada = pose2
            key = ' '
        elif key == '3':
            postura_seleccionada = pose3
            key = ' '
        elif key == '4':
            postura_seleccionada = pose4
            key = ' '
        elif key == '5':
            postura_seleccionada = pose5
            key = ' '
        else:
            postura_seleccionada = None
        
        if postura_seleccionada != None:
            joint_publisher(postura_seleccionada, pub)
        else:
            listener()
        
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass