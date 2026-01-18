import sys

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":

    if len(sys.argv) > 1:
        c = float(sys.argv[1])          # Parameterized input
    else:
        user_input = input("Enter temperature in Celsius: ")
        if user_input:
            c = float(user_input)       # User input
        else:
            c = 25.0                    # Default value

    print("Fahrenheit:", celsius_to_fahrenheit(c))