import pandas as pd

# Load the dataset
data = pd.read_csv('Periodic Table data.csv')

def get_element_properties(atomic_number):
    """
    Function to look up element properties based on atomic number.

    Args:
    - atomic_number: The atomic number of the element

    Returns:
    - All properties of the specified element
    """
    element_properties = data[data['AtomicNumber'] == atomic_number].iloc[0]
    return element_properties

# Display the periodic table
symbol = data['Symbol']
AtomicNumber = data['AtomicNumber']
period = data['Period']

print(symbol[0], end=" ")
for _ in range(16):
    print("   ", end="")
print(symbol[1])

a = 2
for _ in range(2):
    for _ in range(2):
        print(symbol[a], end=" ")
        a += 1
    for _ in range(10):
        print("   ", end="")
    for _ in range(6):
        print(symbol[a], end=" ")
        a += 1
    print("")

for _ in range(2):
    for _ in range(18):
        print(symbol[a], end=" ")
        a += 1
    print("")

for _ in range(2):
    for _ in range(3):
        print(symbol[a], end=" ")
        a += 1
    a += 14
    for _ in range(15):
        print(symbol[a], end=" ")
        a += 1
    print("")

print("")
print("")

a = 57
for _ in range(2):
    for _ in range(14):
        print(symbol[a], end=" ")
        a += 1
    a += 18
    print("")

print("")
print("")
print("")

# Get user input for atomic number
while True:
    try:
        atomic_number = int(input("Enter atomic number: "))
        element_properties = get_element_properties(atomic_number)
        print("\nElement Properties:")
        for key, value in element_properties.items():
            print(f"{key}: {value}")
        break  # Exit the loop after displaying properties
    except ValueError:
        print("Invalid input. Please enter a valid atomic number.")
    except IndexError:
        print("Element not found. Please enter a valid atomic number.")
