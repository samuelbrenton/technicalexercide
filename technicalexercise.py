SIGMA = 3.41e-10 # Metres
EPSILON = 1.65e-21 # Joules  

# Example distance
r = 6.82e-10

# Formula
repulsion = (SIGMA / r) ** 12 # the left hand fraction between the square brackets
attraction = (SIGMA / r) ** 6 # the right hand fraction between the square brackets
u = 4 * EPSILON * (repulsion - attraction)

# Check formula works
print(u)

# Formatted to match example 
formatted_u = "{:.1e}".format(u)
print(formatted_u)

# Package into a function
def lennard_jones(r) -> float:
    repulsion = (SIGMA / r) ** 12 
    attraction = (SIGMA / r) ** 6
    return 4 * EPSILON * (repulsion - attraction)

# List of distances (as floats) provided
distances = [4.1e-10, 2e-10, 3.41e-10]

# Sum of the lennard jones output for each distance 
binding_energy = sum([lennard_jones(distance) for distance in distances])
print(binding_energy)
