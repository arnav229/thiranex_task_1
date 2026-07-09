import re
import secrets
import string

def analyze_password(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (minimum 8 characters, 12+ recommended).")

    # Check complexity
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    # Determine strength
    if score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback

def generate_strong_password(length=14):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()"
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in "!@#$%^&*()" for c in password)):
            return password

# Example Usage
user_password = input("Enter password to analyze: ")
strength, suggestions = analyze_password(user_password)

print(f"\nPassword Strength: {strength}")
if suggestions:
    print("Suggestions to improve:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
    print(f"Suggested Alternative: {generate_strong_password()}")
