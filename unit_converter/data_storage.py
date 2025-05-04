def convert_data_storage(from_unit,to_unit,from_value):
    print("\nData Storage Converter:")
    print("Units:")
    print("1. Bit (bit)")
    print("2. Byte (B)")
    print("3. Kilobyte (KB)")
    print("4. Megabyte (MB)")
    print("5. Gigabyte (GB)")
    print("6. Terabyte (TB)")

    unit_names = {
        1: "Bit (bit)",
        2: "Byte (B)",
        3: "Kilobyte (KB)",
        4: "Megabyte (MB)",
        5: "Gigabyte (GB)",
        6: "Terabyte (TB)"
    }

    # Conversion rates to Byte (base unit)
    units_in_bytes = {
        1: 1 / 8,        # bit to byte
        2: 1,            # byte to byte
        3: 1024,         # KB to bytes
        4: 1024 * 1024,  # MB to bytes
        5: 1024 * 1024 * 1024,  # GB to bytes
        6: 1024 * 1024 * 1024 * 1024  # TB to bytes
    }

   
     

    if from_unit in units_in_bytes and to_unit in units_in_bytes:
        value_in_bytes = from_value * units_in_bytes[from_unit]
        result = value_in_bytes / units_in_bytes[to_unit]

        desc_result = f"{from_value} {unit_names[from_unit]} is equal to {result} {unit_names[to_unit]}"
        short_result = f"{result}"
        return desc_result, short_result
                
    else:
        return "Invalid unit selection. Please choose from the available units."

