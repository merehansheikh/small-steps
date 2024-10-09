def celsius_to_fahrenheit(c):
  c = c*(9/5)
  c = c+32
  return (round(c,1))

def main():
  c = inr(input("Enter temperature in Celsius: "))
  print("Temperature in Fahrenheit:", celsius_to_fahrenheit(c))
main()
