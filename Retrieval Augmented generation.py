# Name: Nitya Juneja
# PRN: 1302250494
# Task: RAG Framework - Customer Dispute Resolution & Grievance

knowledge_base = {
    "chargeback": "ATM cash dispensed failure complaints are auto-resolved within T+5 business days.",
    "ombudsman": "Customers may escalate to RBI Banking Ombudsman if grievance is unresolved in 30 days.",
    "card_block": "Lost cards can be blocked instantly via SMS by sending BLOCK to 56767."
}

# Rule 1: Dispute turnaround verification
# Rule 2: Grace period rule
# Rule 3: Compensation clause disclosure

def retrieve_and_generate(query):
    query_lower = query.lower()
    match = None
    for k, v in knowledge_base.items():
        if k in query_lower or any(word in query_lower for word in k.split("_")):
            match = v
            break
            
    if not match:
        return "Grievance redressal guideline not located."
    return f"Retrieved Redressal Clause: {match}\n[Clause: Rs. 100 per day penalty payable by bank for delays beyond T+5 days.]"

queries = [
    "What is the timeline for atm chargeback dispute?",
    "When can I reach RBI ombudsman?",
    "How to cancel my mutual fund order?"
]

for q in queries:
    print(f"\nQ: {q}\nA: {retrieve_and_generate(q)}")
