def convert_mass(from_unit, to_unit, from_value):
    print("\nMass/Weight Converter:")
    print("Common Units:")
    print("1. Milligram (mg)")
    print("2. Gram (g)")
    print("3. Kilogram (kg)")
    print("4. Metric Tonne (t)")
    print("5. Ounce (oz)")
    print("6. Pound (lb)")
    print("7. Stone (st)")

    # Conversion rates from kilogram (base unit)
    units_in_kg = {
        1: 0.000001,     # mg to kg
        2: 0.001,        # g to kg
        3: 1,            # kg to kg
        4: 1000,         # tonne to kg
        5: 0.0283495,    # oz to kg
        6: 0.453592,     # lb to kg
        7: 6.35029       # stone to kg
    }

    unit_names = {
        1: "Milligram (mg)",
        2: "Gram (g)",
        3: "Kilogram (kg)",
        4: "Metric Tonne (t)",
        5: "Ounce (oz)",
        6: "Pound (lb)",
        7: "Stone (st)"
    }

    

    if from_unit in units_in_kg and to_unit in units_in_kg:
            value_in_kg = from_value * units_in_kg[from_unit]
            result = value_in_kg / units_in_kg[to_unit]

            desc_result = f"{from_value} {unit_names[from_unit]} is equal to {result} {unit_names[to_unit]}"
            short_result = f"{result}"
            return desc_result, short_result
    else:
        return "Invalid unit selection. Please choose from the available units." 