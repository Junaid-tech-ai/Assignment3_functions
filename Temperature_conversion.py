# # Implement the following integer functions:
# # i. A Function Celsius that returns the Celsius equivalent of a Fahrenheit temperature.
# # ii. A Function Fahrenheit returns the Fahrenheit equivalent of a Celsius temperature.
# # iii. Use these functions to write a program that prints charts showing the Fahrenheit
# # equivalents of all Celsius temperatures from 0 to 100 degrees, and the Celsius equivalents
# # of all Fahrenheit temperatures from 32 to 212 degrees. Print the outputs in a tabular format
# # that minimizes the number of lines of output while remaining readable.
#
#

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def print_temperature_chart():
    print("Celsius to Fahrenheit Conversion Chart:")
    print("Celsius\tFahrenheit")
    for celsius in range(0, 101):
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}\t{fahrenheit}")

    print("\nFahrenheit to Celsius Conversion Chart:")
    print("Fahrenheit\tCelsius")
    for fahrenheit in range(32, 213):
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}\t{celsius}")


print_temperature_chart()
