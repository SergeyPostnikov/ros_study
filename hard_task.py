"""Необходимо реализовать простую систему валидации с возможностью дальнейшего расширения.

Любому валидатору, могут потребоваться параметры для выполнения валидации. Например, если валидатор проверяет целые числа, то можно указать как минимальное, так и максимальное допустимое значение целого числа. Эти параметры передаются в конструкторе конкретного валидатора. Помните, что конструктор не является частью интерфейса класса!

    В системе существует базовый абстрактный класс Validator

    Интерфейс класса состоит из одного абстрактного метода validate(value), который принимает валидируемое значение. Метод возвращает True, если value введено верно, или False в случае ошибки.

    Реализовать EMailValidator. Он проверяет, что введенный E-Mail корректный. Дополнительных параметров для валидации не требуется.

    Не торопитесь использовать регулярные выражения, тем более вы можете их и не знать.

    Реализовать DateTimeValidator. Он проверяет, что введенное значение является корректной датой/временем и совпадает с требуемым форматом.

    Формат - это параметр валидатора. Валидатор может использовать более одного формата для проверки совпадения. В конструктор класса необходимо добавить аргумент с именем date_formats - это список допустимых форматов. Аргумент является не обязательным.

    Синтаксис формата совпадает с синтаксисом стандартной библиотеки, использующейся в вашем языке программирования, например, в Python - это модуль datetime.

    Если аргумент date_formats не задан, то валидатор пытается угадать формат сам. Допустимыми для угадывания считаются следующие форматы:
        год-месяц-день (2017-09-01, 2017-09-1, 2017-9-1)
        год-месяц-день часы:минуты (2017-09-01 12:00)
        год-месяц-день часы:минуты:секунды (2017-09-01 12:00:00)
        день.месяц.год (1.9.2017, 1.09.2017, 01.09.2017)
        день.месяц.год часы:минуты (1.9.2017 12:00)
        день.месяц.год часы:минуты:секунды (1.9.2017 12:00:00)
        день/месяц/год (1/9/2017, 1/09/2017, 01/09/2017)
        день/месяц/год часы:минуты (1/9/2017 12:00)
        день/месяц/год часы:минуты:секунды (1/9/2017 12:00:00)

    Реализовать ChainValidator. С его помощью можно объединять валидаторы в цепочку. Если каждый валидатор в цепочке вернул истинное значение, следовательно проверка прошла успешно и валидатор возвращает True. Если хотя бы один валидатор из цепочки вернул ложное значение, то проверка завершилась не удачно и валидатор должен вернуть False. Порядок валидаторов в цепочке должен сохраняться.

    В конструктор класса необходимо добавить обязательный аргумент с именем validators - это список валидаторов.
"""


# Example #1

validator = EMailValidator()
validator.validate('root@localhost') # True


# Example #2

validator = DateTimeValidator(date_formats=['%Y-%m-%d', '%d.%m.%Y'])
validator.validate('2010-05-09') # True
validator.validate('1.7.1999') # True


# Example #3

validator = DateTimeValidator()
validator.validate('1/9/2017 12:00:00') # True


# Example #4

validator = ChainValidator(validators=[EMailValidator(), DateTimeValidator()])
validator.validate('What a you doing, man?!') # False
