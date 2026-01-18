import sys

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":

    if len(sys.argv) > 1:
        c = float(sys.argv[1])   # Jenkins / CLI parameter
    else:
        c = 25.0                 # Default value

    print("Fahrenheit:", celsius_to_fahrenheit(c))
