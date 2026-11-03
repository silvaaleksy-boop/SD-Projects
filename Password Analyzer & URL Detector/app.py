import math
import re
import tkinter as tk
from tkinter import ttk
from urllib.parse import urlparse

def calculate_shannon_entropy(password: str) -> float:
    """Calculates the Shannon entropy of a given password."""
    if not password:
        return 0.0
    length = len(password)
    frequencies = {}
    for char in password:
        frequencies[char] = frequencies.get(char, 0) + 1
    entropy = 0.0
    for count in frequencies.values():
        p = count / length
        entropy -= p * math.log2(p)
    return round(entropy * length, 2)

def evaluate_password_strength(password: str) -> dict:
    """Heuristically evaluates password strength based on length, entropy, and character diversity."""
    length = len(password)
    entropy = calculate_shannon_entropy(password)

    has_upper = int(bool(re.search(r'[A-Z]', password)))
    has_lower = int(bool(re.search(r'[a-z]', password)))
    has_digit = int(bool(re.search(r'[0-9]', password)))
    has_special = int(bool(re.search(r'[^A-Za-z0-9]', password)))

    diversity_score = has_upper + has_lower + has_digit + has_special

    if length < 8:
        category = "Very Weak (Too Short)"
        color = "#d9534f" # Red
    elif length < 12 or entropy < 40 or diversity_score < 3:
        category = "Weak"
        color = "#f0ad4e" # Orange
    elif entropy < 60 or diversity_score < 4:
        category = "Medium"
        color = "#5bc0de" # Blue
    else:
        category = "Strong"
        color = "#5cb85c" # Green

    return {
        "password": password,
        "length": length,
        "entropy_bits": entropy,
        "diversity_score": f"{diversity_score}/4",
        "category": category,
        "color": color
    }

def analyze_url_safety(url: str) -> dict:
    """Heuristically analyzes a URL for phishing indicators."""
    reasons = []
    parsed_url = urlparse(url)
    domain = parsed_url.netloc or parsed_url.path.split('/')[0]

    ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    if re.match(ip_pattern, domain):
        reasons.append("IP address used instead of domain name")

    if len(url) > 75:
        reasons.append(f"URL is exceptionally long ({len(url)} characters)")

    if '@' in url:
        reasons.append("Contains '@' character (used to obscure destination)")

    if domain.count('-') > 2:
        reasons.append("Excessive number of hyphens in domain")

    suspicious_keywords = ['login', 'secure', 'bank', 'update', 'verify', 'signin', 'account', 'paypal', 'webscr']
    found_keywords = [kw for kw in suspicious_keywords if kw in url.lower()]
    if found_keywords:
        reasons.append(f"Contains suspicious keyword(s): {found_keywords}")

    is_phishing = len(reasons) >= 2 or ("IP address used instead of domain name" in reasons)
    classification = "Phishing / Suspicious" if is_phishing else "Safe / Low Risk"
    color = "#d9534f" if is_phishing else "#5cb85c"

    return {
        "url": url,
        "classification": classification,
        "reasons_detected": reasons if reasons else ["None"],
        "color": color
    }

class SecurityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Security Hub: Password Analyzer & URL Detector")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        style = ttk.Style()
        style.theme_use('clam')

        tab_control = ttk.Notebook(root)

        self.tab_pass = ttk.Frame(tab_control)
        self.tab_url = ttk.Frame(tab_control)

        tab_control.add(self.tab_pass, text='Password Strength')
        tab_control.add(self.tab_url, text='URL Phishing Detector')
        tab_control.pack(expand=1, fill="both")

        self.setup_password_tab()
        self.setup_url_tab()

    def setup_password_tab(self):
        title = tk.Label(self.tab_pass, text="Password Strength Analyzer", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        lbl = tk.Label(self.tab_pass, text="Enter Password:", font=("Arial", 10))
        lbl.pack(pady=5)

        self.pass_entry = ttk.Entry(self.tab_pass, show="*", width=40, font=("Arial", 11))
        self.pass_entry.pack(pady=5)

        btn = ttk.Button(self.tab_pass, text="Analyze", command=self.on_analyze_password)
        btn.pack(pady=10)

        self.lbl_category = tk.Label(self.tab_pass, text="", font=("Arial", 14, "bold"))
        self.lbl_category.pack(pady=10)

        self.lbl_entropy = tk.Label(self.tab_pass, text="", font=("Arial", 10))
        self.lbl_entropy.pack(pady=5)

        self.lbl_diversity = tk.Label(self.tab_pass, text="", font=("Arial", 10))
        self.lbl_diversity.pack(pady=5)

    def on_analyze_password(self):
        password = self.pass_entry.get()
        res = evaluate_password_strength(password)
        self.lbl_category.config(text=f"Strength: {res['category']}", fg=res['color'])
        self.lbl_entropy.config(text=f"Entropy: {res['entropy_bits']} bits (Length: {res['length']})")
        self.lbl_diversity.config(text=f"Character Diversity: {res['diversity_score']}")

    def setup_url_tab(self):
        title = tk.Label(self.tab_url, text="URL Phishing Detector", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        lbl = tk.Label(self.tab_url, text="Enter URL:", font=("Arial", 10))
        lbl.pack(pady=5)

        self.url_entry = ttk.Entry(self.tab_url, width=50, font=("Arial", 11))
        self.url_entry.pack(pady=5)

        btn = ttk.Button(self.tab_url, text="Scan URL", command=self.on_analyze_url)
        btn.pack(pady=10)

        self.lbl_classification = tk.Label(self.tab_url, text="", font=("Arial", 14, "bold"))
        self.lbl_classification.pack(pady=10)

        lbl_reasons_header = tk.Label(self.tab_url, text="Threat Indicators:", font=("Arial", 10, "underline"))
        lbl_reasons_header.pack(pady=2)

        self.txt_reasons = tk.Text(self.tab_url, height=6, width=60, font=("Arial", 9), state="disabled", bg="#f4f4f4", relief="flat")
        self.txt_reasons.pack(pady=5)

    def on_analyze_url(self):
        url = self.url_entry.get()
        res = analyze_url_safety(url)
        self.lbl_classification.config(text=f"Verdict: {res['classification']}", fg=res['color'])

        self.txt_reasons.config(state="normal")
        self.txt_reasons.delete("1.0", tk.END)
        for r in res['reasons_detected']:
            self.txt_reasons.insert(tk.END, f"• {r}\n")
        self.txt_reasons.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = SecurityApp(root)
    root.mainloop()
