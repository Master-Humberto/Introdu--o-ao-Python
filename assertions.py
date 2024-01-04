def sum(a, b):
    return a + b

# Assertions table
assertions = [
    # Test case 1: Positive numbers
    {'input': (2, 3), 'expected_output': 5},
    
    # Test case 2: Negative numbers
    {'input': (-5, -7), 'expected_output': -12},
    
    # Test case 3: Zeroes
    {'input': (0, 0), 'expected_output': 0},
    
    # Test case 4: Mixed positive and negative numbers
    {'input': (10, -3), 'expected_output': 7},
    
    # Test case 5: Large numbers
    {'input': (1000000, 2000000), 'expected_output': 3000000},
]

# Run assertions
for assertion in assertions:
    input_data = assertion['input']
    expected_output = assertion['expected_output']
    assert sum(*input_data) == expected_output, f"Failed assertion: sum{input_data} != {expected_output}"
    print("assertion passed!")