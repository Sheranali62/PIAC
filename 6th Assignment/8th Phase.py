def convert_celsius_to_fahrenheit(celsius_list):
    fahrenheit_list = []
    index = 0
    while index < len(celsius_list):
        celsius_temp = celsius_list[index]
        fahrenheit_temp = (celsius_temp * 9/5) + 32
        fahrenheit_list.append(fahrenheit_temp)
        index += 1
    return fahrenheit_list

def main():
    celsius_input = input("Enter temperatures in Celsius separated by commas (e.g., 20, 25, 30): ")
    celsius_list = [float(temp.strip()) for temp in celsius_input.split(',')]
    
    fahrenheit_list = convert_celsius_to_fahrenheit(celsius_list)
    
    print("Temperatures in Fahrenheit:", fahrenheit_list)

if __name__ == "__main__":
    main()
