# Phishing Detection Prototype
IT Service Desk Projects
Project README (English Version)
Phishing Detection Prototype
This project presents a basic prototype for detecting phishing attempts within text-based content, such as email bodies or file attachments. Developed with a focus on practical application in an IT Service Desk environment.

Features
The core of the project is the detect_phishing function, which analyzes input text for common phishing indicators:

Suspicious Keywords: Identifies phrases frequently used in phishing emails (e.g., "verify your account", "urgent action required", "reset password").
Multiple URLs Presence: Flags text containing multiple URLs, which can be an indicator of malicious intent, especially when combined with other factors.
Requests for Personal Information: Detects direct solicitations for sensitive data (e.g., "provide your social security number", "confirm your credit card details").
Technologies Used
Python: The primary programming language.
re (Regular Expressions): Utilized for pattern matching in text, particularly for identifying URLs.
pandas (Optional): Included for potential future expansion, allowing for data handling and analysis of larger datasets of suspicious content.
How It Works
The detect_phishing function takes a string as input and returns a dictionary indicating whether phishing was detected (is_phishing: True/False) and a list of reasons if indicators were found. The detection is rule-based, using a predefined set of keywords and URL patterns.

Example Usage
# Example: Clear phishing attempt
phishing_text_1 = "Dear user, your account has been suspended. Please click here to verify your account: http://bad-link.com/login"
result_1 = detect_phishing(phishing_text_1)
print(f"Test 1: {result_1}\n")

# Example: Legitimate-looking email
legit_text = "Hello, your order #12345 has been shipped. Track your package here: https://example.com/track"
result_legit = detect_phishing(legit_text)
print(f"Test 3 (Legitimate): {result_legit}\n")
