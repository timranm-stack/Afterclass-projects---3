def xor_swap(a, b):
    """Goal 1 & 2: Swap two values without a third variable using XOR bitwise operations."""
    print(f"  Before Swap: a = {a}, b = {b}")
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"  After Swap:  a = {a}, b = {b}")
    return a, b

def double_using_left_shift(number):
    """Goal 3: Understand how left shift doubles a number.
    Shifting bits left by 1 position multiplies the integer value by 2.
    """
    return number << 1

def have_different_signs(num1, num2):
    """Goal 4: Use XOR logic to detect whether two numbers have different signs.
    The sign bit (most significant bit) is 1 for negative and 0 for positive.
    XOR returns 1 if bits differ, so a negative result means different signs.
    """
    return (num1 ^ num2) < 0

def divide_using_subtraction(dividend, divisor):
    """Goal 5: Divide two numbers using repeated subtraction instead of the / operator."""
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
        
    # Handle negative signs tracking
    negative_result = have_different_signs(dividend, divisor)
    
    # Work with absolute values
    dividend = abs(dividend)
    divisor = abs(divisor)
    
    quotient = 0
    remainder = dividend
    
    # Repeated subtraction loop
    while remainder >= divisor:
        remainder -= divisor
        quotient += 1
        
    # Apply sign back
    if negative_result:
        quotient = -quotient
        
    return quotient, remainder

# --- Goal 6: Connect bitwise operators with useful mathematical shortcuts ---
print("=== BITWISE SWAP CHALLENGE ===")

print("\n1. Testing XOR Swap:")
x = 15
y = 42
x, y = xor_swap(x, y)

print("\n2. Testing Left Shift Doubling Shortcut:")
test_num = 24
doubled = double_using_left_shift(test_num)
print(f"  {test_num} << 1 = {doubled} (Equivalent to {test_num} * 2)")

print("\n3. Testing Different Signs Detection via XOR:")
print(f"  Do 10 and -5 have different signs? {have_different_signs(10, -5)}")
print(f"  Do -8 and -3 have different signs? {have_different_signs(-8, -3)}")

print("\n4. Testing Division via Repeated Subtraction:")
dividend = 23
divisor = 5
q, r = divide_using_subtraction(dividend, divisor)
print(f"  Dividing {dividend} by {divisor}:")
print(f"  Quotient  = {q}")
print(f"  Remainder = {r}")
print("=" * 30)