#This project aims to demonstrate basic phishing detection capabilities.

import re
import pandas as pd 

print("Done")


#Phishing Detection Function
Define a function that takes input text (e.g., from an email or a document) and analyzes it for phishing indicators. Initially, this function will look for common suspicious patterns.
                        def detect_phishing(text: str) -> dict:
    """
    Detects potential phishing indicators in the given text.
    Returns a dictionary with detection results.
    """
    indicators = {
        "is_phishing": False,
        "reasons": []
    }

    # Convert text to lowercase for case-insensitive matching
    text_lower = text.lower()


    # 1. Suspicious keywords
    suspicious_keywords = ["verify your account", "urgent action required", "security alert", "reset password", "invoice overdue", "bank account suspended"]
    for keyword in suspicious_keywords:
        if keyword in text_lower:
            indicators["is_phishing"] = True
            indicators["reasons"].append(f"Suspicious keyword found: '{keyword}'")

    # 2. Presence of URLs with non-matching display text (basic check)
    url_pattern = re.compile(r'https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    urls_found = url_pattern.findall(text)
    if urls_found:
        
        if not indicators["is_phishing"] and len(urls_found) > 1: 
             indicators["is_phishing"] = True
             indicators["reasons"].append("Multiple URLs detected, which can be a phishing indicator.")

    # 3. Request for personal information
    personal_info_requests = ["provide your social security number", "confirm your credit card details", "send us your password"]
    for request in personal_info_requests:
        if request in text_lower:
            indicators["is_phishing"] = True
            indicators["reasons"].append(f"Request for personal information: '{request}'")


    return indicators
                                                                                                                               
