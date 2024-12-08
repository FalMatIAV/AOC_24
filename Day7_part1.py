from itertools import product

def evaluate_expression(numbers, operators):
    """Evaluates the expression with given numbers and operators in left-to-right order."""
    result = numbers[0]
    for i, operator in enumerate(operators):
        if operator == '+':
            result += numbers[i + 1]
        elif operator == '*':
            result *= numbers[i + 1]
    return result

def possible_to_calibrate(target, numbers):
    """Checks if the target value can be obtained by placing operators between numbers."""
    operator_combinations = product('+-*', repeat=len(numbers) - 1)
    for operators in operator_combinations:
        if evaluate_expression(numbers, operators) == target:
            return True
    return False

def total_calibration_result(equations):
    """Calculates the total calibration result for all valid equations."""
    total = 0
    for equation in equations:
        target, numbers = equation[0], equation[1:]
        if possible_to_calibrate(target, numbers):
            total += target
    return total

def parse_input(file_path):
    """Parses the input file and converts it into a list of equations."""
    equations = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                parts = line.split(':')
                target = int(parts[0].strip())
                numbers = list(map(int, parts[1].strip().split()))
                equations.append((target, *numbers))
    return equations

# Main execution
input_file = "input.txt"
equations = parse_input(input_file)
total_result = total_calibration_result(equations)
print("Total Calibration Result:", total_result)
