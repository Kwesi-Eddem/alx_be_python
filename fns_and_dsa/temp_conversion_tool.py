FARENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FARENHEIT_FACTOR = 9/5

def convert_to_celcius(farenheit):
    temp_in_celcius = (farenheit-32) * FARENHEIT_TO_CELSIUS_FACTOR
    return temp_in_celcius

def convert_to_farenheit(celcius):
    temp_in_farenheit = (celcius * CELSIUS_TO_FARENHEIT_FACTOR) + 32
    return temp_in_farenheit

inputValue = float(input("Enter the temperature to convert: "))
temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

match temp_type.upper():
    case 'F':
        print(f"{inputValue}°F is {convert_to_celcius(inputValue)}°C")
    case 'C':
        print(f"{inputValue}°C is {convert_to_farenheit(inputValue)}°F")
    case _:
        print()
