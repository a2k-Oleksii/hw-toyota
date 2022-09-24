from car import Toyota

if __name__ == '__main__':
    yaris = Toyota(1.3, "auto", "red")
    camry = Toyota(2.0, "auto", "white")
    eclips = Toyota(3.0, "manual", "black")

    print(eclips)
    print(camry)
    print(yaris)
    print("*" * 40)
    camry.change_color("blue")
    yaris.drive(90, "up")
    eclips.drive(140, "up")
    print(eclips)
    print(camry)
    print(yaris)
    print("*" * 40)
    camry.drive(32, "up")
    yaris.drive(190, "down")
    eclips.drive(92, "down")
    print(eclips)
    print(camry)
    print(yaris)
