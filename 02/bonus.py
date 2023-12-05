import re

def get_game_num(line: str) -> int:
  game_num = re.search(r"Game (\d*):", line).group(1)
  return int(game_num)

def get_ball_sets(line: str) -> list[tuple[int, str]]:
  pat = re.compile(r"(\d*) (green|blue|red)")
  ball_sets = [(int(set.group(1)), set.group(2)) for set in (pat.finditer(line))]
  return ball_sets
  
def parse_game_line(line: str) -> dict:
  game_summary = {
    'game_id': get_game_num(line),
    'ball_sets': get_ball_sets(line),
    'ball_sets_by_color': group_ball_sets_by_color(line),
    'game_power': get_game_power(line),
    'is_valid': validate_all(line)
  }
  print(game_summary)
  return game_summary

def get_game_power(line: str) -> int:
  color_groupings = group_ball_sets_by_color(line)
  power = 1
  for k in color_groupings.keys():
    power *= max(color_groupings[k])
  return power

def group_ball_sets_by_color(line: str) -> dict:
  ball_sets = get_ball_sets(line)
  groupings = {
    'red': [],
    'green': [],
    'blue': []
  }
  for set in ball_sets:
    print(f"set: {set}")
    number, color = set[0], set[1]
    groupings[color].append(number)
  print(groupings)
  return groupings
  
def validate_all(line) -> bool:
  ball_sets = get_ball_sets(line)
  for i in ball_sets:
    if not validate(i): return False
  return True

# Take a single ball set as a tuple (2, blue) and validate it
def validate(ball_set: tuple[int, str]) -> bool:
  number, color = ball_set[0], ball_set[1]
  if (number > 12 and color == 'red' 
      or number > 13 and color == 'green' 
      or number > 14 and color == 'blue'):
      return False
  return True
  
  
def process_games(inputfile):
  total = 0
  with open(inputfile) as f:
    for line in f:
      total += parse_game_line(line)['game_power']
  print(f"invalid game sum {total}")
      
process_games('02/input.txt')