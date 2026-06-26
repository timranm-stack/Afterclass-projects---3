def check_bit_probe(mask, j):
    """Goal 3: Create a bit probe using 1 << j to check the j-th bit."""
    probe = 1 << j
    return (mask & probe) != 0

def generate_power_set(items):
    """Goal 1, 2 & 4: Generate a power set containing all possible subsets 
    using binary masks and nested while loops.
    """
    n = len(items)
    # A set of size n has 2^n total subsets
    total_subsets = 1 << n 
    power_set = []
    
    mask = 0
    # Outer while loop to iterate through every possible binary mask configuration
    while mask < total_subsets:
        current_subset = []
        j = 0
        
        # Inner while loop acting as a bit probe over the list indices
        while j < n:
            # Goal 2 & 3: If the j-th bit is set, select the item
            if check_bit_probe(mask, j):
                current_subset.append(items[j])
            j += 1
            
        power_set.append(current_subset)
        mask += 1
        
    return power_set

def count_bit_difference(num1, num2):
    """Goal 5: Compare two numbers bit by bit to find their bit difference 
    (also known as Hamming distance).
    """
    difference_count = 0
    # Process bits until both numbers are 0
    while num1 > 0 or num2 > 0:
        # Extract the rightmost bit of each number
        bit1 = num1 & 1
        bit2 = num2 & 1
        
        # Compare them bit by bit
        if bit1 != bit2:
            difference_count += 1
            
        # Shift right to examine the next bit position
        num1 >>= 1
        num2 >>= 1
        
    return difference_count

# --- Goal 6: Connect binary patterns with real selection-based problems ---
print("=== BINARY SUBSET BUILDER ===")

# Example: Selecting pizza toppings
toppings = ["Pepperoni", "Mushrooms", "Onions"]
print(f"Original Set of Items: {toppings}")

print("\nGenerating Power Set (All Selection Combinations):")
all_subsets = generate_power_set(toppings)

# Display subsets alongside their corresponding binary mask representations
for index, subset in enumerate(all_subsets):
    # Formats index to its binary string equivalent matching the list size
    binary_mask_string = f"{index:0{len(toppings)}b}"
    print(f"Mask {index} ({binary_mask_string}) -> Selected Items: {subset}")

print("-" * 55)

# Testing Bit Difference Check (Goal 5)
# Mask 3 is '011' (Mushrooms, Pepperoni)
# Mask 5 is '101' (Onions, Pepperoni)
mask_a = 3 
mask_b = 5 
diff = count_bit_difference(mask_a, mask_b)

print(f"Comparing Mask {mask_a} ({mask_a:03b}) and Mask {mask_b} ({mask_b:03b}):")
print(f"Total selection changes needed (Bit Difference): {diff}")
print("=" * 55)