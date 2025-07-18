import re

def check_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Counting how many rules are passed
    score = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, special_char_error])

    if score == 5:
        return "Strong "
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    result = check_strength(pwd)
    print(f"Password Strength: {result}")
