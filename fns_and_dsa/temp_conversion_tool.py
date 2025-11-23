CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9


def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using global factor.
    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using global factor.
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


def main():
    temp_input = input("Enter the temperature to convert: ")

    try:
        temp_value = float(temp_input)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    unit = input(
        "Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        converted = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {converted}°C")
    elif unit == 'C':
        converted = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {converted}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


if __name__ == "__main__":
    main()
