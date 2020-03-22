class Cat:

    def __init__(self, age):
        age = input("Print age of your cat")
        self.age = (age)

    def _set_average_speed(self):
        if self.age <= 7 :
            return 12
        elif self.age > 7 and self.age <= 10:
            return 9
        elif self.age >= 10:
            return 6

    def _set_saturation_level(self):
        saturation_level = 50
        self._set_saturation_level = saturation_level


    def _reduce_saturation_level(self, value):
        self._set_saturation_level= self._set_saturation_level - value
        if self._set_saturation_level < 0:
            return 0

    def _increase_saturation_level(self, value):
        self._set_saturation_level = self._set_saturation_level + value
        if self._set_saturation_level >= 100:
            return 100

    def eat(self, product):
        if product == "fodder":
            self._increase_saturation_level(value=10)
        elif product == "apple":
            self._increase_saturation_level(value=5)
        elif product == "milk":
            self._increase_saturation_level(value=2)

    def run(self, hours):
        hours = input("Which time in hours will run this animal?")
        ran_km = self._set_average_speed * hours
        if ran_km <= 25:
            self._reduce_saturation_level(value=2)
        elif ran_km > 25 and ran_km <= 50:
            self._reduce_saturation_level(value=5)
        elif ran_km > 50 and ran_km <= 100:
            self._reduce_saturation_level(value=15)
        elif ran_km >100 and ran_km <= 200:
            self._reduce_saturation_level(value=50)
        return f"Your cat ran {ran_km} kilometers"

    def get_saturation_level(self):
        return self._set_saturation_level
        if self._set_saturation_level == 0:
            return "Your cat is dead :("

    def get_average_speed(self):
        return self._set_average_speed

class Cheetah (Cat):
    def eat(self, product):
        product = input("What would eat a Cheetah? gazelle/rabbit")
        if product == "gazelle":
            self._increase_saturation_level(value=30)
        elif product == "rabbit":
            self._increase_saturation_level(value=15)

    def _set_average_speed(self):
        if self.age <= 5 :
            average_speed = 90
        elif self.age > 5 and self.age <= 15:
            average_speed = 75
        else: average_speed = 40
        self._set_average_speed = average_speed

class Wall:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def wall_square(self):
        self.wall_square = self.height * self.width


    def number_of_rolls_of_wallpaper(self, roll_width_m, roll_length_m):
        count_of_lines_in_roll = roll_length_m % self.height
        count_of_lines = self.width % roll_width_m
        self.number_of_rolls_of_wallpaper = count_of_lines / count_of_lines_in_roll

class Roof:
    def __init__(self, width, height, roof_type):
        self.width = width
        self.height = height
        self.roof_type = roof_type

    def roof_square(self):
        if self.roof_type == "gable":
            self.roof_square = (self.height * self.width) * 2
        elif self.roof_type == "single-pitch":
            self.roof_square = (self.height * self.width)
        square_of_the_roof = self.roof_type
        return square_of_the_roof

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def window_square(self):
        self.window_square = self.width * self.height

class Door:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def door_square(self):
        self.door_square =  self.height * self.width


    def door_price(self, material):
        wood_price = 10
        metal_price = 3
        self.wood_price = wood_price
        self.metal_price = metal_price
        if material == "wood":
            self.door_price = wood_price * self.door_square
        elif material == "metal":
            self.door_price = metal_price * self.door_square
        else:
            raise ValueError
            print ("Sorry we don't have such material")

    def update_wood_price(self, new_price):
        self.wood_price = new_price

    def update_metal_price(self, new_price):
        self.metal_price = new_price

class House:
    def __init__(self):
        self.__walls = []
        self.__windows = []
        self.__roof = None
        self.__door = None

    def create_wall(self, width, height):
        try:
            if self.__walls.__len__() ==4:
                raise ValueError ("Our house can not have more than 4 walls")
            elif not width or not height:
                raise ValueError('Value must be not 0')
        except ValueError:
            raise
        self.__walls.append(Wall(width, height))

    def create_door(self, width, height):
        try:
            if self.__door:
                raise ValueError('The house can not have two doors')
            elif not width or not height:
                raise ValueError('Value must be not 0')
        except ValueError:
            raise
        else:
            self.__door = Door(width, height)

    def get_count_of_walls(self):
        return self.__walls.__len__()

    def get_count_of_windows(self):
        return self.__windows.__len__()

    def get_door_price(self, material):
        return self.__door.door_price(material)

    def update_wood_price(self, new_wood_price):
        self.__door._wood_price = new_wood_price

    def update_metal_price(self, new_metal_price):
        self.__door._metal_price = new_metal_price

    def get_roof_square(self):
        return self.__roof.roof_square()

    def get_walls_square(self):
        sum_of_all_walls_square = 0
        for wall in self.__walls:
            sum_of_all_walls_square += wall.wall_square()
        return sum_of_all_walls_square

    def get_windows_square(self):
        sum_of_all_windows_square = 0
        for window in self.__windows:
            sum_of_all_windows_square += window.window_square()
        return sum_of_all_windows_square

    def get_door_square(self):
        return self.__door.door_square()

    def get_number_of_rolls_of_wallpapers(self, roll_width_m, roll_length_m):
        try:
            if not roll_width_m or not roll_length_m:
                raise ValueError('Sorry length must be not 0')
        except ValueError:
            raise
        else:
            rolls_for_all_our_walls = 0
            for wall in self.__walls:
                rolls_of_wallpaper_for_current_wall = wall.number_of_rolls_of_wallpaper(roll_width_m, roll_length_m)
                rolls_for_all_our_walls += rolls_of_wallpaper_for_current_wall
            return rolls_for_all_our_walls

    def get_room_square(self):
        return self.get_walls_square() - self.get_windows_square() - self.get_door_square()