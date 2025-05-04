def Convert_temperature(from_unit, to_unit, from_value):
    print("\nTemperature Converter:")
    print("Common Units:")
    print("1. Celsius (°C)")
    print("2. Fahrenheit (°F)")
    print("3. Kelvin (K)")

    unit_names = {
        1: "Celsius (°C)",
        2: "Fahrenheit (°F)",
        3: "Kelvin (K)"
    }

    result = None

    if from_unit == to_unit:
        result = from_value
    elif from_unit == 1 and to_unit == 2:
        result = (from_value * 9 / 5) + 32  # Celsius to Fahrenheit
    elif from_unit == 1 and to_unit == 3:
        result = from_value + 273.15        # Celsius to Kelvin
    elif from_unit == 2 and to_unit == 1:
        result = (from_value - 32) * 5 / 9  # Fahrenheit to Celsius
    elif from_unit == 2 and to_unit == 3:
        result = (from_value - 32) * 5 / 9 + 273.15  # Fahrenheit to Kelvin
    elif from_unit == 3 and to_unit == 1:
        result = from_value - 273.15        # Kelvin to Celsius
    elif from_unit == 3 and to_unit == 2:
        result = (from_value - 273.15) * 9 / 5 + 32  # Kelvin to Fahrenheit

    if result is not None:
        desc_result = f"{from_value} {unit_names[from_unit]} is equal to {result} {unit_names[to_unit]}"
        short_result = f"{result}"
        return desc_result, short_result
    else:
        return "Invalid unit selection. Please choose from the available units."

                

            