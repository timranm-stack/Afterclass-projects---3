def check_equal_using_xor(num1, num2):
    """Goal 2: Use XOR to check whether two numbers are equal.
    If a ^ b == 0, then a and b are identical.
    """
    return (num1 ^ num2) == 0

def find_single_odd_occurring(numbers):
    """Goal 3 & 4: Apply XOR cancellation to find ONE odd-occurring number.
    By XORing all elements together, pairs cancel out (a ^ a = 0), 
    leaving only the number that appears an odd number of times.
    """
    xor_sum = 0
    for num in numbers:
        xor_sum ^= num  # Goal 1: a ^ a = 0 and a ^ 0 = a
    return xor_sum

def find_two_odd_occurring(numbers):
    """Goal 5, 6 & 7: Find TWO odd-occurring numbers using splitting logic."""
    # Step 1: Find the XOR of the two odd-occurring numbers (Goal 5)
    xor_all = 0
    for num in numbers:
        xor_all ^= num
        
    if xor_all == 0:
        return "No distinct pair of odd-occurring numbers exists."

    # Step 2: Get the rightmost set bit of the combined XOR result (Goal 6)
    # This bit is 1 because the two hidden numbers must have different bits here.
    rightmost_set_bit = xor_all & ~(xor_all - 1)
    
    # Step 3: Split the numbers into two groups and find the unique values (Goal 6 & 7)
    group1_result = 0
    group2_result = 0
    
    for num in numbers:
        # Check if the specific rightmost bit is set in the current number
        if (num & rightmost_set_bit) != 0:
            group1_result ^= num  # XOR numbers belonging to Group 1
        else:
            group2_result ^= num  # XOR numbers belonging to Group 2
            
    return group1_result, group2_result

# --- Demonstration / Testing the Project Goals ---

print("=== BINARY CLUE INVESTIGATOR ===")

# Testing Goal 2
print(f"Are 12 and 12 equal? {check_equal_using_xor(12, 12)}")
print(f"Are 12 and 7 equal? {check_equal_using_xor(12, 7)}")
print("-" * 50)

# Testing Goals 3 & 4: Finding ONE odd-occurring number
# Pairs: (4,4), (3,3), (8,8). Odd one out: 5
clues_list_1 = [4, 3, 5, 4, 8, 3, 8]
single_odd = find_single_odd_occurring(clues_list_1)
print(f"Investigating List 1: {clues_list_1}")
print(f"Found the single odd-occurring clue: {single_odd}")
print("-" * 50)

# Testing Goals 5, 6 & 7: Finding TWO odd-occurring numbers
# Pairs: (2,2), (7,7). Odd ones out: 3 and 5
clues_list_2 = [2, 3, 7, 5, 2, 7]
print(f"Investigating List 2: {clues_list_2}")

# The cumulative XOR total of list elements represents (3 ^ 5)
combined_xor = find_single_odd_occurring(clues_list_2) 
print(f"XOR combination of the two odd numbers (3 ^ 5): {combined_xor} (Binary: {combined_xor:04b})")

# Split and isolate the hidden pair
odd_num1, odd_num2 = find_two_odd_occurring(clues_list_2)
print(f"Successfully split groups and identified both clues: {odd_num1} and {odd_num2}")
print("=" * 50)