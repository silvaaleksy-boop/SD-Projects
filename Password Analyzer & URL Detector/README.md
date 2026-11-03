README: Project Overview & Code Description
Password Analyzer & URL Detector

Password Analyzer & URL Detector is a lightweight, privacy focused desktop application designed to evaluate key aspects of personal digital security. Operating entirely offline, it ensures that sensitive credentials and analyzed links are not transmitted over the network.

Application Features
Password Strength Analyzer: Uses Shannon entropy calculations and character diversity checks to provide a precise, realistic assessment of password strength, moving beyond simple length requirements.
URL Phishing Detector: Employs analysis to quickly scan links for threat indicators, such as IP-based hosts, excessive lengths, hidden redirect symbols (`@`), and common phishing keywords.
User-Friendly GUI: Offers a simple, clean, and intuitive tabbed interface built with native window styling, separating the password and link analysis modules for seamless navigation.

Code Architecture
calculate_shannon_entropy: Computes the entropy of the password string to determine its unpredictable randomness in bits.
evaluate_password_strength: Analyzes character composition (uppercase, lowercase, numbers, symbols) and combines this diversity with entropy to categorize passwords from 'Very Weak' to 'Strong'.
analyze_url_safety: Parses input URLs and evaluates them against custom heuristic rules to identify potential phishing indicators, generating clear threat verdicts.
SecurityApp Class: Manages the Tkinter graphical user interface, event loops, and input-output flow to deliver real-time visual results.

Download link to the app:
https://drive.google.com/file/d/1X4A8jEfYw4z8SzqijPaHRu210RUa7gNC/view?usp=drive_link
