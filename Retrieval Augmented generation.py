# Name: Swandan Nayak
# PRN: 1302250597
# Task: RAG Framework - Credit Cards & Rewards Rules

knowledge_base = {
    "reward_points": "Points can be redeemed for air miles at a conversion rate of 1 point = 0.5 air miles.",
    "lounge_access": "Complimentary airport lounge access is limited to 2 visits per calendar quarter.",
    "late_fee": "Late payment fee of Rs. 750 applies on outstanding balance over Rs. 10,000."
}

# Rule 1: Strict query retrieval
# Rule 2: Minimum spend validation check
# Rule 3: Grace period disclosure

def retrieve_and_generate(query):
    query_lower = query.lower()
    match = None
    for k, v in knowledge_base.items():
        if k in query_lower or any(word in query_lower for word in k.split("_")):
            match = v
            break
            
    if not match:
        return "No specific reward/card rule found in repository."
    return f"Retrieved Card Policy: {match}\n[Note: 3-day grace period applicable post due date.]"

queries = [
    "What is the policy for reward points conversion?",
    "How many lounge access visits are free?",
    "Can I apply for cashback card?"
]

for q in queries:
    print(f"\nQ: {q}\nA: {retrieve_and_generate(q)}")
