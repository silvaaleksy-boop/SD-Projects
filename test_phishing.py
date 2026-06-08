# Test for detect_phishing function.
# Example 1: Clear phishing attempt
phishing_text_1 = "Dear user, your account has been suspended. Please click here to verify your account: http://bad-link.com/login"
result_1 = detect_phishing(phishing_text_1)
print(f"Test 1: {result_1}\n")

# Example 2: More subtle, but still suspicious
phishing_text_2 = "Urgent action required! We've detected unusual activity. Kindly reset your password immediately via this link: http://another-bad.net"
result_2 = detect_phishing(phishing_text_2)
print(f"Test 2: {result_2}\n")

# Example 3: Legitimate-looking email (should ideally not be flagged)
legit_text = "Hello, your order #12345 has been shipped. Track your package here: https://example.com/track"
result_legit = detect_phishing(legit_text)
print(f"Test 3 (Legitimate): {result_legit}\n")
