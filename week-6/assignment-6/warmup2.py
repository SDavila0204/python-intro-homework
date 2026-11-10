#convers cel to fah
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

#converts fah to cel
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

#prints out conversions
print(f"0 degrees celsius equals {celsius_to_fahrenheit(0):.1f} degrees fahrenheit")
print(f"80 degrees celsius equals {celsius_to_fahrenheit(80):.1f} degrees fahrenheit")
print(f"32 degrees fahrenheit equals {fahrenheit_to_celsius(32):.1f} degrees celsius")
