
# Function to check if a game is possible with the given cube limits
def is_game_possible(game_data, max_red, max_green, max_blue):
    rounds = game_data.split('; ')
    for round in rounds:
        # Extracting the counts of each color in this round
        counts = {'red': 0, 'green': 0, 'blue': 0}
        for part in round.split(', '):
            color = part.split(' ')[1]
            count = int(part.split(' ')[0])
            if color in counts:
                counts[color] = max(counts[color], count)
        # Checking if any color exceeds its limit
        if counts['red'] > max_red or counts['green'] > max_green or counts['blue'] > max_blue:
            return False
    return True

# Function to process the game data
def process_game_data(filepath, max_red, max_green, max_blue):
    possible_game_ids = []
    with open(filepath, 'r') as file:
        for line in file:
            if line.startswith('Game'):
                game_id = int(line.split(': ')[0].split(' ')[1])
                game_data = line.split(': ')[1].strip()
                if is_game_possible(game_data, max_red, max_green, max_blue):
                    possible_game_ids.append(game_id)
    return sum(possible_game_ids)

# Constants for the maximum number of cubes
max_red = 12
max_green = 13
max_blue = 14

# Filepath to the input data
file_path = '02/input.txt' # Replace with the actual path to the input file

# Processing the file and printing the sum of the IDs of possible games
print(process_game_data(file_path, max_red, max_green, max_blue))
