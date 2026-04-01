print("=== Password Strength Checker ===")
password = input("Enter your password: ")
score = 0
suggestions = []
if len(password) >= 8:
    score += 1
else:
    suggestions.append("Make it at least 8 characters long")

if any(ch.isupper() for ch in password):
    score += 1
else:
    suggestions.append("Add uppercase letters (A-Z)")

if any(ch.islower() for ch in password):
    score += 1
else:
    suggestions.append("Add lowercase letters (a-z)")

if any(ch.isdigit() for ch in password):
    score += 1
else:
    suggestions.append("Include numbers (0-9)")
special_chars = "!@#$%^&*()-_=+[]{};:,.<>/?"

if any(ch in special_chars for ch in password):
    score += 1
else:
    suggestions.append("Use special characters (!,@,#,$, etc.)")
print("Your password score:", score, "/ 5")

if score == 5:
    print("Strong Password")
elif score >= 3:
    print("Medium Password")
else:
    print("Weak Password")
    
if suggestions:
    print("Suggestions to improve your password:")
    for s in suggestions:
        print("-", s)
