
class Toyota:
    __current_speed = 0
    __current_gear = 0

    def __init__(self, name, engine, transmission, color):
        self.__name = name
        self.__engine = engine
        self.__transmission = transmission
        self.__color = color

    def generate_dict(self):
        new_dict = {"name": self.__name, "engine": self.__engine, "transmission": self.__transmission, "color": self.__color}
        return new_dict

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    def __str__(self):
        car_detail = ("Car " + self.__name + ":\n"
                    "\tengine: " + str(self.__engine) + " ltr., " +
                    "\ttransmission: " + self.__transmission + ", "
                    "\tcolor: " + self.__color + ", " +
                      "\tcurrent speed: " + str(self.__current_speed) + " km/h, " +
                      "\tcurrent transmission gear: " + str(self.__current_gear))
        return car_detail

    def drive(self, speed, up_down):
        # Car cannot drive more than 200 km/h.
        # When driving input 'up' when braking input 'down'
        if up_down == "up":
            if self.__current_speed + speed > 200:
                self.__current_speed = 200
                self.shift_gear()
            else:
                self.__current_speed += speed
                self.__shift_gear()
        elif up_down == "down":
            if self.__current_speed - speed < 0:
                self.__current_speed = 0
                self.__shift_gear()
            else:
                self.__current_speed -= speed
                self.__shift_gear()

    def __shift_gear(self):
        # When transmission manual number gear input user
        # when transmission automatic number gear set automatic
        if self.__transmission == "manual":
            self.__current_gear = int(input("Input needed transmission gear: "))
        elif self.__transmission == "auto":
            if self.__current_speed == 0:
                self.__current_gear = 0
            elif self.__current_speed <= 30:
                self.__current_gear = 1
            elif self.__current_speed <= 50:
                self.__current_gear = 2
            elif self.__current_speed <= 65:
                self.__current_gear = 3
            elif self.__current_speed <= 80:
                self.__current_gear = 4
            else:
                self.__current_gear = 5
