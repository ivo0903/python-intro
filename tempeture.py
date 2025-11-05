def Fahrenheit_to_Celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0/9.0
    return celsius 

print(Fahrenheit_to_Celsius(100))


# Temperature Converter

# Prompt the user for input
celsius = float(input("Enter the temperature in Celsius: "))

# Absolute zero check
if celsius < -273.15:
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    # Convert to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equivalent to {fahrenheit}°F")
