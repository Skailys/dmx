from time import sleep
import relative


def level1():
    turret = relative.RelativeControl()
    turret.start()

    turret.set_x(128)
    turret.send()
    sleep(1)

    turret.add_x(10)
    turret.send()
    sleep(1)

    turret.add_x(-20)
    turret.send()
    sleep(1)

    turret.add_x(10)
    turret.send()
    sleep(1)

    turret.stop()
    # test: by now, the turret should be back to its original position


def level2():
    turret = relative.RelativeControl()
    turret.start()

    turret.set_y(128)
    turret.send()
    sleep(1)

    turret.add_y(10)
    turret.send()
    sleep(1)

    turret.add_y(-20)
    turret.send()
    sleep(1)

    turret.add_y(10)
    turret.send()
    sleep(1)

    turret.stop()
    # test: by now, the turret should be back to its original position


def level3():
    turret = relative.RelativeControl()
    turret.start()

    turret.set_x(128)
    turret.set_y(128)
    turret.send()
    sleep(1)

    turret.add_x(10)
    turret.add_y(10)
    turret.send()
    sleep(1)

    turret.add_x(-20)
    turret.add_y(-20)
    turret.send()
    sleep(1)

    turret.add_x(10)
    turret.add_y(10)
    turret.send()
    sleep(1)

    turret.stop()
    # test: by now, the turret should be back to its original position


if __name__ == "__main__":
    input("Press Enter to start level 1")
    level1()

    input("Press Enter to start level 2")
    level2()

    input("Press Enter to start level 3")
    level3()

    print("All tests passed!")
