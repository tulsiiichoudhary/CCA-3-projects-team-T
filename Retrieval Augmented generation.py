# Name:Aman Vaswani
# PRN: 1302250739
# Task: RAG Framework - Digital Banking & Net Banking Limits

knowledge_base = {
    "neft_rtgs": "RTGS is available 24x7 with a minimum transaction threshold of Rs. 2,00,000.",
    "imps_limit": "IMPS daily transaction ceiling is capped at Rs. 5,00,000 per user.",
    "cooling_period": "New beneficiary addition requires a 2-hour cooling window before transfers."
}

# Rule 1: Limit validation rule
# Rule 2: Security check rule
# Rule 3: Fraud mitigation warning

def retrieve_and_generate(query):
    query_lower = query.lower()
    match = None
    for k, v in knowledge_base.items():
        if k in query_lower or any(word in query_lower for word in k.split("_")):
            match = v
            break
            
    if not match:
        return "Transaction limit rule not found."
    return f"Retrieved Limit Policy: {match}\n[Security Notice: Never share OTP or UPI PIN for receiving funds.]"

queries = [
    "What is the cooling period for new beneficiary?",
    "What is the imps limit per day?",
    "Can I transfer funds internationally via IMPS?"
]

for q in queries:
    print(f"\nQ: {q}\nA: {retrieve_and_generate(q)}")
