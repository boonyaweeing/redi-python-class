def initialize():
    print("NASA MISSION CONTROL")
    print("Initiating launch sequence...")
    print("All systems nominal. Begin countdown")

def liftoff():
    print("T-minus 0: LIFTOFF!")
    print("We have liftoff!")
    print("Tower cleared. Vehicle is performing nominally.")
    print("Mission Control, Houston - the Eagle has wings!")

def engine_start(countdown):
    for number in range(countdown, 0, -1): #decrement by 1
        if number == 10:
            print(f"T-minus {number}: Main engine start")
        elif number == 5:
            print(f"T-minus {number}: Go for launch")
        elif number == 3:
            print(f"T-minus {number}: SRB ignition")
        else:
            print(f"T-minus {number}")

initialize()
engine_start(100)
liftoff()


"""
def engine_start(countdown):
    for number in range(countdown, 0, -1):
        if number == 10:
            print(f"T-minus {number}: Main engine start")
        elif number == 5:
            print(f"T-minus {number}: Go for launch")
        elif number == 3:
            print(f"T-minus {number}: SRB ignition")
        else:
            print(f"T-minus {number}")


def initialize():
    print("🚀 NASA MISSION CONTROL")
    print("Initiating launch sequence...")
    print("All systems nominal. Begin countdown.")


def lift_off():
    print("T-minus 0: LIFTOFF!")
    print("🚀 WE HAVE LIFTOFF!")
    print("Tower cleared. Vehicle is performing nominally.")
    print("Mission Control, Houston - the Eagle has wings!")


initialize()
engine_start(100)
lift_off()

"""