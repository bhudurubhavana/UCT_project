print("================================")
print("        UNIT CONVERTER")
print("================================")

print("\n1. Length")
print("2. Weight")
print("3. Temperature")
print("4. Time")
print("5. Volume")

choice = input("\nEnter your choice: ")

# Length Converter
if choice == "1":
    print("\n--- Length Converter ---")
    print("1. Meter to Kilometer")
    print("2. Kilometer to Meter")
    print("3. Meter to Centimeter")
    print("4. Centimeter to Meter")
    print("5. Kilometer to Miles")
    print("6. Miles to Kilometer")

    conversion = input("\nEnter conversion: ")
    value = float(input("Enter value: "))

    if conversion == "1":
        result = value / 1000
        print("Result:", result, "km")

    elif conversion == "2":
        result = value * 1000
        print("Result:", result, "m")

    elif conversion == "3":
        result = value * 100
        print("Result:", result, "cm")

    elif conversion == "4":
        result = value / 100
        print("Result:", result, "m")

    elif conversion == "5":
        result = value * 0.621371
        print("Result:", result, "miles")

    elif conversion == "6":
        result = value / 0.621371
        print("Result:", result, "km")

    else:
        print("Invalid conversion choice!")
 


# Weight Converter
elif choice == "2":
    print("\n--- Weight Converter ---")
    print("1. Kilogram to Gram")
    print("2. Gram to Kilogram")
    print("3. Kilogram to Pound")
    print("4. Pound to Kilogram")

    conversion = input("\nEnter conversion: ")
    value = float(input("Enter value: "))

    if conversion == "1":
        result = value * 1000
        print("Result:", result, "grams")

    elif conversion == "2":
        result = value / 1000
        print("Result:", result, "kg")

    elif conversion == "3":
        result = value * 2.20462
        print("Result:", result, "pounds")

    elif conversion == "4":
        result = value / 2.20462
        print("Result:", result, "kg")

    else:
        print("Invalid conversion choice!")
# Temperature Converter
elif choice == "3":
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    conversion = input("\nEnter conversion: ")
    value = float(input("Enter temperature: "))

    if conversion == "1":
        result = (value * 9/5) + 32
        print("Result:", result, "°F")

    elif conversion == "2":
        result = (value - 32) * 5/9
        print("Result:", result, "°C")

    elif conversion == "3":
        result = value + 273.15
        print("Result:", result, "K")

    elif conversion == "4":
        result = value - 273.15
        print("Result:", result, "°C")

    else:
        print("Invalid conversion choice!")


