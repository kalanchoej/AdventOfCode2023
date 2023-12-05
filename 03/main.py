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
  print(search_ranges)
  for r in search_ranges:
    index = r[0]
    start = r[1]
    end = r[2]
    found = re.search(pat, file_array[index][start:end])
    if found is not None:
      return True
  return False
  

def find_possible_parts_in_line(index, line, last_index):
  pat = re.compile(r"(\d+)")
  numbers = re.finditer(pat, line)
  possible_parts = []
  for n in numbers:
    possible_parts.append({'number': n.group(), 'search_ranges': get_ranges(index, n.start(), n.end(), last_index, len(line))})
  return possible_parts

def is_part(file_array, search_ranges) -> bool:
  return search_surroundings_for_symbols(file_array, search_ranges)

def process_input(inputfile):
  total = 0
  file_array = [f.strip() for f in open(inputfile)]
  for index, line in enumerate(file_array, 0):
    possible_parts = find_possible_parts_in_line(index, file_array[index], len(file_array)-1)
    for possible_part in possible_parts:
      if (is_part(file_array, possible_part['search_ranges'])):
        total += int(possible_part['number'])
  return total
      
print(process_input('03/input.txt'))