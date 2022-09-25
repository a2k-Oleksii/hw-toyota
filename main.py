from car import Toyota

if __name__ == '__main__':
    cars_garage = {}
    while True:
        print("1. Create new car\n" +
              "2. Get all cars\n" +
              "3. Driving\n" +
              "4. Change color \n" +
              "0. Quit"
              )
        flag = int(input("Choose menu item:"))
        if flag == 1:
            name = input("Model car: ")
            engine = input("Engine volume: ")
            transmission = input("Type transmission (manual or auto): ")
            color = input("Color car: ")
            car = Toyota(name, engine, transmission, color)
            if len(cars_garage) > 0:
                id = len(cars_garage) + 1
                cars_garage[id] = car
            else:
                cars_garage[1] = car
        elif flag == 2:
            for key in cars_garage.keys():
                print(cars_garage[key])
        elif flag == 3:
            for key in cars_garage.keys():
                print("car id: " + str(key) + " -> " + cars_garage[key].__str__())
            car_drive_id = int(input("Enter car id: "))
            speed = int(input("Enter speed your car: "))
            up_down = input("Set speed input 'up' when braking input 'down: ")
            cars_garage[car_drive_id].drive(speed, up_down)
            print(cars_garage[car_drive_id])
        elif flag == 4:
            for key in cars_garage.keys():
                print("car id: " + str(key) + " -> " + cars_garage[key].__str__())
            car_drive_id = int(input("Enter car id: "))
            new_color = input("Input new color: ")
            cars_garage[car_drive_id].change_color(new_color)
            print(cars_garage[car_drive_id])
        elif flag == 0:
            print("Goodbye")
            break
