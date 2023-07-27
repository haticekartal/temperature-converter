choose = int(input("1.Celcius to Fahrenheit\n 2.Celcius to Kelvin\n 3.Fahrenheit to Celcius\n 4.Fahrenheit to Kelvin\n 5.Kelvin to Fahrenheit\n 6.Kelvin to Celcius"))

# Celcius to Fahrenheit
if choose == 1:
    c = int(input("enter temperature in celcius: "))
    def fahrenheit(celcius):
        return (celcius * 9 / 5 + 32)
    temp = fahrenheit(c)
    print(f"{c}°C = {temp}F°")

# Celcius to Kelvin
elif choose == 2:
    c = int(input("enter temperature in celcius: "))
    def kelvin(celcius):
        return (celcius + 273.75)
    temp = kelvin(c)
    print(f"{c}°C = {temp}°K")

# Fahrenheit to Celcius
elif choose == 3:
    f = int(input("enter temperature in fahrenheit: "))
    def celcius(fahrenheit):
        return (f - 32) * (5 / 9)
    temp = celcius(f)
    print(f"{f}°F = {temp}°C")

# Fahrenheit to Kelvin
elif choose == 4:
    f = int(input("enter temperature in fahrenheit: "))


    def kelvin(fahrenheit):
        return (f + 459.67) * (5 / 9)


    temp = kelvin(f)
    print(f"{f}°F = {temp}°F")

# Kelvin to Fahrenheit
elif choose == 5:
    k = int(input("enter temperature in kelvin: "))
    def fahrenheit(kelvin):
        return (k * (9 / 5) - 459.67)
    temp = fahrenheit(k)
    print(f"{k}°K = {temp}°F")

# Kelvin to Celcius
elif choose == 6:
    k = int(input("enter temperature in kelvin: "))
    def celcius(kelvin):
        return (k - 273.75)
    temp = celcius(k)
    print(f"{k}°K = {temp}°C")

else:
    print("please choose from 1-6")






