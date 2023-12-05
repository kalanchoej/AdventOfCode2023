import re
total = 0
number_dict = { "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9 }
def str_to_number(str_rep: str) -> int:
  return number_dict[str_rep]

def get_min_max(some_dict: dict) -> tuple:
  dict_keys = list(some_dict.keys())
  min_val = some_dict[min(dict_keys)]
  max_val = some_dict[max(dict_keys)]
  return (str_to_number(min_val), str_to_number(max_val))

with open('01/input.txt') as f:
  for line in f:
    val_dict = {}
    # This is going to be a dictionary that holds the locations of numbers.
    # keys are going to be numbers as numbers or strings as numbers. Values
    # are a list of the starting locations in the substring
    line_dict = {}
    # start by running over the hard coded dict we created that maps all string representations of numbers so that we can look for them one at a time
    for k in number_dict.keys():
      # capture a list of substring locations
      location = [m.start() for m in re.finditer(k, line)]
      if len(location) > 0:
        line_dict[k] = location
      # Now we need to kinda go backwards and work through all of the values to create a new dict that has the locations as keys and the strings as values
    for j in line_dict.keys():
      for i in line_dict[j]:
        val_dict[i] = j
    # finally we get the highest and lowest key values and get the numeric values they represent
    min_max = get_min_max(val_dict)
    total += int(str(min_max[0]) + str(min_max[1]))
    print(line, min_max[0], min_max[1])

print(total)