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
    'is_valid': validate_all(get_ball_sets(line))
  }
  return game_summary
  
def validate_all(ball_sets: list[tuple[int, str]]) -> bool:
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
      game_summary = parse_game_line(line)
      if game_summary['is_valid']: 
        total += game_summary['game_id']
  return total
      
print(process_games('02/input.txt'))