def Convert_speed(from_unit, to_unit, from_value):
    print("\nSpeed Converter:")
    print("Units:")
    print("1. Meters per second (m/s)")
    print("2. Kilometers per hour (km/h)")
    print("3. Miles per hour (mph)")
    print("4. Knots")

    unit_names = {
        1: "Meters per second (m/s)",
        2: "Kilometers per hour (km/h)",
        3: "Miles per hour (mph)",
        4: "Knots"
    }

    # Conversion factors to meters per second (base unit)
    units_in_mps = {
        1: 1,                   # m/s
        2: 1000 / 3600,         # km/h
        3: 1609.34 / 3600,      # mph
        4: 1852 / 3600          # knots
    }



    if from_unit in units_in_mps and to_unit in units_in_mps:
        value_in_mps = from_value * units_in_mps[from_unit]
        result = value_in_mps / units_in_mps[to_unit]
                
        desc_result = f"{from_value} {unit_names[from_unit]} is equal to {result} {unit_names[to_unit]}"
        short_result = f"{result}"
        return desc_result, short_result
                
    else:
         return "Invalid unit selection. Please choose from the available units."
