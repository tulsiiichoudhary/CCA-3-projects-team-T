# Name: Tulsi Choudhary
# PRN: 1302250705
# Task: ML Framework - Hugging Face Sentiment Monitor with Multiple Problem Statements

from transformers import pipeline

# Load pre-trained sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

# Problem Statements (Customer Reviews, Loan Feedback, UPI Experience, App Support)
test_statements = [
    "The instant loan disbursement process was smooth and credited within 5 minutes!",
    "My transaction failed at the payment gateway and my account was debited without a refund.",
    "Customer support answered my ticket quickly, though the portal UI is slightly confusing.",
    "Interest rates charged on this credit line are completely unfair and hidden in fine print.",
    "Very secure authentication flow, feels safe managing savings on this fintech app."
]

print("=== FinTech Sentiment Monitoring Results ===")
for idx, text in enumerate(test_statements, 1):
    result = sentiment_analyzer(text)[0]
    print(f"\nStatement {idx}: {text}")
    print(f"Sentiment: {result['label']} | Confidence: {round(result['score'] * 100, 2)}%")
