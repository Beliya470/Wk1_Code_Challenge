# ==========================================
# Challenge 1: Converting 12-hour time to 24-hour time
# ==========================================

def to_24_hour(hour, minute, period):
    if period == "pm" and hour != 12:
        hour += 12
    if period == "am" and hour == 12:
        hour = 0

    return f"{hour:02}{minute:02}"

# Test Challenge 1
print(to_24_hour(8, 30, "am"))  # 0830
print(to_24_hour(8, 30, "pm"))  # 2030
print(to_24_hour(12, 0, "am")) # 0000

# ==========================================
# Challenge 2: Two numbers are positive
# ==========================================

def two_are_positive(a, b, c):
    positives = sum([1 for num in [a, b, c] if num > 0])
    return positives == 2

# Test Challenge 2
print(two_are_positive(2, 4, -3))   # True
print(two_are_positive(-4, 6, 8))   # True
print(two_are_positive(4, -6, 9))   # True
print(two_are_positive(-4, 6, 0))   # False
print(two_are_positive(4, 6, 10))   # False
print(two_are_positive(-14, -3, -4))# False

# ==========================================
# Challenge 3: Consonant value
# ==========================================

def solve(s):
    consonant_values = {char: ord(char) - 96 for char in "bcdfghjklmnpqrstvwxyz"}
    max_value = 0
    current_value = 0

    for char in s:
        if char in consonant_values:
            current_value += consonant_values[char]
        else:
            max_value = max(max_value, current_value)
            current_value = 0

    return max(max_value, current_value)

# Test Challenge 3
print(solve("zodiacs"))   # 26
print(solve("strength"))  # 57
