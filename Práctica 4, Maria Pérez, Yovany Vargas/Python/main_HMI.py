# -- coding: utf-8 --
import rospy
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import HMI 

pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)

def Deg2Rad(pose_deg):
    pose_rad = [value*np.pi/180 for value in pose_deg]
    return pose_rad

# Poses en radianes
home = Deg2Rad([0, 0, 0, 0, 0])
pose2 = Deg2Rad([25, 25, 20, -20, 0])
pose3 = Deg2Rad([-35, 35, -30, 30, 0])
pose4 = Deg2Rad([85, -10, 55, 25, 0])
pose5 = Deg2Rad([0, -10, 90, -90, 45])

posturas = [home, pose2, pose3, pose4, pose5] # array de poses

def callback(data):
    data = [value*180/np.pi for value in data.position]
    HMI.data_to_HMI(data)

# Función que permite suscribirse al tópico de articulaciones
def listener():
    rospy.Subscriber("/dynamixel_workbench/joint_states", JointState, callback)

# Función que permite publicar en cada tópico de controlador de articulación
def joint_publisher(postura_seleccionada:int):
    global pub, posturas
    postura_seleccionada = posturas[postura_seleccionada]
    state = JointTrajectory()
    state.header.stamp = rospy.Time.now()
    state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5"]
    point = JointTrajectoryPoint()
    point.positions = postura_seleccionada
    point.time_from_start = rospy.Duration(0.5)
    state.points.append(point)
    pub.publish(state)
    print('published command')
    rospy.sleep(1)

def main():
    global pub
    # Publicador de tópico de controlador de articulación
    rospy.init_node('joint_publisher', anonymous=False)
    
    HMI.main()
        
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass