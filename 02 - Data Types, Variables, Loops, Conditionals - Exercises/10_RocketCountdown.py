print("🚀 NASA MISSION CONTROL")
print("Initiating launch sequence...")
print("All systems nominal. Begin countdown.")
print()

# Countdown from 10 to 1 using for loop and range
for number in range(10, 0, -1):
    if number == 10:
        print(f"T-minus {number}: Main engine start")
    elif number == 5:
        print(f"T-minus {number}: Go for launch")
    elif number == 3:
        print(f"T-minus {number}: SRB ignition")
    else:
        print(f"T-minus {number}")

print("T-minus 0: LIFTOFF!")
print("🚀 WE HAVE LIFTOFF!")
print("Tower cleared. Vehicle is performing nominally.")
print("Mission Control, Houston - the Eagle has wings!")