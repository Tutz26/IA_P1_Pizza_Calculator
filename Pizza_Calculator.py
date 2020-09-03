import math


# Welcome message.
print("Welcome to the Tutzis pizza calculator")

# Ask for Inputs!
centimeterFloat = float(input("Please type the pizza diameter in centimeters and press enter!."))
pizzaCostFloat = float(input ("Please type your pizza price in mexican pesos and press enter!."))

# Calculate Pizza area.
pizzaRadiusFloat = centimeterFloat/2
pizzaAreaFloat = math.pi *pizzaRadiusFloat * pizzaRadiusFloat
pizzaPricePerCmFloat = pizzaCostFloat/pizzaAreaFloat

# Print value
print(f"Your pizza area is {pizzaAreaFloat} cm^2")
print(f"Your pizza value is: ${pizzaPricePerCmFloat}/cm^2")


def StandBy():
    pass

