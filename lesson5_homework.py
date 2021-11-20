# 1)

# . Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:

# >>> >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"

# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для 
# перевода: какой тип данных выбрать, в теле функции или снаружи.


# 2)
# Необходимо создать класс Ingredient, конструктор класса принимает три обязательных аргумента:

#     name - название ингредиента
#     weight - вес в граммах
#     cost - стоимость в рублях

# В класс Ingredient необходимо добавить следующие getter-методы:

#     get_name() - возвращает название ингредиента
#     get_weight() - возвращает вес в граммах
#     get_cost() - возвращает стоимость в рублях

# Необхоидмо создать класс Pizza, конструктор класса принимает один обязательный аргумент name - название пиццы.

# Необходимо добавить в класс следующие методы:

#     get_name() - возвращает название пиццы
#     add_ingredient(ingredient) - принимает объект типа Ingredient и добавляет ингредиент в пиццу
#     get_cost() - возвращает стоимость пиццы в рублях
#     get_weight() - возвращает вес пиццы в килограммах (1кг=1000г)

class Pizza:
	def __init__(self, name):
		self.name = name
		self.ingredients = []

	def get_name(self):
		return self.name

	def add_ingredient(self, ingredient):
		self.ingredients.append(ingredient)

a = Pizza('with pinapples')
a.get_name()

class Ingredient:
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

    def get_name(self): # возвращает название ингредиента
        return self.name
    
    def get_weight(self): # возвращает вес в граммах
        return self.weight 

    def get_cost(self): # возвращает стоимость в рублях
        return self.cost

# cream = Ingredient('крем-брюле', 200, 150) # __init__(cream, крем-брюле', 200, 150)
# cream_sauce = Ingredient('Сливочный соус', 50, 50)
# blue_cheese = Ingredient('Сыр блю чиз', 100, 100)
# mozzarella = Ingredient('Моцарелла', 100, 100)
# cheddar = Ingredient('Чеддер', 100, 100)
# parmesan = Ingredient('Пармезан', 100, 100)
# print(cream.get_name())

# ten_cheeze_and_cream  = Pizza('Десять сыров и крем-брюле')
# ten_cheeze_and_cream.add_ingredient(cream)
# ten_cheeze_and_cream.add_ingredient(cream_sauce)
# ten_cheeze_and_cream.add_ingredient(blue_cheese)
# ten_cheeze_and_cream.add_ingredient(cheddar)





def num_translate(num):
	dct = {'one': 1, 'two': 2, 'three': 3}
	return dct[num]
