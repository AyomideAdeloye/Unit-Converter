def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        "meters": 1,
        "kilometers": 0.001,
        "miles": 0.000621371,
        "feet": 3.28084,
        "inches": 39.3701
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        "newtons": 1,
        "pounds-force": 0.224809,
        "kilogram-force": 0.101972
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def mass_converter(value, from_unit, to_unit):
    conversion_factors = {
        "grams": 1,
        "kilograms": 0.001,
        "tons": 0.000001,
        "amu": 6.022e23
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) +32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) *5/9
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    else:
        return value
    
def speed_converter(value, from_unit, to_unit):
     conversion_factors = {
          "m/s": 1,
          "km/h": 3.6,
          "mph": 2.23694,
          "knots": 1.94384
     }
     return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def time_converter(value, from_unit, to_unit):
     conversion_factors = {
          "seconds": 1,
          "minutes": 1/60,
          "hours": 1/3600,
          "days": 1/86400
     }
     return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def energy_converter(value, from_unit, to_unit):
     conversion_factors = {
          "joules": 1,
          "calories": 0.239006,
          "kilowatt_hours": 0.000000277778
     }
     return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def volume_converter(value, from_unit, to_unit):
     conversion_factors = {
          "liters": 1,
          "milliliters": 1000,
          "cubic_meters": 0.001,
          "gallons": 0.264172,
          "cups": 4.22675
     }
     return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def main():
    categories = {
        "1": "Length",
        "2": "Weight",
        "3": "Mass",
        "4": "Temperature",
        "5": "Speed",
        "6": "Time",
        "7": "Energy",
        "8": "Volume"
    }

    print("Thank you for choosing this Unit Converter!")
    print("Select a category: ")
    for key, value in categories.items():
         print(f"{key}: {value}")
    
    category_choice = input("\nEnter the number of choice: ")

    if category_choice == "1":
            units = ["meters", "kilometers", "miles", "feet", "inches"]
            converter = length_converter
    elif category_choice == "2":
            units = ["newtons", "pounds-force", "kilogram-force"]
            converter = weight_converter
    elif category_choice == "3":
            units = ["grams", "kilograms", "tons", "amu"]
            converter = mass_converter
    elif category_choice == "4":
            units = ["celsius", "fahrenheit", "kelvin"]
            converter = temperature_converter
    elif category_choice == "5":
            units = ["m/s", "km/h", "mph", "knots"]
            converter = speed_converter
    elif category_choice == "6":
            units = ["seconds", "minutes", "hours", "days"]
            converter = time_converter
    elif category_choice == "7":
            units = ["joules", "calories", "kilowatts_hours"]
            converter = energy_converter
    elif category_choice == "8":
            units = ["liters", "milliliters", "cubic_meters", "gallons", "cups"]
            converter = volume_converter
    else:
            print("Inavlid choice. Please enter the categories: 1, 2, 3, or 4.")
            return
    
    print("\nAvailable units:", ", ".join(units))
    from_unit = input("Enter the unit you want to convert from: ").strip().lower()
    to_unit = input("Enter the unit you want to convert to: ").strip().lower()

    try:
         value = float(input("Enter the value to convert: "))
         result = converter(value, from_unit, to_unit)
         print(f"\n {value} {from_unit} is equal to {round(result, 4)} {to_unit}")
    except ValueError:
         print("Invalid number entered. Try again.")

if __name__ == "__main__":
     main()