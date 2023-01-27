import math

## Parallel combination function 
def parallel(resistances):
    total_resistance = 0
    for resistors in resistances:
        total_resistance += 1/resistors
    return 1/total_resistance

arr = [330, 1000, 2200]
print(parallel(arr))

 
## Potential divider function below:
def potential_divider(voltage, resistors):
    voltage_drop = []
    total_resistance = sum(resistors)
    for values in resistors:
        voltage_drop.append((values /total_resistance)*voltage)
    return voltage_drop

print(potential_divider(9, [3000,1000]))


## Temperature check function:
def temperature_check(temperature, unit):
    if unit == 'C':
        if temperature < 35:
            print("The patient is hypothermic.")
        elif temperature > 38:
            print("The patient is hyperthermic.")
        else:
            print("The patient has normal body temperature.")
    elif unit == 'F':
        if temperature < 95:
            print("The patient is hypothermic.")
        elif temperature > 100.4:
            print("The patient is hyperthermic.")
        else:
            print("The patient has normal body temperature.")
    else:
        print("Please enter 'C' for Celsius or 'F' for Fahrenheit.")

print(temperature_check(65,"F"))