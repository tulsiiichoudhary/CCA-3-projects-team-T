# Name: Aman Vaswani
# PRN: 1302250739
# Task: Hugging Face Sentiment Monitor - Cyber Security & Fraud Alerts

from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

# Member 6 Custom Scenarios: Security & Alert Feedback
test_statements = [
    "Instant SMS alert helped me block suspicious card transaction immediately.",
    "Phishing email looked identical to genuine bank communication, scary experience.",
    "Two-factor authentication makes me feel completely protected.",
    "Unwanted spam calls offering personal loans multiple times a day.",
    "Biometric lock prevented unauthorized access when phone was misplaced."
]

print("=== Member 6 Sentiment Review ===")
for idx, text in enumerate(test_statements, 1):
    res = sentiment_analyzer(text)[0]
    print(f"{idx}. {text} --> {res['label']} ({round(res['score']*100, 2)}%)")
