#convers cel to fah
def cel_to_fah(celsius):
    return (celsius * 9/5) + 32

#converts fah to cel
def fah_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9

#prints out conversions
print(f"0 degrees celsius equals {cel_to_fah(0):.1f} degrees fahrenheit")
print(f"80 degrees celsius equals {cel_to_fah(80):.1f} degrees celsius")
print(f"32 degrees fahrenheit equals {fah_to_cel(32):.1f} degrees fahrenheit")
