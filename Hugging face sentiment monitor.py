# Name: Subham Sahu
# PRN: 1302250465
# Task: Hugging Face Sentiment Monitor - Payment & Transfer Cases

from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

# Member 1 Custom Scenarios: UPI & Fund Transfer Experiences
test_statements = [
    "Money was instantly credited to the merchant via QR scanner!",
    "Server timeout occurred during fund transfer and amount is on hold.",
    "Auto-debit for SIP failed without prior notification.",
    "Seamless international remittance received within an hour.",
    "Transaction charges for bank transfer are unexpectedly high."
]

print("=== Member 1 Sentiment Test Cases ===")
for idx, text in enumerate(test_statements, 1):
    res = sentiment_analyzer(text)[0]
    print(f"{idx}. {text} --> {res['label']} ({round(res['score']*100, 2)}%)")
