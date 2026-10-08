# Name: Tulsi Choudhary
# PRN: 1302250705
# Task: ML Framework - Retrieval-Augmented Generation (RAG) with Custom Business Rules

knowledge_base = {
    "personal_loan": "Personal loans have an interest rate of 11.5% with a repayment tenure up to 5 years.",
    "credit_card": "Credit card annual fees are waived if annual spends exceed Rs. 50,000.",
    "foreclosure": "Zero penalty on home loan foreclosure after 12 successful EMI repayments."
}

# Added Strict Generation Rules:
# Rule 1: Grounded Response - Only answer from retrieved context.
# Rule 2: Fallback Disclosure - If no relevant context found, decline gracefully.
# Rule 3: Compliance Warning - Always append a risk caveat to loan queries.

def retrieve_and_generate(query):
    query_lower = query.lower()
    retrieved_info = None

    for key, doc in knowledge_base.items():
        if key in query_lower or any(word in query_lower for word in key.split("_")):
            retrieved_info = doc
            break

    # Applying Rule 1 & 2
    if not retrieved_info:
        return "I apologize, but this information is not available in the approved policy documents."

    # Applying Rule 3
    compliance_tag = "\n[Compliance Note: Interest rates and terms are subject to credit bureau verification.]"
    return f"Retrieved Context: {retrieved_info}{compliance_tag}"

# Test Queries
queries = [
    "What are the terms for personal loan?",
    "Tell me about crypto trading investments?",
    "How to waive credit card fee?"
]

print("=== RAG Response System with Rules ===")
for q in queries:
    print(f"\nQuery: {q}")
    print(f"Output:\n{retrieve_and_generate(q)}")
