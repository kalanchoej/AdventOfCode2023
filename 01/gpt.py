import re

def find_first_last_digits_overlapping_corrected(line, digit_map):
    """
    Find the first and last digit in the given line,
    correctly handling both numerical and overlapping spelled-out digits.
    """
    # Preparing the line for processing
    line_processed = re.sub('[^a-z0-9]', ' ', line.lower())  # Replace non-alphanumeric characters with spaces

    # Finding all occurrences of each digit or spelled-out digit
    digit_occurrences = []
    for word, digit in digit_map.items():
        start_positions = [m.start() for m in re.finditer(word, line_processed)]
        for pos in start_positions:
            digit_occurrences.append((pos, digit))

    # Sort occurrences by their position in the line
    digit_occurrences.sort(key=lambda x: x[0])

    # Extract the first and last digits
    first_digit = digit_occurrences[0][1] if digit_occurrences else None
    last_digit = digit_occurrences[-1][1] if digit_occurrences else None

    # If only one digit is found, it's used as both first and last digit
    if first_digit and not last_digit:
        last_digit = first_digit

    return first_digit, last_digit

def calculate_total_calibration_value_overlapping_corrected(file_path):
    total = 0
    digit_map = {
        "0": "0", "1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    with open(file_path, 'r') as file:
        for line in file:
            first_digit, last_digit = find_first_last_digits_overlapping_corrected(line, digit_map)
            if first_digit and last_digit:
                total += int(first_digit + last_digit)
    return total

print(calculate_total_calibration_value_overlapping_corrected('01/input.txt'))