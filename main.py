import json

from car import Toyota

if __name__ == '__main__':
    file = open("./database/garage.json", 'r')
    data_in_json = file.read()
    data = json.loads(data_in_json)
    cars_garage = {}
    for element in data:
        for id in element.keys():
            new_car = Toyota(element[id]["name"], element[id]["engine"], element[id]["transmission"], element[id]["color"])
            cars_garage[id] = new_car
    while True:
        print("1. Create new car\n" +
              "2. Get all cars\n" +
              "3. Driving\n" +
              "4. Change color \n" +
              "0. Quit"
              )
        flag = int(input("Choose menu item: "))
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
                print("car id:", str(key), " -> ", cars_garage[key])
                print("*" * 40)
        elif flag == 3:
            for key in cars_garage.keys():
                print("car id: ", str(key), " -> ", cars_garage[key])
            car_drive_id = input("Enter car id: ")
            speed = int(input("Enter speed your car: "))
            up_down = input("Set speed input 'up' when braking input 'down: ")
            cars_garage[car_drive_id].drive(speed, up_down)
            print(cars_garage[car_drive_id])
        elif flag == 4:
            for key in cars_garage.keys():
                print("car id: ", str(key), " -> ", cars_garage[key])
            car_id = input("Enter car id: ")
            ss = cars_garage[car_id].color
            new_color = input("Input new color: ")
            cars_garage[car_id].color = new_color
            print(cars_garage[car_id])
        elif flag == 0:
            garage =[]
            for key in cars_garage.keys():
                print("car id: ", str(key), " -> ", cars_garage[key])
                car = {key: cars_garage[key].generate_dict()}
                garage.append(car)
            file = open("./database/garage.json", 'w')
            data_json = json.dumps(garage)
            file.write(data_json)
            file.close()
            print("Goodbye")
            break
