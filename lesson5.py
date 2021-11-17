# todo: функции -резюме

def cool_sum(a, b):
	return a + b

# print(cool_sum(5, 4)) 

# todo: ООП


# todo: Типы в Python и ООП


# todo: создание собственных классов(типов)

class Auto:
	wheels = 4
	def __init__(self, name):
		self.name = name # lada.name = 'Kalina'
		# print(f'Создан экземпляр с именем {self.name}')

	def move_forward(self, meters):
		print(f'Я {self.name} и я передвинулася на {meters} метров!')

	def get_data(self):
		print(f'name: {self.name} WIN: {self.number} is_police: {self.is_police} weight: {self.weight}')



# todo: создание экземпляров собственных классов(типов)
lada = Auto('Kalina') # __init__(lada, 'Kalina')
subaru = Auto('Impreza')

lada.number = 75643
lada.is_police = True
lada.weight = 1500
# print(f'WIN: {lada.number} is_police: {lada.is_police} weight: {lada.weight}')

# lada.get_data() #get_data(lada)

# def f():
# 	n = 10

# print(n)


# print(lada.name)
# lada.name = 'Granta'
# print(f'{lada.name} {lada.wheels}')
# print(f'{subaru.name} {subaru.wheels}')
# lada.move_forward(7) # move_forward(lada, 7)
# subaru.move_forward(7) # move_forward(lada, 7)


# todo: создание атрибутов

# а)динамических:

# b)статических

# todo: создание функций для экземпляров собственных классов(типов)


# todo: написание коструктора
class Auto:
	wheels = 4
	def __init__(self, name):
		self.name = name # lada.name = 'Kalina'
		# print(f'Создан экземпляр с именем {self.name}')

	def move_forward(self, meters):
		print(f'Я {self.name} и я передвинулася на {meters} метров!')

	def get_data(self):
		print(f'name: {self.name} WIN: {self.number} is_police: {self.is_police} weight: {self.weight}')

# lada = Auto('Kalina') # __init__(lada, 'Kalina')
# subaru = Auto('Impreza')

# lada.number = 75643
# lada.is_police = True
# lada.weight = 1500

# Person
# 1) должен быть коструктор принимающий:
# имя
# возраст
# профессию
# 2)функция для каждого из этих статических атрибутов

class Person:
	def __init__(self, name, age, skills):
		self.name = name
		self.age = age
		self.skills = skills

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def get_skills(self):
		return self.skills

# me = Person('Sergey', 25.0, 'Dev/Teacher/Small-talk')
# you = Person('Mukchammad', 17, 'Small-talk/chatter-box')
# # print(me.get_name(), me.get_skills())
# # print(me.get_age(), you.get_skills())
# print(type(1))

dct = {1: 'one', 2: 'two', 3:'three'}
# print('hello world!'.split(' '))
for key, value in dct.items():
	print(f'ключ: {key} значение: {value}')