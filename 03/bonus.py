import re
  
def get_ranges(index: int, start: int, end: int, last_index: int, line_len: int) -> list[list[int]]:
  if index == 0:
    return [
      [index, max(start-1, 0), min(end+1, line_len-1)], 
      [index+1, max(start-1, 0), min(end+1, line_len-1)]]
  if index == last_index:
    return [
      [index, max(start-1, 0), min(end+1, line_len-1)], 
      [index-1, max(start-1, 0), min(end+1, line_len-1)]]
  return [
    [index-1, max(start-1, 0), min(end+1, line_len-1)], 
    [index, max(start-1, 0), min(end+1, line_len-1)],
    [index+1, max(start-1, 0), min(end+1, line_len-1)]]

def search_surroundings_for_symbols(file_array, search_ranges) -> bool:
  pat = r"[^\d\.\n]"
  for r in search_ranges:
    index = r[0]
    start = r[1]
    end = r[2]
    found = re.search(pat, file_array[index][start:end])
    if found is not None:
      print(found.group())
      return True
  return False
  
def count_surrounding_parts(file_array, search_ranges) -> int:
  one_part_pat = r"(\d{3})|(\d{2}\D)|(\D\d{2})|(\d\D{2})|(\D{2}\d)"
  two_part_pat = r"(\d\D\d)"
  part_count = 0
  for r in search_ranges:
    index = r[0]
    start = r[1]
    end = r[2]
    found_one = re.search(one_part_pat, file_array[index][start:end])
    found_two = re.search(two_part_pat, file_array[index][start:end])
    if found_one is not None:
      part_count += 1
    if found_two is not None:
      part_count += 2
  return part_count
  

def find_possible_parts_in_line(index, line, last_index):
  pat = re.compile(r"(\d+)")
  numbers = re.finditer(pat, line)
  possible_parts = []
  for n in numbers:
    possible_parts.append({'number': n.group(), 'search_ranges': get_ranges(index, n.start(), n.end(), last_index, len(line))})
  return possible_parts

def find_possible_gears_in_line(index, line, last_index):
  pat = re.compile(r"(\*)")
  numbers = re.finditer(pat, line)
  possible_gears = []
  for n in numbers:
    possible_gears.append({'number': 1, 'search_ranges': get_ranges(index, n.start(), n.end(), last_index, len(line))})
  return possible_gears

def is_part(file_array, search_ranges) -> bool:
  return search_surroundings_for_symbols(file_array, search_ranges)

def is_gear(file_array, search_ranges) -> bool:
  if count_surrounding_parts(file_array, search_ranges) == 2:
    print("found gear")
    return True
  return False

def process_input(inputfile):
  total = 0
  file_array = [f.strip() for f in open(inputfile)]
  for index, line in enumerate(file_array, 0):
    possible_gears = find_possible_gears_in_line(index, file_array[index], len(file_array)-1)
    for possible_gear in possible_gears:
      if (is_gear(file_array, possible_gear['search_ranges'])):
        total += int(possible_gear['number'])
  return total
      
print(process_input('03/input.txt'))