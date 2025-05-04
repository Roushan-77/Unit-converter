def convert_pressure(from_unit, to_unit, from_value):
    print("\nPressure Converter:")
    print("Units:")
    print("1. Pascal (Pa)")
    print("2. Bar")
    print("3. Atmosphere (atm)")
    print("4. mmHg")
    print("5. psi")

    unit_names = {
        1: "Pascal (Pa)",
        2: "Bar",
        3: "Atmosphere (atm)",
        4: "mmHg",
        5: "psi"
    }

    # Conversion rates to Pascals (base unit)
    units_in_pascals = {
        1: 1,              # Pascal to Pascal
        2: 100000,         # Bar to Pascal
        3: 101325,         # Atmosphere to Pascal
        4: 133.322,        # mmHg to Pascal
        5: 6894.76         # psi to Pascal
    }


    if from_unit in units_in_pascals and to_unit in units_in_pascals:
        value_in_pascals = from_value * units_in_pascals[from_unit]
        result = value_in_pascals / units_in_pascals[to_unit]
        
        desc_result = f"{from_value} {unit_names[from_unit]} is equal to {result} {unit_names[to_unit]}"
        short_result = f"{result}"
        return desc_result, short_result
                
    else:
         return "Invalid unit selection. Please choose from the available units."
