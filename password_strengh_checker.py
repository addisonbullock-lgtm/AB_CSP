# AB - Password Strength Checker

# 1. Ask for user input and store as a variable
password = input("What is your password: ")

# 2. Check each individual rule using string methods/membership checks
has_length = len(password) >= 8
has_uppercase = any(char.isupper() for char in password)
has_lowercase = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)

# Define symbol set and check if password contains at least one
symbols = "!@#$%^&*()_+-=[]{}|;:'\",.<>/?`~"
has_symbol = any(char in symbols for char in password)

# 3. Print True/False results for each individual rule
print(f"At least 8 characters: {has_length}")
print(f"Has an uppercase letter: {has_uppercase}")
print(f"Has a lowercase letter: {has_lowercase}")
print(f"Has a number: {has_digit}")
print(f"Has a symbol: {has_symbol}")

# 4. Calculate total number of rules met
score = sum([has_length, has_uppercase, has_lowercase, has_digit, has_symbol])

# 5. Determine overall strength rating based on total rules met
if score == 5:
    strength = "Strong"
elif score >= 3:
    strength = "Medium"
else:
    strength = "Weak"

print(f"Your password strength is: {strength}")

# 6. If not Strong, identify and print specific missing rules
if strength != "Strong":
    missing = []
    
    if not has_length:
        missing.append("at least 8 characters")
    if not has_uppercase:
        missing.append("an uppercase letter")
    if not has_lowercase:
        missing.append("a lowercase letter")
    if not has_digit:
        missing.append("a number")
    if not has_symbol:
        missing.append("a symbol")
        
    print(f"To make it Strong, add: {', '.join(missing)}")