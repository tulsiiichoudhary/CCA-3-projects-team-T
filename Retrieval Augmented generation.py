# Name: Parth Deshmukh
# PRN: 1302250642
# Task: RAG Framework - KYC & Document Verification Rules

knowledge_base = {
    "aadhaar_kyc": "Aadhaar e-KYC requires an active mobile number linked for OTP authentication.",
    "pan_card": "Valid PAN is mandatory for all accounts with transactions exceeding Rs. 50,000.",
    "address_proof": "Utility bills not older than 3 months are accepted as valid address proof."
}

# Rule 1: Strict match verification
# Rule 2: Non-match fallback notification
# Rule 3: Regulatory compliance disclaimer

def retrieve_and_generate(query):
    query_lower = query.lower()
    match = None
    for k, v in knowledge_base.items():
        if k in query_lower or any(word in query_lower for word in k.split("_")):
            match = v
            break
            
    if not match:
        return "Query not recognized under approved RBI KYC documentation policy."
    return f"Retrieved Policy: {match}\n[Mandatory: Digital KYC must be refreshed every 2 years.]"

queries = [
    "Tell me about aadhaar kyc requirements?",
    "Is PAN card required for large transfers?",
    "Can I open demat account with driving license?"
]

for q in queries:
    print(f"\nQ: {q}\nA: {retrieve_and_generate(q)}")
