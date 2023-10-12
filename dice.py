import random

def roll_dice():
    return random.randint(1, 6)

# You can specify the number of rolls you want to simulate
num_rolls = 5

print(f"Simulating {num_rolls} dice rolls:")
for i in range(num_rolls):
    result = roll_dice()
    print(f"Roll {i + 1}: {result}")
