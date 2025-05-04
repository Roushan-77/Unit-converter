def convert_area(from_unit, to_unit, from_value):
    print("\nArea Converter:")
    print("Units:")
    print("1. Square meter (m²)")
    print("2. Square kilometer (km²)")
    print("3. Square foot (ft²)")
    print("4. Square yard (yd²)")
    print("5. Acre")
    print("6. Hectare")

    unit_names = {
        1: "Square meter (m²)",
        2: "Square kilometer (km²)",
        3: "Square foot (ft²)",
        4: "Square yard (yd²)",
        5: "Acre",
        6: "Hectare"
    }

    # All conversions to Square Meters (base unit)
    units_in_square_meters = {
        1: 1,               # m²
        2: 1e6,             # km²
        3: 0.092903,        # ft²
        4: 0.836127,        # yd²
        5: 4046.86,         # acre
        6: 10000            # hectare
    }

    

    if from_unit in units_in_square_meters and to_unit in units_in_square_meters:
        value_in_square_meters = from_value * units_in_square_meters[from_unit]
        result = value_in_square_meters / units_in_square_meters[to_unit]

        desc_result = f"{from_value} {unit_names[from_unit]} is equal to {result} {unit_names[to_unit]}"
        short_result = f"{result}"
        return desc_result, short_result
                
    else:
        return "Invalid unit selection. Please choose from the available units."

