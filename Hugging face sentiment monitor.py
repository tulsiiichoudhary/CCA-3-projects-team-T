# Name: Swandan Nayak 
# PRN: 1302250597
# Task: Hugging Face Sentiment Monitor - Mobile App UI & UX

from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

# Member 3 Custom Scenarios: App Performance & Bug Reports
test_statements = [
    "Biometric fingerprint login is ultra responsive and accurate.",
    "App crashes immediately after typing OTP on Android 14.",
    "Dashboard layout is very intuitive and easy for elderly users.",
    "Frequent session timeouts make balance checking frustrating.",
    "Dark mode looks sleek and saves battery."
]

print("=== Member 3 Sentiment Analysis ===")
for idx, text in enumerate(test_statements, 1):
    res = sentiment_analyzer(text)[0]
    print(f"{idx}. {text} | Result: {res['label']} ({round(res['score']*100, 2)}%)")
