
class Toyota:
    __current_speed = 0
    __current_gear = 0

    def __init__(self, name, engine, transmission, color):
        self.name = name
        self.engine = engine
        self.transmission = transmission
        self.color = color


    def __str__(self):
        car_detail = ("Car " + self.name + ":\n"
                    "\tengine: " + str(self.engine) + " ltr., " +
                    "\ttransmission: " + self.transmission + ", "
                    "\tcolor: " + self.color + ", " +
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
        if self.transmission == "manual":
            self.__current_gear = int(input("Input needed transmission gear: "))
        elif self.transmission == "auto":
            if self.__current_speed == 0:
                self.__current_gear = 0
            elif self.__current_speed <= 30:
                self.__current_gear = 1
            elif self.__current_speed <= 50:
                self.__current_gear = 2
            elif self.__current_speed <= 65:
                self.__current_gear = 3
            elif self.__current_speed > 80:
                self.__current_gear = 4

    def change_color(self, color):
        self.color = color
