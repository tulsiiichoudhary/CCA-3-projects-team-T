# Name: Mohammad Rehan
# PRN: 1302250270
# Task: RAG Framework - Fixed Deposits & Interest Rates

knowledge_base = {
    "fd_rates": "Senior citizens get an extra 0.50% interest on tenure above 1 year.",
    "premature_withdrawal": "1% penalty deducted from contracted interest rate on early FD break.",
    "tax_saver_fd": "5-year Tax Saver FD has a lock-in period with no premature liquidation permitted."
}

# Rule 1: Deposit verification constraint
# Rule 2: Minimum deposit value alert
# Rule 3: Tax benefit limitation notice

def retrieve_and_generate(query):
    query_lower = query.lower()
    match = None
    for k, v in knowledge_base.items():
        if k in query_lower or any(word in query_lower for word in k.split("_")):
            match = v
            break
            
    if not match:
        return "Deposit guideline not found in current circular."
    return f"Retrieved Terms: {match}\n[Regulatory Rule: TDS applies if interest exceeds threshold.]"

queries = [
    "What are fd rates for senior citizens?",
    "Can I break my tax saver fd early?",
    "What is the gold loan interest rate?"
]

for q in queries:
    print(f"\nQ: {q}\nA: {retrieve_and_generate(q)}")
