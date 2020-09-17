import rospy
from neato_node.msg import Bump
import rospy

rospy.init_node("e_stop") #init node
rospy.Subscriber('/bump', Bump)


# while not rospy.is_shutdown():

print('hello world')