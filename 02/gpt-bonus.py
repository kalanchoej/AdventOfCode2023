
def calculate_minimum_set_power(file_path):
    minimum_sets = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('Game'):
                # Initialize minimum counts for each color for this game
                min_counts = {'red': 0, 'green': 0, 'blue': 0}
                rounds = line.strip().split(': ')[1].split('; ')
                for round in rounds:
                    for part in round.split(', '):
                        count = int(part.split(' ')[0])
                        color = part.split(' ')[1].strip()  # Stripping any whitespace or newline characters
                        min_counts[color] = max(min_counts[color], count)

                # Calculate the power of the set for this game
                power = min_counts['red'] * min_counts['green'] * min_counts['blue']
                minimum_sets.append(power)

    # Summing the powers of the minimum sets
    return sum(minimum_sets)

# Path to the input file
file_path = '02/input.txt' # Replace with the actual path to the input file

# Calculate the sum of the power of minimum sets and print the result
print(calculate_minimum_set_power(file_path))
