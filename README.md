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
# Example 1: Clear phishing attempt
phishing_text_1 = "Dear user, your account has been suspended. Please click here to verify your account: http://bad-link.com/login"
result_1 = detect_phishing(phishing_text_1)
print(f"Test 1: {result_1}\n")

# Example 3: Legitimate-looking email
legit_text = "Hello, your order #12345 has been shipped. Track your package here: https://example.com/track"
result_legit = detect_phishing(legit_text)
print(f"Test 3 (Legitimate): {result_legit}\n")
Project README (Wersja Polska)
Prototyp Systemu Detekcji Phishingu
Ten projekt przedstawia podstawowy prototyp systemu do wykrywania prób phishingu w treściach tekstowych, takich jak treść wiadomości e-mail lub załączników. Opracowany z myślą o praktycznym zastosowaniu w środowisku IT Service Desk.

Funkcjonalności
Rdzeniem projektu jest funkcja detect_phishing, która analizuje wprowadzony tekst pod kątem typowych wskaźników phishingu:

Podejrzane słowa kluczowe: Identyfikuje frazy często używane w e-mailach phishingowych (np. "verify your account", "urgent action required", "reset password").
Obecność wielu adresów URL: Oznacza tekst zawierający wiele linków, co może być wskaźnikiem złośliwych intencji, szczególnie w połączeniu z innymi czynnikami.
Prośby o dane osobowe: Wykrywa bezpośrednie prośby o wrażliwe dane (np. "provide your social security number", "confirm your credit card details").
Użyte Technologie
Python: Główny język programowania.
re (Wyrażenia Regularne): Wykorzystywane do dopasowywania wzorców w tekście, szczególnie do identyfikacji adresów URL.
pandas (Opcjonalnie): Uwzględniony w celu potencjalnej przyszłej rozbudowy, umożliwiając obsługę danych i analizę większych zbiorów podejrzanych treści.
Jak to działa?
Funkcja detect_phishing przyjmuje ciąg znaków jako dane wejściowe i zwraca słownik wskazujący, czy phishing został wykryty (is_phishing: True/False) oraz listę powodów, jeśli znaleziono wskaźniki. Detekcja opiera się na regułach, wykorzystując predefiniowany zestaw słów kluczowych i wzorców URL.

Przykładowe użycie
# Przykład 1: Wyraźna próba phishingu
phishing_text_1 = "Drogi użytkowniku, Twoje konto zostało zawieszone. Kliknij tutaj, aby zweryfikować swoje konto: http://zly-link.com/login"
result_1 = detect_phishing(phishing_text_1)
print(f"Test 1: {result_1}\n")

# Przykład 3: Wiarygodnie wyglądający e-mail
legit_text = "Witaj, Twoje zamówienie #12345 zostało wysłane. Śledź swoją paczkę tutaj: https://example.com/track"
result_legit = detect_phishing(legit_text)
print(f"Test 3 (Legitimate): {result_legit}\n")
