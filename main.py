class Vehicle:
    __COLOR_VARIANTS = ('red', 'black', 'white', 'silver', 'green')

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner  # владелец транспорта. (владелец может меняться)
        self.__model = __model  # модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = __engine_power  # мощность двигателя. (мы не можем менять мощность двигателя
        # самостоятельно)
        self.__color = __color  # название цвета. (мы не можем менять цвет автомобиля своими руками)

    def get_model(self):
        return f'модель {self.__model}'

    def get_horsepower(self):
        return f'мощность двигателя  {self.__engine_power}'

    def get_color(self):
        return f' цвет {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f' владелец {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
             print(f' нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    # (в седан может поместиться только 5 пассажиров)


# Текущие цвета __COLOR_VARIANTS = ['red', 'black', 'white', 'silver', 'green']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'silver')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
