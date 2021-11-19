"""
Необходимо создать класс Ingredient, конструктор класса принимает три обязательных аргумента:

    name - название ингредиента
    weight - вес в граммах
    cost - стоимость в рублях

В класс Ingredient необходимо добавить следующие getter-методы:

    get_name() - возвращает название ингредиента
    get_weight() - возвращает вес в граммах
    get_cost() - возвращает стоимость в рублях

Необхоидмо создать класс Pizza, конструктор класса принимает один обязательный аргумент name - название пиццы.

Необходимо добавить в класс следующие методы:

    get_name() - возвращает название пиццы
    add_ingredient(ingredient) - принимает объект типа Ingredient и добавляет ингредиент в пиццу
    get_cost() - возвращает стоимость пиццы в рублях
    get_weight() - возвращает вес пиццы в килограммах (1кг=1000г)

Необходимо создать класс Order и добавить в него следующие методы:

    add_pizza(pizza) - принимает объект типа Pizza и добавляет пиццу в заказ
    get_cost() - возвращает стоимость заказа в рублях

    print_receipt() - печатает чек на экран, пример вывода чека на экран:

    Четыре сыра (0.450кг) - 450.00руб
    Ветчина и сыр (1.000кг) - 600.00руб
    Мясная (0.550кг) - 445.00руб """




cream_sauce = Ingredient('Сливочный соус', 50, 50)
blue_cheese = Ingredient('Сыр блю чиз', 100, 100)
mozzarella = Ingredient('Моцарелла', 100, 100)
cheddar = Ingredient('Чеддер', 100, 100)
parmesan = Ingredient('Пармезан', 100, 100)

pizza = Pizza('Четыре сыра')
pizza.add_ingredient(cream_sauce)
pizza.add_ingredient(blue_cheese)
pizza.add_ingredient(mozzarella)
pizza.add_ingredient(cheddar)
pizza.add_ingredient(parmesan)

order = Order()
order.add_pizza(pizza)
order.add_pizza(pizza)
order.add_pizza(pizza)


# импорт в python



# git
git clone
git commit
git add
git push
git pull
git log
git status
git branch
git checkout
