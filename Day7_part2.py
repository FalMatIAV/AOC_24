import itertools

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if operators[i-1] == '+':
            result += numbers[i]
        elif operators[i-1] == '*':
            result *= numbers[i]
        elif operators[i-1] == '||':
            result = int(str(result) + str(numbers[i]))
    return result

def find_valid_equations_part2(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    total_calibration_result = 0
    valid_equations = []

    for line in lines:
        if not line.strip():
            continue
        test_value, numbers = line.split(':')
        test_value = int(test_value.strip())
        numbers = list(map(int, numbers.strip().split()))

        if len(numbers) == 1:
            continue

        operators = ['+', '*', '||']
        valid = False

        for ops in itertools.product(operators, repeat=len(numbers)-1):
            try:
                result = evaluate_expression(numbers, ops)
                if result == test_value:
                    valid = True
                    break
            except Exception as e:
                continue

        if valid:
            total_calibration_result += test_value
            valid_equations.append(line.strip())

    return total_calibration_result, valid_equations

if __name__ == "__main__":
    filename = 'input.txt'
    result_part2, valid_equations_part2 = find_valid_equations_part2(filename)
    
    print(f"Total calibration result (Part 2): {result_part2}")
    print("Valid equations (Part 2):")
    for eq in valid_equations_part2:
        print(eq)