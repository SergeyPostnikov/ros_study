from rospy import init_node, spin
from rospy.topics import Subscriber

from std_msgs.msg import String

init_node("My_subscriber")




def echo(msg):
	msg.data += 'Hello, steal shiny friend!' 
	print(msg)

subscriber = Subscriber("My_first_topic", String, echo)
spin()
