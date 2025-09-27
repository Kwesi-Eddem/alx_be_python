FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    temp_in_celsius = (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return temp_in_celsius

def convert_to_fahrenheit(celsius):
    temp_in_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return temp_in_fahrenheit

inputValue = float(input("Enter the temperature to convert: "))
temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

match temp_type.upper():
    case 'F':
        print(f"{inputValue}°F is {convert_to_celsius(inputValue)}°C")
    case 'C':
        print(f"{inputValue}°C is {convert_to_fahrenheit(inputValue)}°F")
    case _:
        print()
