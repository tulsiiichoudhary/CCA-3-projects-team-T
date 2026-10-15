# Name: Deep Agarwal 
# PRN: 1302250670
# Task: Hugging Face Sentiment Monitor - Loan & Credit Inquiries

from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

# Member 4 Custom Scenarios: Loan Processing Feedback
test_statements = [
    "Education loan interest rate subsidy credited without delay!",
    "Customer executive asked for unnecessary physical documents despite paperless promise.",
    "Pre-approved home loan offer saved a huge amount of processing time.",
    "Hidden processing fees charged after sanction letter was generated.",
    "Very transparent loan repayment schedule provided in PDF."
]

print("=== Member 4 Sentiment Monitor ===")
for idx, text in enumerate(test_statements, 1):
    res = sentiment_analyzer(text)[0]
    print(f"{idx}. {text} -> {res['label']} ({round(res['score']*100, 2)}%)")
