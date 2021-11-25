#!/usr/bin/python3


# 1) Publisher
from rospy import Publisher, init_node, is_shutdown, sleep
from std_msgs.msg import String

init_node("My_first_node")

pub = Publisher("My_first_topic", String, queue_size=20)

s = String()
s.data = "Hello, truecoders!"

# print(dir(Publisher))

while not is_shutdown():
    pub.publish(s)
    sleep(1)
