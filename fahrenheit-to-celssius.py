def fahrenheit_to_celsius(f):
  f = f-32
  f = f*5
  f = round((f/9),1)
  return f

def main():
  f = inr(input("Enter temperature in Fahrenheit: "))
  print("Temperature in Celsius:", fahrenheit_to_celsius(f))
main()
