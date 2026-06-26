def remove_rightmost_set_bit(n):
    """Goal 1: Understand how the n & (n-1) trick removes the rightmost set bit."""
    return n & (n - 1)

def is_power_of_2(n):
    """Goal 2: Use a bitwise condition to check whether a number is a power of 2.
    A positive number is a power of 2 if it has exactly one set bit.
    """
    return n > 0 and (n & (n - 1)) == 0

def get_set_bit_position(n):
    """Goal 5: Use right shift to find the 0-indexed position of the single set bit."""
    if not is_power_of_2(n):
        return -1
    position = 0
    while n > 1:
        n >>= 1
        position += 1
    return position

def is_power_of_4(n):
    """Goal 3: Check powers of 4 using even bit positions.
    Powers of 4 must be a power of 2, and their single set bit must be 
    at an even position index (0, 2, 4, 6...). 
    Alternately checked with mask 0x55555555 (01010101... in binary).
    """
    if not is_power_of_2(n):
        return False
    position = get_set_bit_position(n)
    return position % 2 == 0

def is_power_of_8(n):
    """Goal 4: Check powers of 8 using bit positions divisible by 3.
    Powers of 8 must be a power of 2, and their single set bit position 
    must be divisible by 3 (0, 3, 6, 9...).
    """
    if not is_power_of_2(n):
        return False
    position = get_set_bit_position(n)
    return position % 3 == 0

def binary_exponentiation(base, exp):
    """Goal 6: Apply binary exponentiation to calculate powers quickly."""
    result = 1
    while exp > 0:
        # If exp is odd, multiply base with result
        if exp & 1:
            result *= base
        # Square the base and shift exp right by 1
        base *= base
        exp >>= 1
    return result

# --- Goal 7: Connect binary patterns with efficient mathematical checks ---
def scan_number(num):
    print(f"\nScanning Number: {num} (Binary: {num:08b})")
    
    # Check power of 2
    if is_power_of_2(num):
        pos = get_set_bit_position(num)
        print(f"  -> Is a Power of 2! (Set bit position: {pos})")
        
        # Check power of 4 (even positions)
        if is_power_of_4(num):
            print("  -> Is also a Power of 4! (Bit position is even)")
            
        # Check power of 8 (positions divisible by 3)
        if is_power_of_8(num):
            print("  -> Is also a Power of 8! (Bit position is divisible by 3)")
    else:
        print("  -> Not a power of 2.")
        print(f"  -> n & (n-1) bit removal visual: {remove_rightmost_set_bit(num):08b}")

# --- Execution ---
print("=== POWER OF TWO SCANNER ===")

# Testing the Scanner Checks
scan_number(16)   # 2^4 or 4^2 -> Position 4
scan_number(64)   # 2^6 or 4^3 or 8^2 -> Position 6
scan_number(12)   # Not a power of 2

print("\n--- Testing Binary Exponentiation ---")
# Quickly calculating 2^10
print(f"2^10 calculated quickly via binary exponentiation: {binary_exponentiation(2, 10)}")
print("=" * 28)