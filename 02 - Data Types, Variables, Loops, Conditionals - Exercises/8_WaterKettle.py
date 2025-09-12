# Water Kettle Simulation
# A simple program that simulates heating water in a kettle until it reaches boiling point.

# Starting conditions
temperature = 20  # Room temperature in Celsius
boiling_point = 100  # Water boils at 100°C
heating_increment = 10  # Degrees to increase each cycle

print("Water Kettle Simulation")
print(f"Starting temperature: {temperature}°C")

# Heat the water until it reaches boiling point
while temperature < boiling_point:
    temperature += heating_increment

    if temperature <= 25:
        status = "Cool"
    elif temperature <= 40:
        status = "Getting warm"
    elif temperature <= 65:
        status = "Hot"
    elif temperature < 100:
        status = "Almost boiling!"
    else:
        status = "Boiling!"

    print(f"Heating... Current temperature: {temperature}°C - {status}")

# Kettle automatically turns off when water boils
print("Kettle has reached boiling point! Turning off...")
print("Your water is ready! 🫖")
