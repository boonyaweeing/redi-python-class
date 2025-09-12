has_degree = True
years_experience = 3
speaks_english = True
has_drivers_license = False

if has_degree and years_experience >= 2:
    print("Qualified for Senior role")
elif has_degree or years_experience >= 5:
    print("Qualified for Junior role")
else:
    print("Not qualified")

if speaks_english and (has_degree or years_experience >= 3):
    print("Eligible for international projects")

if has_drivers_license or speaks_english:
    print("Can work in field operations")
