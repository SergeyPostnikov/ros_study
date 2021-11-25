# 1) Publisher
# todo: Разобрать с какими классами работаем, импортировать их
from rospy import Publisher, init_node, is_shutdown, sleep
from std_msgs.msg import String

# todo: поднять ноду
init_node("Имя_ноды")

# todo: создать топик (объект издатель)
pub = Publisher("Имя_топика", Класс/Тип_сообщения, размер очереди)

# todo: создать объект сообщения и закинуть сообщение в него
msg = String()
msg.data = "Сообщение в топик"

# todo: Рабочий цикл
while not is_shutdown():
	объект_издатель.publish(объект_строки)
	sleep(1) 




# 2)Suscriber
# todo: Разобрать с какими классами/функциями работаем, импортировать их

from rospy import init_node, spin
from rospy.topics import Subscriber

from std_msgs.msg import String

# todo: поднять ноду
init_node("Имя_ноды")

# todo: функция обработки сообщения
def f(msg):
	print(msg.data)

# todo: создать объект Подписчик
sub = Subscriber("Имя_топика_Издателя", Класс/Тип_сообщения, функция_обработки_сообщения)

# todo: крутимся
spin()